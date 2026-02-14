import os

from dotenv import load_dotenv
from ollama import Client

load_dotenv()

# Ollama Local
MODEL = "granite4:latest" # or granite4:350m

client = Client()

# # Ollama Cloud
# MODEL = "glm-5"

# client = Client(
#     host="https://ollama.com",
#     headers={"Authorization": f"Bearer {os.getenv('OLLAMA_API_KEY')}"},
# )

print("Terminal chat started. Type 'exit' or 'quit' to stop.\n")
print("Welcome to CalgaryHacks 2026! I'm your personal LLM assistant!")

system_prompt = "Welcome to CalgaryHacks 2026! Encourage the user and provide them with a winning hackathon idea."

messages = [
    {
        "role": "system",
        "content": system_prompt,
    }
]

try:
    while True:
        user_prompt = input("> You: ").strip()
        if not user_prompt:
            continue
        if user_prompt.lower() in {"exit", "quit"}:
            print(f"> Assistant ({MODEL}): Goodbye.")
            break

        messages.append({"role": "user", "content": user_prompt})

        print(f"> Assistant ({MODEL}): Your Hackathon Assistant is thinking...")
        print(f"> Assistant ({MODEL}): ", end="", flush=True)

        response = ""
        for chunk in client.chat(model=MODEL, messages=messages, stream=True):
            text = chunk["message"]["content"]
            response += text
            print(text, end="", flush=True)
        print()

        messages.append({"role": "assistant", "content": response})
except KeyboardInterrupt:
    print(f"\n> Assistant ({MODEL}): Goodbye.")
