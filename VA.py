import pyttsx3
from Speech import callback

engine = pyttsx3.init()

voices = engine.getProperty("voices")

engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 200)

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
callback()