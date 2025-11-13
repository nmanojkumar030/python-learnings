from dataclasses import dataclass


@dataclass
class Question:
    text: str
    correct_answer: str
    options: list[str]


def get_questions() -> list[Question]:
    questions: list[Question] = [
        Question(
            text="What is the capital of France?",
            correct_answer="paris",
            options=["Paris", "London", "Berlin", "Madrid"],
        ),
        Question(
            text="What is the capital of Germany?",
            correct_answer="berlin",
            options=["Paris", "London", "Berlin", "Madrid"],
        ),
        Question(
            text="What is the capital of Italy?",
            correct_answer="rome",
            options=["Paris", "London", "Berlin", "Rome"],
        ),
        Question(
            text="What is the capital of Spain?",
            correct_answer="madrid",
            options=["Paris", "London", "Berlin", "Madrid"],
        ),
        Question(
            text="What is the capital of Portugal?",
            correct_answer="lisbon",
            options=["Paris", "London", "Berlin", "Lisbon"],
        ),
        Question(
            text="What is the capital of Greece?",
            correct_answer="athens",
            options=["Paris", "London", "Berlin", "Athens"],
        ),
        Question(
            text="What is the capital of Turkey?",
            correct_answer="ankara",
            options=["Paris", "London", "Berlin", "Ankara"],
        ),
        Question(
            text="What is the capital of Egypt?",
            correct_answer="cairo",
            options=["Paris", "London", "Berlin", "Cairo"],
        ),
        Question(
            text="What is the capital of Saudi Arabia?",
            correct_answer="riyadh",
            options=["Paris", "London", "Berlin", "Riyadh"],
        ),
        Question(
            text="What is the capital of UAE?",
            correct_answer="abu dhabi",
            options=["Paris", "London", "Berlin", "Abu Dhabi"],
        ),
        Question(
            text="What is the capital of Qatar?",
            correct_answer="doha",
            options=["Paris", "London", "Berlin", "Doha"],
        ),
    ]
    return questions


def play_quiz(questions: list[Question]) -> int:
    total_score: int = 0
    for question in questions:
        print(question.text)

        for option in question.options:
            print(f"- {option}")

        user_answer: str = input(f"Enter your answer: ")

        if user_answer.lower() == question.correct_answer:
            print("Correct!")
            total_score += 1
        else:
            print(f"Incorrect! The correct answer is {question.correct_answer}.")
    return total_score


if __name__ == "__main__":
    questions: list[Question] = get_questions()
    total_score: int = play_quiz(questions)
    print(f"Your total score is {total_score} out of {len(questions)}.")
