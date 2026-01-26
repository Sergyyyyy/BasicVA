from VA import speak
import creds

from groq import Groq

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
speak(completion.choices[0].message.content)

# for chunk in completion:
#     print(chunk.choices[0].delta.content or "", end="")