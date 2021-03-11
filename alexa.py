import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import os
listner = sr.Recognizer()
engine = pyttsx3.init()
engine.say("Hey! What can I do for you?")
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait() 

def takecommand():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice =listner.listen(source)
            command=listner.recognize_google(voice)
            command=command.lower()
            if 'play' in command:
                    song=command.replace('play','')
                    pywhatkit.playonyt(song)
                    print('Playing'+song)
                    talk('Playing'+song)
                    

            elif 'date' in command:
                date=datetime.datetime.now().strftime('%B %d')
                print(date)
                talk(date)

            elif 'time' in command:
                    time =datetime.datetime.now().strftime('%I %M %p')
                    print(time)
                    talk('It is '+time)

            elif 'search for' in command:
                    thing = command.replace('search for','')
                    pywhatkit.search(thing)
                    print('Searching for'+thing)
                    talk('Searching for'+thing) 
                   
            elif 'search' in command:
                    thing = command.replace('search','')
                    pywhatkit.search(thing)
                    print('Searching for'+thing)
                    talk('Searching for'+thing) 
                    
            elif 'day' in command:
                    day=datetime.datetime.now().strftime('%A')
                    print('It is '+day)
                    talk('It is '+day)

            elif 'how are you' in command:
                print('I am fine. How are you doing?')
                talk('I am fine. How are you doing?')

            elif 'bye' in command:
                print('Okay Sai. Hope to see you soon. Have a good day!')
                talk('Okay Sai. Hope to see you soon. Have a good day!')

            

    except:
        pass
    return command

# def runjarvis():
#     command=takecommand()
    # if 'play' in command:
    #     print('Redirecting to youtube')
    #     song=command.replace('play','')
    #     talk('Playing'+song)
    #     pywhatkit.playonyt(song)

    # elif 'time' in command:
    #     time =datetime.datetime.now().strftime('%I %M %p')
    #     talk('It is '+time)

    # elif 'search for' in command:
    #     thing = command.replace('search for','')
    #     talk('Searching for'+thing) 
    #     pywhatkit.search(thing)

    # elif 'search' in command:
    #     thing = command.replace('search','')
    #     talk('Searching for'+thing) 
    #     pywhatkit.search(thing)

    # elif 'day' in command:
    #     day=datetime.datetime.now().strftime('%A')
    #     talk('It is'+day)      
    
    # else:
    #     print("Reinitialize Jarvis")

while True:
    takecommand()

