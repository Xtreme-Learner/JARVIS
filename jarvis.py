import pyttsx3 
import speech_recognition as sr 
import datetime
import time
import random
import requests
import wikipedia 
import webbrowser
import os
import smtplib
import subprocess
import json
import wolframalpha
import pyjokes
from urllib.request import urlopen
import pywhatkit
import pyautogui
import keyboard
from playsound import playsound
from googletrans import Translator
from gtts import gTTS
from bs4 import BeautifulSoup
import PyPDF2
import speedtest
from pywikihow import search_wikihow
from notifypy import Notify
import train
import NN
import brain

# import Hotwart_Detection

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
            print(e)
            speak("Pardon Ma'am! Would you please repeat that?")
            print("Pardon Ma'am! Would you please repeat that?")
            return "None"
        return query

print("Loading your JARVIS AI Personal Assistant ")
speak("Loading your JARVIS AI Personal Assistant")    



def tellDay():
      
    day = datetime.datetime.today().weekday() + 1
      
    Day_dict = {1: 'Monday', 2: 'Tuesday', 
                3: 'Wednesday', 4: 'Thursday', 
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
      
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)   



def takeHindi():

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
            return "None"
        return query.lower()       

def trans():
    speak("Tell me , I'm your translator!")
    line=takeHindi()
    translate=Translator()
    result=translate.translate(line) 
    Text=result.text
    speak(Text)    

def Temp():
    search="temperature in kanpur"
    url=f"https://www.google.com/search?q={search}"
    r=requests.get(url)
    data=BeautifulSoup(r.text,"html.parser")
    temperature = data.find("div",class_="BNeawe").text
    speak(f"The Temperature outside is {temperature} .")   
    print(f"The Temperature outside is {temperature} .")      

def NotePad():
    speak("Tell me the query")
    speak("I'm ready to write..")

    write=takeCommand()

    time=datetime.datetime.now().strftime("%H:%M")

    fileName=str(time).replace(":","-") + "-note.txt"

    with open(fileName,"w") as file:
        file.write(write)

    path_1="C:\\Users\\pc\\Desktop\\JARVIS\\" + str(fileName)        
    path_2="C:\\Users\\pc\\Desktop\\JARVIS\\DataBase\\NotePad\\" + str(fileName)

    os.rename(path_1,path_2)
    os.startfile(path_2)

def Reader():
    speak("Tell me the name of the book")

    name=takeCommand()

    if 'india' in name:
        os.startfile("C:\\Users\\pc\\Documents\\Moral Stories.pdf") 
        book=open("C:\\Users\\pc\\Documents\\Moral Stories.pdf","rb")
        pdfreader=PyPDF2.PdfFileReader(book)
        pages=pdfreader.getNumPages()
        speak(f"Number of Pages in this book are {pages}")
        speak("From which page I have to start reading?")
        numPage=takeCommand()
        page=pdfreader.getPage(numPage)
        text=page.extractText()
        speak("In which language, I have to read?")
        lang=takeCommand()

        if 'hindi' in lang:
            transl=Translator()
            textHin=transl.translate(text,'hi')
            textm=textHin.text
            speech=gTTS(text=textm)
            try:
                speech.save("engine = pyttsx3.init('sapi5')",
"voices = engine.getProperty('voices')",
"engine.setProperty('voice', voices[0].id)",
"engine.setProperty('rate',190)")
                playsound("engine = pyttsx3.init('sapi5')",
"voices = engine.getProperty('voices')",
"engine.setProperty('voice', voices[0].id)",
"engine.setProperty('rate',190)")
            except:
                playsound("engine = pyttsx3.init('sapi5')",
"voices = engine.getProperty('voices')",
"engine.setProperty('voice', voices[0].id)",
"engine.setProperty('rate',190)")

        else:
            speak(text)            

