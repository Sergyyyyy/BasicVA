from vosk import Model, KaldiRecognizer
import sounddevice as sd
import json

model = Model("Python/BasicVA/BasicVA/vosk-model-small-en-us-0.15")
rec = KaldiRecognizer(model, 16000)

def callback(indata, frames, time, status):
    if rec.AcceptWaveform(indata):
        print(json.loads(rec.Result()))

with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                       channels=1, callback=callback):
    print("Listening...")
    input()
