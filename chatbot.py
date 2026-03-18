#Chat Bot
import speech_recognition as sr
import webbrowser
import time
import pyttsx3

def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("System is Listening....")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        return command.lower()
    except:
        return ""

def speek(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(text)
    engine.runAndWait()
    print("Done")
print("Sytem: Hello, I am your Chat Bot, how can i help you")
while True:
    x = take_command()
    if x == "":
        print("Can not able to recognize, come Again")
        speek("Can not able to recognize, come Again")
    else:
        x = x.lower()
        print(x)
    
        if "hello" in x:
            print("System: Hello, How are you")
            speek("Hello, How are you")
        elif "how are you" in x:
            print("System: I am doing Good")
            speek("I am doing Good")
        elif "bye" in x:
            print("System: Good bye, Take Care")
            speek("Good bye, Take Care")
            break
        elif "name" in x:
            print("System: I am Your Virtual Assistant")
            speek("I am Your Virtual Assistant")
        elif "you tube" in x:
            print("System: Opening You tube")
            speek("Opening You tube")
            time.sleep(1)
            webbrowser.open("https://www.youtube.com/")
        elif "instagram" in x:
            print("System: Opening Instagram")
            speek("Opening Instagram")
            time.sleep(1)
            webbrowser.open("https://www.instagram.com/")
        else:
            print("System: I can't get you, come Again")
            speek("I can't get you, come Again")
                







