# Project: Golden-AI-Powered-Voice-Assistant.
 🔊 Golden AI Powered Voice Assistant

Golden AI Powered Voice Assistant is a Python project that enables hands-free control of a computer using voice commands.  
The assistant can open applications and websites, play music, tell the time, read news, and answer general queries using the Groq LLaMA AI model.

---

 ✨ Features

- Voice activation using the wake word **“Golden”**
- Open websites: Google, YouTube, Facebook, LinkedIn
- Open system applications: Notepad, File Explorer, Downloads, Camera, Settings, Browser
- Shutdown / power-off command
- Play preset songs from the music library
- Read latest news headlines
- Tell the current time
- Respond to general queries using AI

---

🧠 Tech Stack

| Component | Technology |
|----------|-------------|
| Programming Language | Python |
| Speech to Text | SpeechRecognition |
| Text to Speech | pyttsx3 |
| Browser / Web Automation | webbrowser |
| System Control | subprocess, os |
| News Data | NewsAPI |
| AI Response | Groq LLaMA |

⚙️ Installation

1. Clone the Repository
   
git clone https://github.com/Goldenkumar97/Golden-AI-Powered-Voice-Assistant.git
cd Golden-AI-Powered-Voice-Assistant

3. Create a Virtual Environment (Recommended)

python -m venv venv

to activate it.

   • Windows
     venv\Scripts\activate
   
   • Linux / macOS
     source venv/bin/activate

4. Install Required Dependencies
   
code- pip install -r requirements.txt

| If requirements.txt is not present, install manually:

code- pip install speechrecognition pyttsx3 requests newsapi-python

▶️ How to Run the Project
bash
code- python main.py

| Make sure your microphone is connected and working.

🗣️ Usage Instructions

1. Run the program.

2. Say the wake word “Golden”.

3. Give voice commands such as:

    ⦿ “Open Google”
   
    ⦿ “Play music”
   
    ⦿ “What is the time?”
   
    ⦿ “Read today’s news”
   
    ⦿ Ask general questions

🔐 API Configuration (Required)
 This project uses external APIs.
 
 Create a .env file in the root directory: 
 
   NEWS_API_KEY=your_newsapi_key_here
   
   GROQ_API_KEY=your_groq_api_key_here
