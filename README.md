# AI-Infused-7-8

## InterviewIQ -- AI Mock Interview Coach

An agent that evaluates mock-interview answers using tool calls (filler words,
STAR structure, keyword relevance), keeps session memory, and produces a report
with your weakest area.

### Setup

1. Install dependencies: `uv sync`
2. Create a `.env` file in the project root with your key:
   ```
   GROQ_API_KEY=your_key_here
   ```
   (To use OpenAI instead, set `PROVIDER = "openai"` in `agent.py` / `interview_agent.py` and add `OPENAI_API_KEY`.)

### Run

From `InterviewIQ-Project/`:

| Command | What it does |
|---|---|
| `uv run python app.py` | Gradio web UI (main interface) |
| `uv run python main.py` | CLI interview over all questions |
| `uv run python run_multi_agent.py` | Two-agent mode: Interviewer picks the next category, Evaluator scores |
| `uv run python memory_check.py` | Scripted check that session memory finds the weakest answer |
