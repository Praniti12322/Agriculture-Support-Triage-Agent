# 🌾 Krishi AI Assistant

Krishi AI Assistant is a professional, AI-powered agricultural support platform designed to help farmers diagnose crop issues in real-time. It uses advanced Large Language Models (LLMs) and Vision Models via the Groq API to provide tailored advice based on crop symptoms, images, location, and automatically detected urgency levels.

## 🚀 Features

- **🎤 Voice Commands (EN/HI)**: Support for voice input in both English and Hindi for hands-free interaction.
- **📷 Camera-Based Diagnosis**: Capture or upload photos of crops for instant automated problem analysis.
- **🚦 Smart Urgency Triage**: Robust AI-driven categorization (Low, Medium, High) with improved detection logic.
- **📍 Location-Aware Support**: Tailors agricultural suggestions based on the user's specific region.
- **🎨 Modern Professional UI**: Premium, responsive chat interface with desktop and mobile support.
- **🔐 Secure Authentication**: User sign-up and login functionality with JWT-based security.
- **👁️ Vision AI Engine**: Leverages cutting-edge multimodal models on Groq for accurate visual identification.

## 🛠️ Tech Stack

- **Frontend**: React.js, Vanilla CSS
- **Backend**: FastAPI (Python), SQLModel (SQLite)
- **AI Vision Engine**: Groq API (`meta-llama/llama-4-scout-17b-16e-instruct`)
- **AI Text Engine**: Groq API (`llama-3.1-8b-instant`)
- **Authentication**: JWT (JSON Web Tokens)
- **APIs**: Web Speech API (for voice), MediaDevices API (for camera)

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
   MODEL=llama-3.1-8b-instant
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
2. **Select Language**: Toggle between **EN** (English) and **हिन्दी** (Hindi) for voice input.
3. **Voice/Text Query**: Click the 🎤 icon to speak or type your crop issue.
4. **Capture Crop Problem**: Click the 📷 icon to take a photo of your plant or upload an existing image.
5. **Set Location**: Type your growing region (e.g., "Punjab") to receive localized advice.
6. **AI Response**: The assistant will analyze both text and images to provide a structured solution with a detected urgency level.

## 👨‍💻 Project Structure

```
Agriculture-Support-Triage-Agent/
├── backend/                # FastAPI source code
│   ├── main.py             # API endpoints & AI logic (Vision + Text)
│   ├── models.py           # SQLModel database models
│   ├── auth.py             # Security & JWT logic
│   └── database.py         # DB connection setup
├── frontend/               # React source code
│   ├── src/
│   │   ├── App.js          # main Chat UI (Voice/Camera/Chat)
│   │   ├── App.css         # UI Styling & Animations
│   │   └── AuthForm.js     # Login/Signup components
│   └── public/             # Static assets (Logo, etc.)
└── README.md
```

## 📜 License

This project is for educational purposes. Feel free to contribute or adapt it for your own agricultural projects!
