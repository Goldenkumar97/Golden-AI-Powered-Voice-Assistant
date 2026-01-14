# 🔊 Golden AI Powered Voice Assistant

Golden AI Powered Voice Assistant is a Python-based project that enables hands-free control of a computer using voice commands.  
The assistant can open applications and websites, play music, tell the time, read news, and answer general queries using the **Groq LLaMA AI model**.

---

## ✨ Features

- Voice activation using the wake word **“Golden”**
- Open websites: Google, YouTube, Facebook, LinkedIn
- Open system applications: Notepad, File Explorer, Downloads, Camera, Settings, Browser
- Shutdown / power-off command
- Play preset songs from the music library
- Read latest news headlines
- Tell the current time
- Respond to general queries using AI

---

## 🧠 Tech Stack

| Component | Technology |
|----------|------------|
| Programming Language | Python |
| Speech to Text | SpeechRecognition |
| Text to Speech | pyttsx3 |
| Browser / Web Automation | webbrowser |
| System Control | subprocess, os |
| News Data | NewsAPI |
| AI Response Engine | Groq LLaMA |

---


## ⚙️ Installation

## 1. Clone the Repository
```bash
git clone https://github.com/Goldenkumar97/Golden-AI-Powered-Voice-Assistant.git
cd Golden-AI-Powered-Voice-Assistant
```
2. Create a Virtual Environment (Recommended)
```bash
python -m venv venv
```
Activate it:

• Windows

```bash
venv\Scripts\activate
```

• Linux / macOS
```bash
source venv/bin/activate
```
3. Install Required Dependencies
```bash
pip install -r requirements.txt
```
If requirements.txt is not present:
```bash
pip install speechrecognition pyttsx3 requests newsapi-python
```
---
## ▶️ How to Run the Project

```bash
python main.py
```
Make sure your microphone is connected and working.

---

## 🗣️ Usage Instructions
1. Run the program.

2. Say the wake word “Golden”.

3. Give voice commands such as:

    “Open Google”

    “Play music”

    “What is the time?”

    “Read today’s news”

    Ask general questions

---
## 🔐 API Configuration (Required)

Create a file in the root directory:
 
    env
    NEWS_API_KEY=your_newsapi_key_here

    GROQ_API_KEY=your_groq_api_key_here
---
## 📁 Project Structure

    txt
    Golden-AI-Powered-Voice-Assistant/
    ├── main.py
    ├── README.md
    ├── requirements.txt
    └── .git/

---
## 📦 requirements.txt

    txt
    speechrecognition
    pyttsx3
    requests
    newsapi-python
    
Install dependencies:    
```bash
pip install -r requirements.txt
```
## API Reference

This project uses external APIs to fetch news data and generate AI-based responses.

---

### 🔹Get Latest News Headlines

Fetches the latest news headlines using **NewsAPI**.

```http
    https://newsapi.org/v2/top-headlines
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Country` | `string` | Country code (e.g. in, us) |
| `api_key` | `string` | Required. Your NewsAPI key |

### 🔹Get AI Response (Groq LLaMA)

Generates intelligent responses for general user queries using Groq LLaMA.

```http
   https://api.groq.com/openai/v1/chat/completions
```

| Key | Value   
| :-------- | :------- |
| `Authorization` | `Bearer GROQ_API_KEY` | 
| `Content-Type` | `application/json` | 


## Screenshots


https://github.com/Goldenkumar97/Golden-AI-Powered-Voice-Assistant/blob/main/Screenshot%202025-12-08%20151945.png
