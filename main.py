import speech_recognition as sr  
import webbrowser                
import pyttsx3                  
import musicLibrary             
import requests                 
import subprocess               
import os                       
from groq import Groq          


recognizer = sr.Recognizer()
newsapi = "YOUR_NEWS_API_KEY"          # Replace this with your NewsAPI key
client = Groq(api_key="YOUR_GROQ_API_KEY")   # Replace this with your Groq API key


def speak(text):  # Speak the given text out loud and print it to the console.
    print("Golden:", text)
    engine = pyttsx3.init('sapi5')
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def processCommand(c):
    c = c.lower()
    print("Command:", c)

      # Browser & website commands 
    if "open google" in c:
        speak("Opening Google")
        webbrowser.open_new_tab("https://google.com")
    elif "open youtube" in c:
        speak("Opening YouTube")
        webbrowser.open_new_tab("https://youtube.com")
    elif "open facebook" in c:
        speak("Opening Facebook")
        webbrowser.open_new_tab("https://facebook.com")
    elif "open linkedin" in c:
        speak("Opening LinkedIn")
        webbrowser.open_new_tab("https://linkedin.com")

    #  Play music from custom music library 
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    #  Fetch and read latest news 
    elif c.strip() == "news" or "tell me the news" in c or "latest news" in c:
        speak("Getting the latest news, please wait.")
        r = requests.get(
            f"https://newsapi.org/v2/everything?q=india&pageSize=5&apiKey={newsapi}"
        )
        data = r.json()
        for a in data.get("articles", [])[:5]:
            title = a.get("title")
            if title:
                speak(title)

    #  Tell current time 
    elif "time" in c:
        from datetime import datetime
        now = datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")

    # Windows applications and system utilities 
    elif "open notepad" in c:
        speak("Opening Notepad")
        subprocess.Popen(["notepad.exe"])
    elif "open file explorer" in c or "open explorer" in c:
        speak("Opening File Explorer")
        subprocess.Popen(["explorer.exe"])
    elif "open downloads" in c:
        speak("Opening Downloads folder")
        os.startfile(os.path.join(os.path.expanduser("~"), "Downloads"))
    elif "shutdown" in c or "power off" in c:
        speak("Shutting down your system")
        os.system("shutdown /s /t 0")
    elif "open browser" in c:
        speak("Opening Browser")
        os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

    # apps 
    elif "open camera" in c:
        speak("Opening Camera")
        subprocess.Popen(["start", "microsoft.windows.camera:", ""], shell=True)
    elif "open settings" in c or "open setting" in c:
        speak("Opening Settings")
        subprocess.Popen(["start", "ms-settings:"], shell=True)
    elif "open whatsapp" in c:
        speak("Opening WhatsApp")
        os.startfile(r"C:\Users\user_name\Desktop\WhatsApp.lnk")    # Replace your path

    # Fallback: AI response from Groq LLM 
    else:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are Golden, a friendly AI assistant"},
                {"role": "user", "content": c}
            ]
        )

        answer = response.choices[0].message.content
        speak(answer)

                # main code
if __name__ == "__main__":  # Startup message
    speak("Initializing Golden...")

    while True:
        r = sr.Recognizer()
        print("\nrecognizing...")

        try:
            # Listen for wake word 
            with sr.Microphone() as source:
                print("Listening for wake word...")
                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source, timeout=5, phrase_time_limit=2)

            word = r.recognize_google(audio, language="en-IN")
            print("You said:", word)

            # Wake word detection
            if "golden" in word.lower():
                speak("Yaa Golden, I am here. Awaiting your Command.")

                # Listen for the actual command 
                with sr.Microphone() as source:
                    print("Golden active... listening for command")
                    r.adjust_for_ambient_noise(source, duration=0.5)
                    cmd_audio = r.listen(source, timeout=7, phrase_time_limit=5)

                command = r.recognize_google(cmd_audio, language="en-IN")
                print("Recognized command:", command)

                # Process the command
                processCommand(command)

        # Error handling for common speech issues 
        except sr.WaitTimeoutError:
            print("Timeout: no speech, trying again...")
        except sr.UnknownValueError:
            print("Could not understand audio, say again...")
        except KeyboardInterrupt:
            print("\nProgram stopped by user.")
            break
        except Exception as e:
            print("Error:", e)
