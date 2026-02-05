# References for API
import creds
from groq import Groq

# References for Speech Recognition
from vosk import Model, KaldiRecognizer
import sounddevice as sd
import json

# References for Speak functionality
import pyttsx3






# Comp Speak functionality

engine = pyttsx3.init()

voices = engine.getProperty("voices")

engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 200)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# AI API capability

client = Groq(api_key = creds.API_Key)

def artificialize(input):
    summarize = "summarize in a sentence."

    completion = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {"role": "user", "content": f"{input} {summarize}"}
        ],
        stream=False
    )
    print(completion.choices[0].message.content)
    speak(completion.choices[0].message.content)



# Speech capability
yourVoiceText = ""


model = Model("Python/BasicVA/BasicVA/vosk-model-small-en-us-0.15")
rec = KaldiRecognizer(model, 16000)

def callback(indata, _frames, _time, 
             status):
    global yourVoiceText
    
    if status:
        print(status)

    if rec.AcceptWaveform(bytes(indata)):
        result = json.loads(rec.Result())
        
        yourVoiceText = result["text"]
        print("You said:", yourVoiceText)



with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                       channels=1, callback=callback):
    print("Listening...")
    input()
    
if yourVoiceText:
    artificialize(yourVoiceText)
else:
    speak("I didn't hear anything.")


# Integrated Version

callback()
artificialize(yourVoiceText)
