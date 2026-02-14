import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama

load_dotenv()

"""
Set to "cloud" to use Ollama Cloud
or
Set to "local" to use Ollama locally
"""
BACKEND = "local"

user_prompt = "What model are you?"

messages = [
    {"role": "user", "content": user_prompt},
]

if BACKEND == "cloud":
    MODEL = "gemini-3-flash-preview"
    llm = ChatOllama(
        model=MODEL,
        base_url="https://ollama.com",
        client_kwargs={
            "headers": {"Authorization": f"Bearer {os.getenv('OLLAMA_API_KEY')}"}
        },
    )
elif BACKEND == "local":
    MODEL = "granite4:350m"
    llm = ChatOllama(model=MODEL, base_url="http://localhost:11434")
else:
    raise ValueError("BACKEND must be 'cloud' or 'local'.")

print(f"Backend: {BACKEND} | Model: {MODEL}")

response = ""
for chunk in llm.stream(messages):
    text = chunk.content or ""
    response += text
    print(text, end="", flush=True)
