from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import JSONResponse
import traceback
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.exc import IntegrityError
from sqlmodel import select

import models
import database
import schemas
import auth

import os
from dotenv import load_dotenv
from groq import Groq

# explicitly load env vars before setting up client
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

app = FastAPI()

# allow requests from the React dev server during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


# DEBUG: return full traceback in JSON for uncaught exceptions during development
@app.exception_handler(Exception)
async def debug_exception_handler(request, exc):
    tb = traceback.format_exc()
    return JSONResponse(status_code=500, content={"detail": str(exc), "trace": tb})

@app.on_event("startup")
def on_startup():
    database.init_db()


@app.post("/signup", response_model=schemas.Token)
def signup(user: schemas.UserCreate):


    session = next(database.get_session())
    db_user = models.User(
        username=user.username,
        hashed_password=auth.get_password_hash(user.password),
    )
    session.add(db_user)
    try:
        session.commit()
        session.refresh(db_user)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Username already registered")
    access_token = auth.create_access_token(data={"sub": db_user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/login", response_model=schemas.Token)
def login(user: schemas.UserCreate):


    session = next(database.get_session())
    stmt = select(models.User).where(models.User.username == user.username)
    db_user = session.exec(stmt).first()
    if not db_user or not auth.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    access_token = auth.create_access_token(data={"sub": db_user.username})
    return {"access_token": access_token, "token_type": "bearer"}


# simple protected chat route
@app.post("/chat")
def chat(
    payload: dict,
    current_user: str = Depends(auth.get_current_user),
):
    message = payload.get("message", "")
    location = payload.get("location", "Not specified")

    if not message:
        return {"response": "Please provide a crop issue description.", "image": ""}
        
    prompt = f"""You are an expert agricultural AI assistant analyzing crop issues.

User query: "{message}"
Location: {location}

Analyze the situation and determine the urgency level: Low, Medium, or High.

Please provide a detailed, structured response formatted as follows:
[[URGENCY: LOW/MEDIUM/HIGH]]
**Crop Name**: [Identify the crop and variety if applicable]
**Urgency**: [Acknowledge the detected urgency level and explain the timeframe for action]
**Location/Plant Part Affected**: [Tailor advice for {location} if relevant, and describe parts affected]
**Time/Growth Stage**: [Time of year or growth stage when this issue typically occurs]
**Solution**: [Detailed, actionable suggestions or treatments to resolve the problem]

Ensure the tone is helpful and informative.
"""

    try:
        model_name = os.environ.get("MODEL", "llama3-8b-8192")
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model=model_name,
        )
        content = chat_completion.choices[0].message.content
        
        # Extract urgency from response
        detected_urgency = "Medium"
        if "[[URGENCY: HIGH]]" in content:
            detected_urgency = "High"
        elif "[[URGENCY: MEDIUM]]" in content:
            detected_urgency = "Medium"
        elif "[[URGENCY: LOW]]" in content:
            detected_urgency = "Low"
            
        # Clean up response to remove the internal tag
        cleaned_content = content.replace("[[URGENCY: HIGH]]", "").replace("[[URGENCY: MEDIUM]]", "").replace("[[URGENCY: LOW]]", "").strip()
            
        return {"response": cleaned_content, "urgency": detected_urgency, "image": ""}
    except Exception as e:
        error_msg = str(e)
        if "429" in error_msg or "rate_limit" in error_msg.lower():
            return {
                "response": "**API Quota Exceeded:** We are currently receiving too many requests on the Groq network. Please try again in a few moments.", 
                "image": ""
            }
        return {"response": f"Error generating response: {error_msg}", "image": ""}
