# Hangman Game
import random

word_list = ['robber', 'karma', 'aardvark']

# Generate a random word
word = random.choice(word_list)

# Generatte as many blanks as letters in the word
hangman = []
for letter in word:
    hangman.append("_")

remaining_guesses = 5

while remaining_guesses > 0:
    # Guess a letter
    user_guess = input("What letter would you like to guess?\n")
    # Is guess in word
    if user_guess.lower() in word:
        # Replace blank with letter
        for i, l in enumerate(word):
            if l == user_guess:
                hangman[i] = l
        print(f"You're right! The word has that letter: {hangman}\n")
        if "_" not in hangman:
            print(f"You've got it! The word was {word}")
            break
    else:
        remaining_guesses -= 1
        if remaining_guesses == 0:
            print(f"Better luck next time! The word was {word}")
        print(f"That letter isn't present! You have {remaining_guesses} left! ")
        