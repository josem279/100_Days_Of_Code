# Namespaces and scope + Number Guessing Game Project
import random
import sys

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0

def choose_difficulty():
    difficulty= input("Choose a difficulty. Type 'easy' or 'hard':\n")
    if difficulty == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def make_guess(guess, answer, turns):
    """Checks answer against guess and returns the number of guesses remaining if not correct."""
    if guess > answer:
        print("Too high. Guess again!")
        turns -= 1
        return turns
    elif guess < answer:
        print("Too low. Guess again!")
        turns -= 1
        return turns
    else:
        print(f"That's right! The correct number is {answer}, you win!")


def game():
    print("Welcome to the Number Guessing Game!\n I'm thinking of a number between 1 and 100.")

    answer = random.randint(1, 100)
    turns = choose_difficulty()

    guess = 0 

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess:\n"))
        turns = make_guess(guess, answer, turns)

        if turns == 0:
            print(f"The number was {answer}! You lose! Better luck next time.")

game()