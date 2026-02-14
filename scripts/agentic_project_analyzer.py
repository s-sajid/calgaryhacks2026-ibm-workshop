from datetime import datetime
from pathlib import Path
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_ollama import ChatOllama

SCRIPT_DIR = Path(__file__).resolve().parent
ANALYZE_REPO_PATH = SCRIPT_DIR / "example-project"
OUTPUT_REPO_PATH = SCRIPT_DIR / "output/analysis_output.md"

HACKATHON_OBJECTIVE = (
    "Build a simple, user-friendly mobile app that helps professors track, "
    "verify, and manage student assignment submissions."
)

END_DATETIME = "2026-02-15T00:00"

MODEL_NAME = "granite4:latest"
OLLAMA_HOST = "http://localhost:11434"

MAX_FILES = 30
MAX_CHARS_PER_FILE = 1500
ALLOWED_EXTS = {".py", ".js", ".ts", ".tsx", ".kt", ".md", ".xml", ".yml", ".yaml"}


def get_hours_left() -> float:
    end = datetime.fromisoformat(END_DATETIME)
    hours = (end - datetime.now()).total_seconds() / 3600
    return round(max(0.0, hours), 2)


@tool
def repo_snapshot(max_files: int = MAX_FILES) -> str:
    """Return a compact text snapshot of the project files and sample content."""
    snippets: list[str] = []
    count = 0

    for path in ANALYZE_REPO_PATH.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() not in ALLOWED_EXTS:
            continue
        rel_path = path.relative_to(ANALYZE_REPO_PATH)
        try:
            content = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        snippets.append(f"### FILE: {rel_path}\n{content[:MAX_CHARS_PER_FILE]}")
        count += 1
        if count >= max_files:
            break

    if not snippets:
        return f"No readable files found in: {ANALYZE_REPO_PATH}"

    return "\n\n".join(snippets)


@tool
def time_budget_hours() -> float:
    """Return the remaining hackathon hours until the configured deadline."""
    return get_hours_left()


def extract_final_text(result: dict) -> str:
    message = result["messages"][-1]
    content = getattr(message, "content", "")
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts: list[str] = []
        for item in content:
            if isinstance(item, dict):
                text = item.get("text")
                if text:
                    parts.append(text)
        return "\n".join(parts).strip()
    return str(content)


def run_agent(agent, prompt: str) -> str:
    result = agent.invoke({"messages": [{"role": "user", "content": prompt}]})
    return extract_final_text(result).strip()


def main() -> None:
    llm = ChatOllama(model=MODEL_NAME, base_url=OLLAMA_HOST)
    analyzer = create_agent(
        model=llm,
        tools=[repo_snapshot, time_budget_hours],
        system_prompt=(
            "You are AnalyzerAgent for a student hackathon. "
            "Use tools when needed and return concise markdown analysis."
        ),
    )

    planner = create_agent(
        model=llm,
        tools=[],
        system_prompt=(
            "You are PlannerAgent. Turn analysis into a realistic execution plan "
            "for limited hackathon time."
        ),
    )

    judge = create_agent(
        model=llm,
        tools=[],
        system_prompt=(
            "You are JudgeAgent. Provide realistic 1-10 scores and short feedback "
            "for a hackathon project."
        ),
    )

    analysis_prompt = f"""
    Analyze this repository for hackathon readiness.

    Objective:
    {HACKATHON_OBJECTIVE}

    Use tools first:
    1) `time_budget_hours`
    2) `repo_snapshot`

    Return markdown with exactly these sections:
    - Overview
    - Existing Strengths
    - Weaknesses
    """
    analysis_md = run_agent(analyzer, analysis_prompt)

    plan_prompt = f"""
    Create a practical markdown plan from this analysis.

    Objective:
    {HACKATHON_OBJECTIVE}

    Analysis:
    {analysis_md}

    Return markdown with exactly these sections:
    - Top Features to Build
    - 24-Hour Execution Plan
    - Demo Pitch
    - First 3 Tasks
    """
    plan_md = run_agent(planner, plan_prompt)

    judge_prompt = f"""
    Judge this project plan and analysis.

    Objective:
    {HACKATHON_OBJECTIVE}

    Analysis:
    {analysis_md}

    Plan:
    {plan_md}

    Return markdown with exactly these sections:
    - Scores (1-10): Topic Alignment, Innovation, Solution Effectiveness, Technical Challenge, UI/Design
    - Strengths
    - Weaknesses
    - Overall Verdict
    """
    judge_md = run_agent(judge, judge_prompt)

    markdown = (
        "# Hackathon Project Report\n\n"
        "## Analyzer Output\n\n"
        f"{analysis_md}\n\n"
        "## Planner Output\n\n"
        f"{plan_md}\n\n"
        "## Judge Output\n\n"
        f"{judge_md}\n"
    )

    OUTPUT_REPO_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_REPO_PATH.write_text(markdown, encoding="utf-8")
    print(f"Wrote: {OUTPUT_REPO_PATH}")


if __name__ == "__main__":
    main()
