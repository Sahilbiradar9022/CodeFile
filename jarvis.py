import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")  
    speak("I am Jarvis Sir, How may I help you!")   

def takeCommand():
    # It takes microphone input and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Corrected method and parameter
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    loop_count = 0  # Initialize a counter
    while loop_count < 2:  # Limit to two iterations
        query = takeCommand().lower()
        loop_count += 1  # Increment the counter

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            print(results)
        elif 'open youtube' in query:  # Fixed spacing issue for 'open youtube'
            webbrowser.open("youtube.com")  
        elif 'open facebook' in query:  # Fixed spacing issue for 'open youtube'
            webbrowser.open("facebook.com")
        elif 'open amazon' in query:  # Fixed spacing issue for 'open youtube'
            webbrowser.open("amazon.com")
        elif 'play music' in query:  # Fixed spacing issue for 'open youtube'
            webbrowser.open("https://www.youtube.com/watch?v=kJQP7kiw5Fk&list=PL15B1E77BB5708555")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir ,The time is {strTime}")
        

        else:
            speak("I did not understand the command.")
