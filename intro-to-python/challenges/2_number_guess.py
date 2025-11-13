"""
Number guessing game
The number to guess will be from 1 to 20 (inclusive).
The user will have 4 guesses to guess the number correctly.
After each wrong guess, the user will be told whether to
guess higher or lower next time.
If the user doesn't win, tell them the number.
"""
import random


def run_game():
    print("I'm thinking of a number between 1 and 20")
    answer: int = random.randint(1, 20)

    num_of_guesses: int = 4
    while num_of_guesses > 0:
        guess: int = int(input("Guess a number: "))
        if guess == answer:
            print("Correct guess")
            return
        elif guess > answer:
            print("Guess lower")
        else:
            print("Guess higher")

        num_of_guesses -= 1
        
    print(f"Nope! It was {answer}")
run_game()
