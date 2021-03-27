import pyttsx3
import speech_recognition as sr
import time
import pyautogui as pg


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    '''
#it take microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold=0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")
    
    except Exception as e:
        #print(e)
        print("Say that again")
        return "None"'''
    return input()

if __name__ == "__main__":
    speak('before further proceed make sure that your browser will appear as full screen. do you want to continue? reply as yes or no')
    query=takeCommand().lower()
    if 'no' in query:
        quit()
    speak ("which song") 
    while True:
        query = takeCommand().lower()

        if 'song' in query:
            speak("playing sir")
            query=query.replace("song",'')
            song=query
            pg.press("win")
            time.sleep(0.5)
            pg.write('chrome',interval=0.05)
            pg.press("enter")
            time.sleep(2)
            pg.click(x=347,y=60)
            pg.press("backspace")
            pg.write("www.youtube.com",interval=0.05)
            pg.press("enter")
            time.sleep(5)
            pg.click(x=578,y=125)
            pg.write(song,interval=0.1)
            pg.press("enter")
            pg.sleep(5)
            pg.click(x=1092,y=257)
            quit()

        else:
            speak("playing sir")
            song=query
            pg.press("win")
            time.sleep(0.5)
            pg.write('chrome',interval=0.05)
            pg.press("enter")
            time.sleep(2)
            pg.click(x=347,y=60)
            pg.press("backspace")
            pg.write("www.youtube.com",interval=0.05)
            pg.press("enter")
            time.sleep(5)
            pg.click(x=578,y=125)
            pg.write(song,interval=0.1)
            pg.press("enter")
            pg.sleep(5)
            pg.click(x=1092,y=257)
            quit()