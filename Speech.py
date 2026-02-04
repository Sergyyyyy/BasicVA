from vosk import Model, KaldiRecognizer
import sounddevice as sd
import json

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

