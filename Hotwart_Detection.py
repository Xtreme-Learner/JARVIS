import speech_recognition as sr 
import os
import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',190)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<17:
        speak("Good Afternoon!")   

    elif hour>=17 and hour<23:
        speak("Good Evening!")
    else:
        speak("Good Night! Sweet Dream.")

    speak("I am your Assistant, JARVIS. Please tell me how may I help you")    
         

def takeCommand():

    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        speak("I'm listening")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        query=""
        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            return "none"

        return query.lower()  

while True:

    wake_up=takeCommand()

    if 'wake up' in wake_up:
        os.startfile("C:\\Users\\pc\\Desktop\\JARVIS\\jarvis.py")        

    else:
        print('ERROR!!!')    
