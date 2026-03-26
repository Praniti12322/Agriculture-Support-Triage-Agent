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
- **🏗️ Infrastructure as Code (IaC)**: Automated provisioning of AWS infrastructure using Terraform for scalability and reliability.

## 🛠️ Tech Stack

- **Frontend**: React.js, Vanilla CSS
- **Backend**: FastAPI (Python), SQLModel (SQLite)
- **AI Vision Engine**: Groq API (`meta-llama/llama-4-scout-17b-16e-instruct`)
- **AI Text Engine**: Groq API (`llama-3.1-8b-instant`)
- **Infrastructure**: Terraform (IaC), AWS (EC2), Docker, MicroK8s

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- [Python 3.8+](https://www.python.org/downloads/)
- [Node.js (v14+) and npm](https://nodejs.org/en/download/)
- [Terraform](https://developer.hashicorp.com/terraform/downloads) (for infrastructure setup)
- A [Groq Cloud API Key](https://console.groq.com/keys)

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd Agriculture-Support-Triage-Agent
```

### 2. Infrastructure Setup (Terraform) 🌐

Automation ke liye Terraform ka use karein:

1. Navigate to the terraform directory:
   ```powershell
   cd terraform
   ```
2. Set your AWS Credentials (current session):
   ```powershell
   $env:AWS_ACCESS_KEY_ID="your_access_key"
   $env:AWS_SECRET_ACCESS_KEY="your_secret_key"
   ```
3. Initialize and Plan:
   ```powershell
   .\terraform.exe init
   .\terraform.exe plan
   ```
4. Deploy (Optional):
   ```powershell
   .\terraform.exe apply
   ```

### 3. Backend Setup (FastAPI)

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

4. Create a `.env` file in the `backend/` folder:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   MODEL=llama-3.1-8b-instant
   ```

5. Run the backend server:
   ```bash
   uvicorn main:app --reload
   ```

### 4. Frontend Setup (React)

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies and start:
   ```bash
   npm install
   npm start
   ```

---

## 🎤 How to Present in a Meeting

Meeting mein ye points highlight karein:

1. **Automation (IaC)**: "Humne manual infrastructure setup ko khatam kar diya hai. Ab Terraform use karke hum 5 minute mein pura AWS environment automatically khada kar sakte hain."
2. **Scalability**: "Infrastructure as Code hone ki wajah se hum project ko asani se scale kar sakte hain aur manual configuration errors zero ho gaye hain."
3. **Consistency**: "Jo setup mere local system par hai, wahi exact setup production server par bhi hoga, thanks to Terraform and Docker."
4. **Disaster Recovery**: "Agar hamara server down hota hai, to hum `terraform apply` run karke naya server turant ready kar sakte hain."

---

## 📖 How to Use

1. **Sign Up / Login**: User account banayein ya login karein.
2. **Select Language**: Voice input ke liye EN ya हिन्दी choose karein.
3. **Voice/Text Query**: Mic icon use karein ya type karein.
4. **Capture Crop Problem**: Camera icon use karke photo click karein.
5. **AI Response**: AI aapko solution aur urgency level (Low/Medium/High) provide karega.

## 👨‍💻 Project Structure

```
Agriculture-Support-Triage-Agent/
├── backend/                # FastAPI source code
│   ├── main.py             # API endpoints & AI logic
│   └── ...
├── frontend/               # React source code
│   ├── src/App.js          # main Chat UI
│   └── ...
├── terraform/              # Infrastructure as Code (AWS EC2, SG)
├── scripts/                # Automation & Setup scripts
└── README.md
```

## 📜 License

This project is for educational purposes. Feel free to contribute or adapt it for your own agricultural projects!