def SpeedTest():
    speak("Checking speed...")
    speed=speedtest.Speedtest()
    downloading=speed.download()
    correctDown=int(downloading/800000)
    uploading=speed.upload()
    correctUpload=int(uploading/800000)

    if 'uploading' in query:
        speak(f"The uploading speed is {correctUpload} mbps")
        print(f"The uploading speed is {correctUpload} mbps")

    elif 'downloading' in query:
        speak(f"The downloading speed is {correctDown} mbps")
        print(f"The downloading speed is {correctDown} mbps")

    else:
        speak(f"The downloading speed is {correctDown} mbps and the uploading speed is {correctUpload} mbps")
        print(f"The downloading speed is {correctDown} mbps and the uploading speed is {correctUpload} mbps")   

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('adweteeya9916@gmail.com', '@Dw3teey')
    server.sendmail('adweteeya1999@gmail.com', to, content)
    server.close()
 

def OpenApps():
    speak("Ok ma'am, Wait a second!")

    if 'code' in query:
        os.startfile("C:\\Users\\pc\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\")

    elif 'chrome'  in query:
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")       

def CloseApps():
    speak("Ok, ma'am, wait a second!")

    if  'notepad' in query:
        os.system("TASKKILL /F /im Notepad.exe")

    elif 'code' in query:
        os.system("TASKKILL /F /im Code.exe") 

    elif 'chrome' in query:
        os.system("TASKKILL /F /im chrome.exe")

    elif 'youtube' in query:
        os.system("TASKKILL /F /im chrome.exe")
                          
def TimeTable():

    speak("Checking......")
    from DataBase.TimeTable.TimeTable import Time

    value=Time()
    Noti=Notify()
    Noti.title="TimeTable"
    Noti.message=str(value)
    Noti.audio="C:\\Users\\pc\\Desktop\\JARVIS\\notification_sound.wav"
    Noti.send()

    speak("Anything Else Sir?")

if __name__ == "__main__":
    clear = lambda: os.system('cls')

    clear()
    wishMe()
    while True:
        query = takeCommand().lower()


        if query==0:
            continue

        elif ' from wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(str(results.encode('utf8').decode('ascii','ignore')))
            speak(results)

        elif 'news' in query:
            news=webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")    
            speak("Hera are some headlines from the Times of India, Happy reading")
            time.sleep(6)

        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open_new_tab("youtube.com")
            time.sleep(4)

        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open_new_tab("google.com")
            time.sleep(4)

        elif 'open gmail' in query:
            speak("Here your google mail open now")
            webbrowser.open_new_tab("gmail.com")
            time.sleep(4)    

        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open_new_tab("stackoverflow.com") 
            time.sleep(4)  

        # elif 'search' in query or 'search music apps' in query:
        #     query=query.replace("search", "")
        #     query = query.replace("search music apps", "") 
        #     webbrowser.open_new_tab(query)
        #     time.sleep(5)
        

        elif 'repeat my words' in query:
            speak("Speak Sir!")
            jj=takeCommand()
            speak(f"You Said : {jj}")


        elif 'whatsapp' in query:
            try:
                pywhatkit.sendwhatmsg_to_group("CcVNibJcjmy3TIfUZkP9Dg", "Hey dear, whatsup?", 15, 47,2)
                print("Successfully sent!")
                speak("Successfully sent!")

            except:
                print("An Unexcepted Error!!")  

        elif 'send message' in query:
            try:
                speak("Tell me the message to send!")
                msg=takeCommand()
                speak("Tell me the time sir!")
                speak("tell me in hour!")
                hour=int(takeCommand())
                speak("time in minutes!")
                minutes=int(takeCommand())
                pywhatkit.sendwhatmsg("+918840875630", msg, hour, minutes, 2)  
                print("Successfully sent!")
                speak("Successfully sent!") 
            except:
                print("An Unexcepted Error!!")  



        elif 'instant message' in query:
            try:
                pywhatkit.sendwhatmsg_to_group_instantly("Random", "Hey All!")   
                print("Successfully sent!")
                speak("successfully sent!")

            except:
                print("An Unexpected error!!")     

        elif 'send image to group' in query:
                pywhatkit.sendwhats_image("Random", "Images/Hello.png", "Hello") 
                print("Successfully sent!")
                speak("successfully sent!")

        elif 'send image' in query:
                pywhatkit.sendwhats_image("+916397277985", "image.jpg") 
                print("Successfully sent!")
                speak("successfully sent!")        


        elif 'downloading speed' in query:
            SpeedTest()

        elif 'uploading speed' in query:
            SpeedTest()

        elif 'internet speed' in query:
            SpeedTest()        
          

        elif 'my location' in query:
            speak("OK ma'am, wait for a second.")
            webbrowser.open('https://www.google.co.in/maps/place/Barra+4,+Neemeshwar+MahaMandir+Society,+Barra+World+Bank,+Barra,+Kanpur,+Uttar+Pradesh+208022/@26.4402648,80.2890314,17z/data=!3m1!4b1!4m5!3m4!1s0x399c47c25b7175a3:0xf09813720f7eefc!8m2!3d26.4402648!4d80.2912201')    


        elif 'World Affairs' in query:
             
            try:
                jsonObj = urlopen('''https://newsapi.org/v2/top-headlines?country=in&apiKey=3aa9eb3c307c4641934dce0c62c264f6''')
                data = json.load(jsonObj)
                i = 1
                 
                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============'''+ '\n')
                 
                for item in data['articles']:
                     
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                 
                print(str(e))    

        elif 'sports' in query:
             
            try:
                jsonObj = urlopen('''https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=3aa9eb3c307c4641934dce0c62c264f6
''')
                data = json.load(jsonObj)
                i = 1
                 
                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============'''+ '\n')
                 
                for item in data['articles']:
                     
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                 
                print(str(e))           


        elif 'technology' in query:
             
            try:
                jsonObj = urlopen('''https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=3aa9eb3c307c4641934dce0c62c264f6
''')
                data = json.load(jsonObj)
                i = 1
                 
                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============'''+ '\n')
                 
                for item in data['articles']:
                     
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                 
                print(str(e))           
        

        elif 'temperature' in query:
            Temp()


        elif "tell me your name" in query:
            speak("I am JARVIS. Your deskstop Assistant")    


        elif 'music' in query:
            speak("Here you go with music")
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)    
            random=os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play song' in query:
            song=takeCommand().replace("play song", " ")
            speak("playing" + 'song')
            pywhatkit.playonyt(song)  

           
        
        elif "what day it is" in query:
            tellDay()    

        elif 'tell me the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%p")    
            speak(f"Ma'am, the time is {strTime}")
            print(f"Ma'am, the time is {strTime}")

        elif 'translator' in query:
            trans()    

        elif 'pdf reader' in query:
            Reader()    

        elif 'alarm' in query:
            speak("enter the time!")
            time=input("=> Enter the time : ")

            while True:
                Time_Ac=datetime.datetime.now()
                now=Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    speak("Time to Wake Up!")
                    playsound("beatiful-sms meloboom.mp3")
                    speak("Alarm Closed!")

                elif now>time:
                    break      


        elif 'weather' in query:
            api_key="9d15eff2acdc5cb25563f187392f21f6"
            base_url="https://api.openweathermap.org//data//2.5//weather?"
            speak("what is the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response= requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature= y["temp"]
                current_humidity= y["humidity"]
                z=x["weather"]
                weather_description=z[0]["description"]
                speak("Temperature in kelvin unit is " + str(current_temperature) + "\n humidity in percentage is " + str(current_humidity)+ "\n description " + str(weather_description))
                print("Temperature in kelvin unit =" + str(current_temperature)+ "\n humidity(in percentage)=" + str(current_humidity)+ "\n description= "+
                str(weather_description))          

        elif 'pause' in query:
            keyboard.press('space bar')

        elif 'restart' in query:
            keyboard.press('0') 

        elif 'mute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('l')

        elif 'back' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'film mode' in query:
            keyboard.press('t')      


        elif 'close this tab' in query:
            keyboard.press('ctrl + w')       

        elif 'open new tab' in query:
            keyboard.press('ctrl + t')

        elif 'open new window' in query:
            keyboard.press('ctrl + n')

        elif 'history' in query:
            keyboard.press('ctrl + h')                                                   
 

        elif 'joke' in query:
            speak(pyjokes.get_joke())    
            print(pyjokes.get_joke())    

        elif 'break' in query:
            speak("Ok Ma'am , You can call me anytime!")
            speak("Just Say Wake Up Jarvis")
            break
        
        elif 'open code' in query:
            OpenApps()

        elif 'open chrome' in query:
            OpenApps()

        elif 'ask me anything' in query:
            speak("Getting data from the internet!")
            op=query.replace("jarvis","")
            max_result=1
            how_to_func=search_wikihow(op,max_result)
            assert len(how_to_func)==1
            how_to_func[0].print()
            speak(how_to_func[0].summary)

        elif 'email to Edward' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "adweteeya1999@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Ma'am. I am not able to send this email") 

        elif 'send a mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("whome should i send")
                to = input()   
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")  

        elif "calculate" in query:
             
            app_id = "WJVYPR-QEVWQW3PKK"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)    

        elif "give an answer " in query:
            speak("what's your question to answer?")
            question = takeCommand()
            app_id = "WJVYPR-QEVWQW3PKK"
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            print(answer)
            speak(answer)   

        elif 'google search' in query:
            import wikipedia as googleScrap
            query=query.replace("Jarvis","")
            query=query.replace("google search","") 
            query=query.replace("google","")
            speak("This is what I have found on google!")
            pywhatkit.search(query)

            try:
                result=googleScrap.summary(query,3)
                speak(result)
                print(result)

            except:
                speak("No speakable data Available")       

        elif "screenshot" in query:
            speak("Ok ma'am , What should I name that file?")
            path=takeCommand()
            path1_name=path + ".png" 
            path1= "E:\\Screenshots\\"+ path1_name
            kk=pyautogui.screenshot()  
            kk.save(path1)
            os.startfile("E:\\Screenshots")
            speak("Here is your screenshot.") 
        


        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Ma'am")
 
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")    

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Adweteeya.")

        elif 'reason for your' in query:
            speak("I am created as a Major project by Adweteeya and Rajat . I'm still in developing and evolving mode.")    
            speak("I can do many stuffs for you as still I'am developing so bear with me.")


        elif "who i am" in query:
            speak("If you talk then definitely your human.")

        elif 'open presentation' in query:
            speak("opening Power Point presentation")
            power =r"C:\\Users\\pc\\Desktop\\JarvisPresentation"
            os.startfile(power) 

        elif 'remember that' in query:
            rememberMsg=query.replace("remember this","")
            rememberMsg=rememberMsg.replace("jarvis","")
            speak("You Ask Me To Remind You That:" + rememberMsg)
            remember=open('data.txt','w')
            remember.write(rememberMsg)
            remember.close()

        elif 'what you have remembered'in query:
            remember=open('data.txt','r')
            speak("You  Ask Me To Remind You That" + remember.read())    


        elif 'you need a break' in query:
            speak("Ok maam , You Can Call Me Anytime!")
            speak("Just You Need To Say Wake Up Jarvis!")    
            break

 
        elif 'log off' in query or 'sign out' in query:
            speak("Ok, you pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])    

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)    

   
        elif 'thank you' in query:
            speak("I'm happy to help you. Thanks for giving me your time")
            print("I'm happy to help you. Thanks for giving me your time")

        elif 'bye' in query:
            speak("Now JARVIS your AI personal assistant is shutting down, good bye")
            print("Now JARVIS your AI personal assistant is shutting down, good bye")
            exit()

        elif 'write a note' in query:
            NotePad()

        elif 'close note' in query:
            CloseApps()        

        elif 'close youtube' in query:
            CloseApps()

        elif 'close chrome' in query:
            CloseApps()        

        elif 'time table' in query:
            TimeTable()    

              

        else:
            from DataBase.ChatBot.ChatBot import chatterBot
            reply=chatterBot(query)
            speak(reply)

            if 'bye' in query:
                break

            elif 'exit' in query:
                break

            elif 'go' in query:
                break

