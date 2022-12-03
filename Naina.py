import pyttsx3
import speech_recognition as sr
import datetime as dt
import wikipedia
import webbrowser
import os
import smtplib
import random

print("Initializing Naina....")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(dt.datetime.now().hour)

    if hour >= 0 and hour < 12:
        print("Good Morning..Saurabh!!")
        speak("Good Morning..Saurabh!!")
    elif hour >= 12 and hour < 15:
        print("Good Afternoon..Saurabh!!")
        speak("Good Afternoon..Saurabh!!")
    elif hour >= 15 and hour < 20:
        print("Good Evening..Saurabh!!")
        speak("Good Evening..Saurabh!!")
    else:
        print("Good Night..Saurabh!!")
        speak("Good Night..Saurabh!!")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print("Recogninzing...")
        speak("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        print("Sorry,can you please say it again")
        speak("Sorry,can you please say it again")
        return "None"
    return query

def game():
    def GameWin(comp,you):
        if comp==you:
            return None
        elif comp=="snake":
            if you=="water":
                return False
            elif you=="gun":
                return True
        elif comp=="water":
            if you=="snake":
                return True
            elif you=="gun":
                return False
        elif comp=="gun":
            if you=="water":
                return True
            elif you=="snake":
                return False

    print("Computer turn: S(Snake)  W(Water)  G(Gun)")
    
    Choose=random.randint(1,3)
    if Choose==1:
        comp="snake"
    elif Choose==2:
        comp="water"
    elif Choose==3:
        comp="gun"

    speak("My turn first and I choosed what I wanted to.And Now it's your turn to choose...")
    you=takecommand().lower()
    a=GameWin(comp,you)

    print(f"Computer choose {comp}")
    speak(f"Computer choose {comp}")
    print(f"You choose {you}")
    speak(f"You choose {you}")

    if a==None:
        print("The game is a tie!!!")
        speak("The game is a tie!!!")
    elif a:
        print("You win!!!!")
        speak("You win!!!!")
    else:
        print("You lost!!!!")
        speak("You lost!!!")

speak("Initializing Naaina....")

if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()

        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "youtube" in query:
            speak("Searching...")
            query=query.replace("youtube","")
            url = "youtube.com"
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif "google" in query:
            speak("Searching...")
            query=query.replace("google","")
            url = "google.com"
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif "hotstar" in query:
            speak("Searching...")
            query=query.replace("hotstar","")
            url = "hotstar.com"
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif "play music" in query:
            songs_dir = "D:\\gaana"
            songs = os.listdir(songs_dir)
            k=len(songs)
            for i in range(1,k):
                print(f"{i} - {songs[i]}")
            speak("In above list which song do you want to play...")
            gaana = takecommand().lower()
            for i in range(1,k):
                if gaana in songs[i].lower():
                    os.startfile(os.path.join(songs_dir, songs[i]))
            speak("Playing music")

        elif "time" in query:
            strtime = dt.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir! the time is {strtime}")

        elif "how are you" in query:
            speak("I am fine!! How are you?")
            talk=takecommand().lower()
            if "I am also fine" in talk:
                speak("That's good to hear!!")
                
        elif "tell me about you" in query:
            speak("I am Naaina. My name is given by my master's mom!!I am very grateful of her for giving me such a cute name. I am a virtual assistant which can do few tasks for you, according to your wish..and that's all because you will know about me more by using me. Thank you!! ")

        elif "let's play a game" in query:
            speak("ok let's play a game then...")
            game()

        elif "exit" in query:
            speak("going to sleep bye... Thanks for using me")
            quit()

