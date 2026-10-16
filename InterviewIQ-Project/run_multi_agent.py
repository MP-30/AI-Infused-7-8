# run_multi_agent.py -- Ask 4 (optional bonus): the orchestrator
# ============================================================
#  InterviewIQ -- Two-Agent Mock Interview (CLI)
#  A small orchestrator that coordinates two specialized agents:
#    - Interviewer (interview_agent.py): picks the NEXT question's
#      category ("behavioral" or "technical") from the report so far.
#    - Evaluator   (agent.py): scores each answer with the tools and
#      gives feedback, recording it into session memory.
#  Run:  python run_multi_agent.py
# ============================================================

from interview_bank import QUESTIONS
from agent import run_turn, ask_for_final_report, session_log
from interview_agent import choose_next_category


def pick_question(category, remaining):
    """First unasked question in `category`, or any unasked one if that category is used up."""
    for q in remaining:
        if q["category"] == category:
            return q
    return remaining[0]


def main():
    print("=== InterviewIQ -- Two-Agent Mock Interview ===\n")
    remaining = list(QUESTIONS)

    while remaining:
        summary = ask_for_final_report() if session_log else ""
        category = choose_next_category(summary)
        q = pick_question(category, remaining)
        remaining.remove(q)

        print(f"[Interviewer chose: {category}]")
        print(f"Q: {q['question']}")
        answer = input("Your answer: ")
        feedback = run_turn(q["question"], answer, q["expected_keywords"])
        print(f"\nCoach: {feedback}\n")
        print("-" * 60)

    print("\n=== Final Report ===")
    print(ask_for_final_report())


if __name__ == "__main__":
    main()
