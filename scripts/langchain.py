import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI

load_dotenv()

# "ollama_local" or "ollama_cloud" or "openai"
BACKEND = "ollama_local"

user_prompt = "What model are you?"

messages = [
    {"role": "user", "content": user_prompt},
]

if BACKEND == "ollama_cloud":
    MODEL = "gemini-3-flash-preview"
    llm = ChatOllama(
        model=MODEL,
        base_url="https://ollama.com",
        client_kwargs={
            "headers": {"Authorization": f"Bearer {os.getenv('OLLAMA_API_KEY')}"}
        },
    )
elif BACKEND == "ollama_local":
    MODEL = "granite4:350m"
    llm = ChatOllama(model=MODEL, base_url="http://localhost:11434")
elif BACKEND == "openai":
    MODEL = "gpt-5-mini"
    llm = ChatOpenAI(
        model=MODEL,
        api_key=os.getenv("OPENAI_API_KEY"),
    )
else:
    raise ValueError("BACKEND must be 'ollama_cloud', 'ollama_local', or 'openai'.")

print(f"Backend: {BACKEND} | Model: {MODEL}")

response = ""
for chunk in llm.stream(messages):
    text = chunk.content or ""
    response += text
    print(text, end="", flush=True)
