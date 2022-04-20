from datetime import datetime
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',190)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

FiveTo6= '''In This Time, You have to Get Up & Listen Something Positive.
5:00 am To 6:00 am
Thanks.
'''

SixTo9= '''In This Time, You Have To Study.
6:00 am To 9:00 am
Thanks.'''

NineTo12= '''In This Time, you have to make a vedio.
9:00 am To 12:00pm
Thanks.
'''

TwelveTo15='''In This Time,You have to gain some knowledge by surfing.
12:00 pm To 3:00 pm
Thanks.'''

TwentyTo21='''In This Time, You Have To Work On Your Major Project.
20:00 pm To 21:00 pm
Thanks.'''

TwentyOneTo22='''Fun Time
9:00 pm To 10:00 pm
Thanks.'''


def Time():
    hour=int(datetime.now().strftime("%H"))

    if hour>=5 and hour<6:
        speak(FiveTo6)
        return FiveTo6

    elif hour>=6 and hour<9:
        speak(SixTo9)
        return SixTo9

    elif hour>=9 and hour<12:
        speak(NineTo12)
        return NineTo12

    elif hour>=12 and hour<15:
        speak(TwelveTo15)
        return TwelveTo15

    elif hour>=20 and hour<21:
        speak(TwentyTo21) 
        return TwentyTo21   

    elif hour>=21 and hour<22:
        speak(TwentyOneTo22) 
        return TwentyOneTo22 

    else:
        speak("In This Time , You Have To A Rest.")
        return '''In This Time , You Have To A Rest.'''                  