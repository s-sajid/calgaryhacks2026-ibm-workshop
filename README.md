# CalgaryHacks 2026 IBM Workshop

This repo is a hands-on workshop for participants learning how to use LLMs in Python for hackathon-style workflows using Ollama.

The notebooks use open-source cloud models from Ollama, but you can replace them with other models based on your team environment.

For this IBM event, you can also use Granite models. Granite is not always available on Ollama Cloud and may instead be run on dedicated/local hardware.

You will run 2 notebooks:

1. `intro.ipynb`: connect to Ollama Cloud and send prompts.
2. `agentic_project_analyzer.ipynb`: analyze a code repo and generate a structured hackathon plan.

---

## What You Will Build in This Workshop

By the end, you will know how to:

- connect a Python app to `https://ollama.com`
- store secrets safely in a `.env` file
- run notebooks with `uv` + JupyterLab
- use an "agentic" workflow to review a project and produce actionable tasks

---

## Prerequisites

- Git
- Python `3.12+` (this project was developed with `3.12.12`)
- An Ollama account and API key

---

## Setup (Step-by-Step)

### 1. Clone the repository

```bash
git clone https://github.com/s-sajid/calgaryhacks2026-ibm-workshop
cd calgaryhacks2026-ibm-workshop
```

### 2. Install `uv`

`uv` manages environments and dependencies for this workshop.

Windows (PowerShell):

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

macOS:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

After install, confirm:

```bash
uv --version
```

Full install instructions: `https://docs.astral.sh/uv/getting-started/installation/`

### 3. Install project dependencies

From the project root:

```bash
uv sync
```

### 4. Create an Ollama API key

1. Go to `https://ollama.com` and sign in (or create an account).
2. Open API key settings: `https://ollama.com/settings/keys`.
3. Generate a new key and copy it.

### 5. Configure environment variables

Create `.env` from the template:

macOS/Linux:

```bash
cp .env.example .env
```

Windows (PowerShell):

```powershell
Copy-Item .env.example .env
```

Then open `.env` and set:

```env
OLLAMA_API_KEY=your_real_api_key_here
```

---

## Run the Workshop

### Start JupyterLab

```bash
uv run jupyter lab
```

Then open notebooks in this order:

1. `intro.ipynb`
2. `agentic_project_analyzer.ipynb`

Run cells from top to bottom in each notebook.

---

## Notebook Notes

For `agentic_project_analyzer.ipynb`, update these config values before running:

- `ANALYZE_REPO_PATH`: local path to the repo you want to evaluate
- Sample repo to clone and analyze: `https://github.com/yyc-hacks/calgary-accessibility`
- `START_DATETIME` / `END_DATETIME`: your hackathon timeline
- `HACKATHON_OBJECTIVE`: what your team is trying to build

The notebook writes a report file (default: `demo_output.md`) with:

- prioritized tasks
- 24-hour execution plan
- judging snapshot and risks

Model options (Ollama Library): `https://ollama.com/library`

---

## Troubleshooting

- `Missing OLLAMA_API_KEY`: verify `.env` exists and key is set correctly.
- `uv: command not found`: restart terminal after installing `uv`.
- Notebook cannot import packages: run `uv sync` again.
- Kernel issues in Jupyter: choose the project kernel in the top-right of notebook UI.
