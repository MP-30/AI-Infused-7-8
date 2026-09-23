import os
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

load_dotenv(find_dotenv(), override=True)

PROVIDER = "groq"   # "groq" (free) or "openai"

if PROVIDER == "groq":
    MODEL = "openai/gpt-oss-20b"
    client = OpenAI(api_key=os.getenv("GROQ_API_KEY"), base_url="https://api.groq.com/openai/v1")
else:
    MODEL = "gpt-4o-mini"
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """You are the Interviewer half of InterviewIQ's two-agent mock interview system.
Your only job: decide whether the NEXT question should be "behavioral" or "technical",
based on how the candidate has done so far.
Rule of thumb: after a weak answer, consider staying in the same category so the
candidate can try again; after a strong answer, feel free to switch categories to
test breadth. Respond with exactly one word: behavioral or technical."""


def choose_next_category(session_summary: str) -> str:
    """Ask the Interviewer agent to pick the next question's category.

    `session_summary` is a short plain-English recap of performance so far
    (e.g. agent.generate_final_report()'s output) -- pass "" for the very
    first question of the session.
    """
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": session_summary or "This is the first question of the session. Pick a category to start with."},
    ]
    response = client.chat.completions.create(model=MODEL, messages=messages)
    choice = response.choices[0].message.content.strip().lower()
    return "technical" if "technical" in choice else "behavioral"
