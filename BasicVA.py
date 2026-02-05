# References for API
import creds
from groq import Groq

# References for Speech Recognition
from vosk import Model, KaldiRecognizer
import sounddevice as sd
import json

# References for Speak functionality
import pyttsx3



# AI API capability

client = Groq(api_key = creds.API_Key)

summarize = "summarize in a sentence."

userQuestion = str(input("-> "))

completion = client.chat.completions.create(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    messages=[
        {"role": "user", "content": f"{userQuestion} {summarize}"}
    ],
    stream=False
)

print(completion.choices[0].message.content)


# Speech capability

model = Model("Python/BasicVA/BasicVA/vosk-model-small-en-us-0.15")
rec = KaldiRecognizer(model, 16000)

def callback(indata, frames, time, status):
    if status:
        print(status)

    if rec.AcceptWaveform(bytes(indata)):
        result = json.loads(rec.Result())
        print("You said:", result["text"])



with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                       channels=1, callback=callback):
    print("Listening...")
    input()
    
    

# Speak functionality

engine = pyttsx3.init()

voices = engine.getProperty("voices")

engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 200)

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
speak("Hello World!")


# Integrated

