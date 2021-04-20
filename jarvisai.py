import pyttsx3
import datetime
import speech_recognition as sr
# import pyaudio
import wikipedia
import webbrowser
import os
import wolframalpha
import folderify

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("Good Morning!")

    elif hour >=12 and hour <18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hello I am Jarvis sir, please tell me how may I help you?")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.record(source, duration=4)

    try:
        print("Recognizing...")
        speak("Recognizing...")
        # print("User said:")
        # speak("User said")
        query = r.recognize_google(audio, language='en-us')
        print(query)

    except Exception as e:
        print(e)
        print("Say that again please...")
        speak("Sir, Say that again please...")
        return 'None'
    return query



if __name__ == "__main__":
    WishMe()
    # takeCommand()
    # "How can i help you today?"

while True:
    query = takeCommand().lower()

    if 'wikipedia' in query:
        speak("Searching for WikiPedia...")
        query = query.replace("wikipedia", "")
        answer = wikipedia.summary(query, sentences=2)
        print("According to WikiPedia:")
        speak("According to WikiPedia")
        print(answer)
        speak(answer)

    elif'open youtube' in query:
        browser_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s "
        url = "https://www.youtube.com"
        webbrowser.get(browser_path).open(url)
        True
        break 

    elif'open google' in query:
        googlePath = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe")
        os.startfile(googlePath)
        break

    elif'open photos' in query:
        photo_path = ("C:/Dell/jarvis/Photos.exe.lnk")
        os.startfile(photo_path)
        break    

    elif'open file explorer' in query:
        folder_path = ("C:/Windows/explorer.exe")
        os.startfile(folder_path)
        break

    elif'open spotify' in query:
        music_path = ("C:/Users/shing/AppData/Roaming/Spotify/Spotify.exe")
        os.startfile(music_path)
        break

    # else:
    #     print("I'm going to sleep...")
    #     speak("I'm going to sleep...")
    #     break

    
    
        # chrome('chrome')
# def speak(audio)
#     speak("Recignizing...")

