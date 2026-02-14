# CalgaryHacks 2026 IBM Workshop

This hands-on workshop explores how to build Agentic AI workflows with a focus on using IBM’s Open Source Large Language Models.

Through practical demos, we’ll showcase how IBM Granite 4 models running via Ollama can be used to build agentic workflows to support your hackathon projects.

We’ll also explore how to extend these workflows with cloud-hosted models, including Ollama Cloud offerings and OpenAI GPT models, to enable various approaches.

## What You Will Run

This repo contains the following Python-based demos:

1. `1_intro.py` - An initial look at using using Ollama Cloud.
2. `2_stream.py` - A demo of an interactive terminal chat
3. `3_langchain_chat.py` - A LangChain chat with swappable backends (`ollama_cloud`, `ollama_local`, or `openai`)
4. `4_langchain_agent.py` - A LangChain tool-calling agent demo
5. `5_agentic_project_analyzer.py` - A multi-agent analyzer, planner, and judging pipeline that goes through your project files and creates a report to help you prioritize tasks for the hackathon

## Prerequisites

- Git
- Python `3.11+`
- `uv` package manager
- Ollama setup:
  - Local Ollama server (`http://localhost:11434`)
  - Granite model available locally (for example `granite4:latest` or `granite4:350m`)
- Ollama Cloud API key for cloud-backed scripts
- Optional: OpenAI API key for OpenAI backend demos (USD$ 5 required)

## Setup

### 1. Clone

```bash
git clone https://github.com/s-sajid/calgaryhacks2026-ibm-workshop
cd calgaryhacks2026-ibm-workshop
```

### 2. Install `uv`

Windows (PowerShell):

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

macOS/Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Full install instructions: [uv installation docs](https://docs.astral.sh/uv/getting-started/installation/)

### 3. Install dependencies

```bash
uv sync
```

### 4. Configure environment variables

Create `.env`:

Windows (PowerShell):

```powershell
Copy-Item .env.example .env
```

macOS/Linux:

```bash
cp .env.example .env
```

Set values:

```env
OLLAMA_API_KEY=your_ollama_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

Notes:

- `OLLAMA_API_KEY` is needed for cloud scripts.
- `OPENAI_API_KEY` is only needed if you switch scripts to `BACKEND="openai"`.

Model options: [Ollama Library](https://ollama.com/library)

## Run Demos

Run each script from repo root:

```bash
uv run scripts/1_intro.py
uv run scripts/2_stream.py
uv run scripts/3_langchain_chat.py
uv run scripts/4_langchain_agent.py
uv run scripts/5_agentic_project_analyzer.py
```

## Demo Guide

### `1_intro.py`

- Uses `ollama.Client` against `https://ollama.com`.
- Sends one prompt and streams model output token-by-token.

### `2_stream.py`

- Interactive terminal assistant with message history.
- Includes commented cloud configuration if you want to switch to an Ollama Cloud model

### `3_langchain_chat.py`

- Basic LangChain chat streaming example.
- Backend selected by `BACKEND` constant:
  - `ollama_local` (default in file)
  - `ollama_cloud`
  - `openai`

### `4_langchain_agent.py`

- Builds a tool-calling agent with two tools:
  - `multiply(a, b)`
  - `project_name_idea(theme)`
- Defaults to `ollama_local` with Granite.
- Runs one prompt that asks the agent to use both tools.

### `5_agentic_project_analyzer.py`

- Runs a three-stage workflow over `scripts/example-project`:
  - `AnalyzerAgent` (repo analysis + time budget)
  - `PlannerAgent` (execution plan)
  - `JudgeAgent` (hackathon scoring/feedback)
- Writes final markdown report to `scripts/output/analyzer_output.md`.

## `scripts/output` Notes

There are no executable scripts in `scripts/output`; this folder stores generated markdown reports.

- `scripts/output/demo_output.md`: committed sample report output for reference.
- `scripts/output/analyzer_output.md`: generated when you run the `5_agentic_project_analyzer.py` file.

## Troubleshooting

- `Missing OLLAMA_API_KEY`: set it in `.env` for cloud scripts.
- `Connection refused http://localhost:11434`: start local Ollama before local scripts.
- `Model not found`: change model names in scripts to models available in your Ollama account/runtime.
- `uv: command not found`: reopen terminal after installing `uv`.
