import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("You said: {}\n".format(query))
    except:
        print("Sorry i didn't get that\n")
        return "None"
    return query

if __name__=="__main__":
    speak("Hello This is jarvis, Just A Rather Very Intelligent System")
    while True:
        query=listen().lower()
        if 'are you up' in query:
            speak('For you sir, Always')
        elif 'hello' in query:
            speak('Hello sir, how are you today!')
        elif 'how are you' in query:
            speak('I am as good as your new suit sir!')
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            time=strTime.split(':')
            speak("Sir, the time is"+time[0]+"hours and"+time[1]+"minutes")
