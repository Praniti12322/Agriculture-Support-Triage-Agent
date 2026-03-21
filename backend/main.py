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
import re
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
    allow_origins=[
        "http://localhost:3000", 
        "http://127.0.0.1:3000",
        "http://3.110.128.84"
    ],
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
    image_base64 = payload.get("image") # Base64 encoded image data (without prefix)

    if not message and not image_base64:
        return {"response": "Please provide a crop issue description or an image.", "image": ""}
        
    system_prompt = "You are an expert agricultural AI assistant analyzing crop issues. "
    
    if image_base64:
        # Vision-specific prompt
        prompt_content = [
            {
                "type": "text",
                "text": f"Analyze this crop image. User query: {message or 'What is the problem with this crop?'}. Location: {location}. "
                        "Identify the crop, the problem (pest, disease, nutrient deficiency), and suggest a solution. "
                        "Determine urgency: Low, Medium, or High. "
                        "IMPORTANT: You MUST start your response with exactly: [[URGENCY: LEVEL]] where LEVEL is LOW, MEDIUM, or HIGH. "
                        "Format response as: [[URGENCY: LEVEL]] **Crop Name**: ... **Urgency**: ... **Solution**: ..."
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{image_base64}"
                }
            }
        ]
        model_name = "meta-llama/llama-4-scout-17b-16e-instruct"
    else:
        # Text-only prompt
        prompt_content = f"""You are an expert agricultural AI assistant analyzing crop issues.

User query: "{message}"
Location: {location}

Analyze the situation and determine the urgency level: Low, Medium, or High.

IMPORTANT: You MUST start your response with exactly: [[URGENCY: LEVEL]] where LEVEL is LOW, MEDIUM, or HIGH.

Please provide a detailed, structured response formatted as follows:
[[URGENCY: LOW/MEDIUM/HIGH]]
**Crop Name**: [Identify the crop and variety if applicable]
**Urgency**: [Acknowledge the detected urgency level and explain the timeframe for action]
**Location/Plant Part Affected**: [Tailor advice for {location} if relevant, and describe parts affected]
**Time/Growth Stage**: [Time of year or growth stage when this issue typically occurs]
**Solution**: [Detailed, actionable suggestions or treatments to resolve the problem]

Ensure the tone is helpful and informative.
"""
        model_name = os.environ.get("MODEL", "llama3-8b-8192")

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt_content,
                }
            ],
            model=model_name,
        )
            
        content = chat_completion.choices[0].message.content
        
        # Robust urgency extraction using regex (case-insensitive)
        detected_urgency = "Medium"
        urgency_match = re.search(r"\[\[URGENCY:\s*(HIGH|MEDIUM|LOW)\]\]", content, re.IGNORECASE)
        
        if urgency_match:
            detected_urgency = urgency_match.group(1).capitalize()
        elif "HIGH" in content.upper() and ("urgent" in content.lower() or "critical" in content.lower()):
            detected_urgency = "High"
        elif "LOW" in content.upper():
             # Check if it's explicitly low
             if "low urgency" in content.lower() or "low priority" in content.lower():
                 detected_urgency = "Low"
            
        # Clean up response to remove the internal tag (case-insensitive)
        cleaned_content = re.sub(r"\[\[URGENCY:\s*(HIGH|MEDIUM|LOW)\]\]", "", content, flags=re.IGNORECASE).strip()
            
        return {"response": cleaned_content, "urgency": detected_urgency, "image": ""}
    except Exception as e:
        error_msg = str(e)
        if "429" in error_msg or "rate_limit" in error_msg.lower():
            return {
                "response": "**API Quota Exceeded:** We are currently receiving too many requests. Please try again in a few moments.", 
                "image": ""
            }
        return {"response": f"Error generating response: {error_msg}", "image": ""}
