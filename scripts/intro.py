import os
from dotenv import load_dotenv
from ollama import Client

load_dotenv()

client = Client(
    host="https://ollama.com",
    headers={"Authorization": f"Bearer {os.getenv('OLLAMA_API_KEY')}"},
)

system_prompt = "Welcome to CalgaryHacks 2026! Encourage the user with their hackathon and provide them with great ideas"

user_prompt = "Can you suggest a great hackathon idea to impress the judges?"

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt},
]

response = ""
MODEL = "qwen3-next:80b"
for chunk in client.chat(model=MODEL, messages=messages, stream=True):
    text = chunk["message"]["content"]
    response += text
    print(text, end="", flush=True)
