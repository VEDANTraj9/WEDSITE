import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') #print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning vedant!")
    elif 12 <= hour < 18:
        speak("Good afternoon vedant!")
    else:
        speak("Good evening vedant!")

    speak("I am Zara. How may I help you?")


def takecommand(): #it take microphone to the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again, please...")
        return "None"
    return query


if __name__ == "__main__":
    wishme()
    while True: # (this loop will executing infinite time.)
           #if 1: (this command execute the code only once and stop)

        query = takecommand().lower()

         #logic for executing task based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open chatgpt' in query:
            webbrowser.open("chatgpt.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\vedan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'play music' in query:
            music_dir = 'C:\\Users\\vedan\\Music'
            songs = os.listdir(music_dir)
            if songs:
                random.shuffle(songs)
                os.startfile(os.path.join(music_dir, songs[0]))
            
            elif 'python teacher' in query:
                print("Thank you for being such an inspiring and patient sir.Your clear explanations and guidance have made learning Python a truly enjoyable experience.")

            speak('Thank you for being such an inspiring and patient sir.')

            speak('Your clear explanations and guidance have made learning Python a truly enjoyable experience.')

        elif 'ramesh' in query:
            print("Thank you for being such an inspiring and patient sir.Your clear explanations and guidance have made learning Python a truly enjoyable experience.")

            speak('Thank you for being such an inspiring and patient sir.')
            speak('Your clear explanations and guidance have made learning Python a truly enjoyable experience.')

        elif 'friend' in query:
            speak('laura , behanchod ')
            speak(' gand marwaye bhonsdiwala')
        elif 'kaushki and harsh' in query:
            speak('aap dono ki joori number one hai')
        elif 'aman' in query:
            speak('aapka dost aman ')
            speak('rishabh louru lalit hai')
        elif 'thank you' in query:
            speak("You're welcome!")

        elif 'stop' in query:
            speak("Goodbye!")
            exit()
