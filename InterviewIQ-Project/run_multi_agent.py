import random
from interview_bank import QUESTIONS
from interviewer_agent import choose_next_category
import agent as evaluator

QUESTIONS_BY_CATEGORY = {}
for q in QUESTIONS:
    QUESTIONS_BY_CATEGORY.setdefault(q["category"], []).append(q)

NUM_TURNS = 3   # keep it short -- this is a bonus demo, not the full bank


def main():
    print("=== InterviewIQ -- Two-Agent Mode (Interviewer + Evaluator) ===\n")
    asked = set()
    summary = ""   # fed to the Interviewer agent each round

    for turn in range(1, NUM_TURNS + 1):
        category = choose_next_category(summary)
        pool = [q for q in QUESTIONS_BY_CATEGORY.get(category, []) if q["question"] not in asked]
        if not pool:
            pool = [q for q in QUESTIONS if q["question"] not in asked]
        if not pool:
            print("Ran out of fresh questions -- ending early.")
            break

        q = random.choice(pool)
        asked.add(q["question"])

        print(f"[Interviewer picked category: {category}]")
        print(f"Q{turn}: {q['question']}")
        answer = input("Your answer: ")
        feedback = evaluator.run_turn(q["question"], answer, q["expected_keywords"])
        print(f"\nCoach: {feedback}\n")
        print("-" * 60)

        summary = evaluator.generate_final_report()   # what the Interviewer sees next round

    print("\n=== Final Report ===")
    print(evaluator.ask_for_final_report())


if __name__ == "__main__":
    main()
