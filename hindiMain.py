
import speech_recognition as sr

from jarvis import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[4].id)
engine.setProperty('rate',190)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# explicit function to take input commands
# and recognize them
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
            query = r.recognize_google(audio, language='hi-In')
            print(f"User said: {query}\n")

        except Exception as e:
            print(e)
            speak("Pardon Ma'am! Would you please repeat that?")
            print("Pardon Ma'am! Would you please repeat that?")
            return "None"
        return query

def TaskExe():
    while True:
        query = takeCommand().lower()


        if query==0:
            continue

        elif 'hello' or 'नमस्ते' in query:
            speak("नमस्ते सर आप कैसे हो?")

        elif ' मैं अच्छा हूँ, आप कैसे जार्विस हैं?' or 'मै ठीक हूँ' in query:
            speak("मैं भी ठीक हूँ धन्यवाद")   

TaskExe()