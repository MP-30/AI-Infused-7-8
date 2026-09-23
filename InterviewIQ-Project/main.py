from interview_bank import QUESTIONS
from agent import run_turn, ask_for_final_report


def main():
    print("=== InterviewIQ -- Mock Interview Coach ===\n")
    for q in QUESTIONS:
        print(f"Q: {q['question']}")
        answer = input("Your answer: ")
        feedback = run_turn(q["question"], answer, q["expected_keywords"])
        print(f"\nCoach: {feedback}\n")
        print("-" * 60)

    print("\n=== Final Report ===")
    print(ask_for_final_report())


if __name__ == "__main__":
    main()
