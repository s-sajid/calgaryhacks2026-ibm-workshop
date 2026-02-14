import os
from dotenv import load_dotenv
from ollama import Client

load_dotenv()

client = Client(
    host="https://ollama.com",
    headers={"Authorization": f"Bearer {os.getenv('OLLAMA_API_KEY')}"},
)

user_prompt = "Give me a fun fact about the University of Calgary in one line"

messages = [
    {"role": "user", "content": user_prompt},
]

response = ""
MODEL = "qwen3-next:80b"
for chunk in client.chat(model=MODEL, messages=messages, stream=True):
    text = chunk["message"]["content"]
    response += text
    print(text, end="", flush=True)
