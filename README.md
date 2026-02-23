🌾 Agriculture Support Triage Agent (AI)

An AI-powered Agriculture Assistance System that analyzes farmers' problems in real time and generates intelligent solutions using Qube AI (LLM API).

The system acts as a first-level support agent — it understands the farmer’s issue, determines urgency, extracts important details, and provides a helpful response through a simple GUI.

🚜 Features

Real-time agriculture query analysis

Urgency classification (Low / Medium / High / Emergency)

Intent detection (disease, pest, irrigation, fertilizer, weather, etc.)

Named Entity Recognition (crop, location, date, symptoms)

AI generated farmer-friendly suggestions

Hindi + English input support

Desktop GUI interface (Tkinter)

Fast response using Qube AI LLM API

🧠 How It Works

Farmer types problem in the GUI

System sends query to Qube AI

AI processes text using structured prompt

Returns structured JSON containing:

Urgency level

Problem category

Extracted information

Suggested solution

🖥️ Tech Stack
Technology	Purpose
Python	Backend logic
Tkinter	GUI
Requests	API communication
Qube AI (LLM API)	Natural Language Understanding
dotenv	Secure API key handling
📂 Project Structure
Agriculture-Triage-Agent
│── agri_triage_agent.py
│── .env
│── README.md

⚙️ Installation
1. Clone Repository
git clone https://github.com/your-username/Agriculture-Triage-Agent.git
cd Agriculture-Triage-Agent

2. Install Dependencies
pip install requests python-dotenv

🔑 Setup API Key

Create .env file:

QUBE_API_KEY=your_api_key_here
QUBE_API_URL=https://api.qube.ai/v1/chat/completions

▶️ Run the Application
python agri_triage_agent.py


The Agriculture AI GUI will open.

💡 Example Query

"My tomato leaves are turning yellow and small insects are visible since 3 days"

AI Output:

Urgency: Medium

Intent: Pest attack

Crop: Tomato

Suggestion: Spray neem oil or imidacloprid pesticide

🎯 Objective

To reduce delay in agricultural advisory support by providing instant AI-generated assistance and prioritizing serious crop problems.

📈 Future Enhancements

Farmer database & ticket system

Image-based crop disease detection

WhatsApp chatbot integration

Government scheme recommendations

Multi-language support

👨‍💻 Author

Developed as an AI-based smart agriculture support system project using Large Language Models.

📜 License

This project is for educational and research purposes.
