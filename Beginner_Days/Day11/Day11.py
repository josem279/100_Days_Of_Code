# Blackjack Capstone Project for Beginner section
import random
import sys
import os

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """takes a list of cards and returns calculated score (sum) of cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, opponent has blackjack :("
    elif u_score == 0:
        return "Win! You have Blackjack :)"
    elif u_score > 21:
        return "You went over, you lose :("
    elif c_score > 21:
        return "Opponent went over, you win! :)"
    elif u_score > c_score:
        return "You win! :)"
    else:
        return "You lose :("

def play_game():
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    is_game_over = False

    for n in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass.")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

logo = '''
 ___   ___
|A  | |10 |
| ♣ | | ♦ |
|__A| |_10|
'''

while input("Do you want to play a game of Blackjack? Type 'y' or 'n'.") == "y":
    os.system("cls")
    print(logo)
    play_game()