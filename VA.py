import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty("voices")

engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 200)

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
speak("Hello World!")