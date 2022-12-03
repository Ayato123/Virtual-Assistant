import os
import pyttsx3
import speech_recognition as sr
from subprocess import call

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        speak("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        return "None"
    return query

if __name__ == "__main__":
    query=takecommand().lower()
    if "activate" in query:
        call(["python","Naina.py"])

