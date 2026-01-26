import sounddevice as sd
import json
from vosk import Model, KaldiRecognizer

model = Model("vosk-model-en-us-0.22-lgraph")
recognizer = KaldiRecognizer(model, 16000)

def listen():
    with sd.RawInputStream(
        samplerate=16000,
        blocksize=8000,
        dtype="int16",
        channels=1
    ) as stream:

        print("Listening...")

        while True:
            data, _ = stream.read(4000)

            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                return result.get("text", "")

spoken_text = listen()
print("You said:", spoken_text)
