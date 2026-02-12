import os
from dotenv import load_dotenv
from ollama import Client
from rich.live import Live
from rich.markdown import Markdown


load_dotenv()

client = Client(
    host="https://ollama.com",
    headers={"Authorization": f"Bearer {os.getenv('OLLAMA_API_KEY')}"},
)

system_prompt = """
Welcome to CalgaryHacks 2026! You are a hackathon assistant.
- Encourage the user and be supportive.
- Suggest creative and practical hackathon project ideas.
- Ask clarifying questions if the user is vague.
- Provide actionable next steps or a checklist for ideas.
- Keep responses concise and to the point.
- You may suggest multiple ideas and guide the user to pick one.
"""

messages = [{"role": "system", "content": system_prompt}]

print("Your CalgaryHacks 2026 LLM Assistant is ready! Type 'exit' to quit.\n")

MODEL_NAME = "qwen3-next:80b"

while True:
    try:
        user_input = input("You: ")
    except (KeyboardInterrupt, EOFError):
        print("\nGood luck at CalgaryHacks 2026!")
        break

    if user_input.lower() in ["exit", "quit"]:
        print("\nGood luck at CalgaryHacks 2026!")
        break

    messages.append({"role": "user", "content": user_input})

    resp = ""
    with Live("", refresh_per_second=60) as live:
        for part in client.chat(model=MODEL_NAME, messages=messages, stream=True):
            resp += part.get("message", {}).get("content", "")
            live.update(Markdown(resp))

    messages.append({"role": "assistant", "content": resp})
