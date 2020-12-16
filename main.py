import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
newVoiceRate = 150
engine.setProperty('rate',newVoiceRate)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def giving_command():
    try: 
        with sr.Microphone() as source:
            print("listening.....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "alexa" in command:
                command = command.replace('alexa')
                print(command)            
    except:
        pass
    
    return command

def taking_command():
    command = giving_command()
    song = command.replace('can you play', '')
    if 'can you play' in command:
        talk('playing' + song)
        print('playing' + song)
        pywhatkit.playonyt(song)

    elif "time" in command:
                time = datetime.datetime.now().strftime('%H:%M')
                print(time)
                talk("the current time is" + time)
    
    elif "who is" in command:
        person = command.replace("who is", '')
        info = wikipedia.summary(person, 1)
        talk(info)
        print(info)

    elif "date" in command:
        talk(" in just 2 mins i wil be ready.")

    elif "marry" in command:
        talk("I am all yours from the second i met you")

    elif "parents" in command:
        talk("they are my parents too, you don't need to worry about it")

    elif "date" in command:
        talk(" in just 2 mins i wil be ready.")

    elif "my name" in command:
        talk("Your name is Jitesh Bhojwani, my virtual owner")

    elif "thank you" in command:
        talk("Your welcome")
    
    else:
        talk("sorry i didnt hear that properly, come again")


while True:
    taking_command()
