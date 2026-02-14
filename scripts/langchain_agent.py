import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two integers."""
    return a * b


@tool
def project_name_idea(theme: str) -> str:
    """Return one short hackathon project name idea for a given theme."""
    return f"{theme.title()} Hackathon"


def get_llm(backend: str):
    if backend == "ollama_cloud":
        model = "qwen3-next:80b"
        llm = ChatOllama(
            model=model,
            base_url="https://ollama.com",
            client_kwargs={
                "headers": {"Authorization": f"Bearer {os.getenv('OLLAMA_API_KEY')}"}
            },
        )
    elif backend == "ollama_local":
        model = "granite4:latest"  # or granite4:350m
        llm = ChatOllama(model=model, base_url="http://localhost:11434")
    elif backend == "openai":
        model = "gpt-5-mini"
        llm = ChatOpenAI(model=model, api_key=os.getenv("OPENAI_API_KEY"))
    else:
        raise ValueError("BACKEND must be 'ollama_cloud', 'ollama_local', or 'openai'.")
    return llm, model


def main() -> None:
    load_dotenv()

    BACKEND = "ollama_cloud"

    llm, model = get_llm(BACKEND)

    agent = create_agent(
        model=llm,
        tools=[multiply, project_name_idea],
        system_prompt="You are a helpful hackathon assistant. Use tools when useful.",
    )

    print(f"Backend: {BACKEND} | Model: {model}")

    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Use tools: multiply 17 and 23, then suggest one project name for theme 'innovation'.",
                }
            ]
        }
    )

    final_message = result["messages"][-1]
    print(final_message.content)


if __name__ == "__main__":
    main()
