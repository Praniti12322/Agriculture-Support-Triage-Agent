# 🌾 Krishi AI Assistant

Krishi AI Assistant is a professional, AI-powered agricultural support platform designed to help farmers diagnose crop issues in real-time. It uses advanced Large Language Models (LLMs) via the Groq API to provide tailored advice based on crop symptoms, location, and automatically detected urgency levels.

## 🚀 Features

- **AI-Detected Urgency**: Automatically categorizes crop issues as Low, Medium, or High urgency to provide prioritized advice.
- **Location-Aware Support**: Tailors agricultural suggestions based on the user's specific region.
- **Professional Chat Interface**: A clean, modern, and responsive UI built with React.
- **Secure Authentication**: User sign-up and login functionality with JWT-based security.
- **AI-Powered Diagnostics**: Leveraging the Groq API for fast and intelligent agricultural insights.

## 🛠️ Tech Stack

- **Frontend**: React.js, Vanilla CSS
- **Backend**: FastAPI (Python), SQLModel (SQLite)
- **AI Engine**: Groq API (Llama 3 / Mixtral models)
- **Authentication**: JWT (JSON Web Tokens)

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- [Python 3.8+](https://www.python.org/downloads/)
- [Node.js (v14+) and npm](https://nodejs.org/en/download/)
- A [Groq Cloud API Key](https://console.groq.com/keys)

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd Agriculture-Support-Triage-Agent
```

### 2. Backend Setup (FastAPI)

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the `backend/` folder and add your credentials:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   MODEL=llama3-8b-8192
   ```

5. Run the backend server:
   ```bash
   uvicorn main:app --reload
   ```
   The backend will be running at `http://127.0.0.1:8000`.

### 3. Frontend Setup (React)

1. Open a new terminal window and navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install the frontend dependencies:
   ```bash
   npm install
   ```

3. Start the React development server:
   ```bash
   npm start
   ```
   The frontend will be running at `http://localhost:3000`.

---

## 📖 How to Use

1. **Sign Up / Login**: Create an account or log in to access the assistant.
2. **Set Location**: Type your growing region (e.g., "Punjab", "Tamil Nadu") to receive localized advice.
3. **Describe Issue**: Enter your crop problem in the chat box.
4. **AI Response**: The assistant will automatically detect the urgency and provide a structured solution, including crop identification and actionable advice.

## 👨‍💻 Project Structure

```
Agriculture-Support-Triage-Agent/
├── backend/                # FastAPI source code
│   ├── main.py             # API endpoints & AI logic
│   ├── models.py           # SQLModel database models
│   ├── auth.py             # Security & JWT logic
│   └── database.py         # DB connection setup
├── frontend/               # React source code
│   ├── src/
│   │   ├── App.js          # Main Chat UI
│   │   └── AuthForm.js     # Login/Signup components
│   └── public/             # Static assets (Logo, etc.)
└── README.md
```

## 📜 License

This project is for educational purposes. Feel free to contribute or adapt it for your own agricultural projects!
