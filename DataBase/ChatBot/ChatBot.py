import random

Hello=['hello','I need your help jarvis','Help Me', 'Kha Ho Jarvis','hola']

reply_Hello=['Hello Maam, Welcome Back!', 'Always For You Sir!','How Can I Help You?','Good to have you again sir, how may I help you','I am here maam, tell me what is the issue' ]

Bye=['bye','go and sleep', 'go','good bye','ok bye, jarvis','shut up jarvis']

reply_Bye=['Bye sir, Nice meeting you!', 'Bye Sir, Hope You Love My Work!', 'If you want me to come back again.. You can just say Wake Up Jarvis.', ' It would be a great meeting you again sir','Bye, As your wish sir','Have A Good Day Sir, Nice Meeting You!']

How_Are_You=['How are you Jarvis']

reply_how=["I'm fine ma'am", "Good Doing"]

nice=['nice','good','thanks']

reply_nice=['Thanks.','Ohh, It is Good to hear that.','Thanks to you']

Functions=['functions','abilities','what can you do','features']

reply_Functions=['I can perform many tasks or varieties of tasks, how can I help you?','I can message your mom that you are playing now',
'Let Me Ask you first, How can I help you?','If you want me to tell my features , call : print features']

sorry_reply=['Sorry, That is beyond my abilities','Sorry, I can not do that','Sorry, that is above me.']

def chatterBot(Text):
    Text=str(Text)
    for word in Text.split():
        if word in Hello:
            reply=random.choice(reply_Hello)
            return reply

        elif word in Bye:
            reply=random.choice(reply_Bye)
            return reply

        elif word in How_Are_You:
            reply=random.choice(reply_how)
            return reply

        elif word in nice:
            reply=random.choce(reply_nice)
            return reply

        elif word in Functions:
            reply=random.choice(reply_Functions)
            return reply

        else:
            return random.choice(sorry_reply)

value=chatterBot('hello')
print(value)                                

