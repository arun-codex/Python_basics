import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

# pip install packet
recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "b3dd6a6c4a9341df9743cbe2f286c06d"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
         webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=b3dd6a6c4a9341df9743cbe2f286c06d")
        if r.status_code == 200:
            # parse thee JSON response
            data = r.json()

            # Extract the articles
            articles = data.get('articles', [])

            # Print the headlines
            for article in articles:
                speak(articles['title'])

    else 

if __name__ == "__main__":
    speak("Initializing jarvis.....")
    while True: 
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source) 
            command = r.recognize_google(audio)
            if(command.lower() == "jarvis"):
                speak("Ya")
                # listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
            
        except Exception as e:
            print("Error; {0}".format(e))
