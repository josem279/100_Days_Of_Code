# Day 13 -> Debugging and how find bugs ---- NO CODE Challenge
# Day 14
########### Higher/Lower Game

import Day14_Helpers as h
import random

data = h.data

def make_rand_selection():
    return data[random.randint(1, len(data))]

def guess(choice1, choice2, total_correct):

    print(f"Compare A: {choice1['name']}, a {choice1['description']}, from {choice1['country']}.")
    print(h.vs)
    print(f"Against B: {choice2['name']}, a {choice2['description']}, from {choice2['country']}.")

    user_choice = input("Pick 'A' or 'B':\n").lower()

    if user_choice == 'a':
        if choice1['follower_count'] > choice2['follower_count']:
            print(f"You're right! Current score: {total_correct + 1}")
            return True
        else:
            print(f"Sorry, that's wrong. Total correct: {total_correct}")
            return False
    elif user_choice == 'b':
        if choice2['follower_count'] > choice1['follower_count']:
            print(f"You're right! Current score: {total_correct + 1}")
            return True
        else:
            print(f"Sorry that's wrong. Final Score: {total_correct}")
            return False


def game():
    correct = True
    total_correct = 0

    while correct:
        choice1 = make_rand_selection()
        choice2 = make_rand_selection()

        while choice1 == choice2:
            choice2 = make_rand_selection()

        correct = guess(choice1, choice2, total_correct)
        total_correct += 1
    
game()