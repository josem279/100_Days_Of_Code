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


# ####################################### My own solution
# def get_score(user_hand):
#     score = sum(user_hand)
#     return score
#
# def show_current_hands():
#     print(f"Your cards: {user_hand}, current score: {user_score}")
#     print(f"Computer's first card: {computer_hand[0]}")
#
# def draw_cards(hand):
#     hand.append(random.choice(cards))
#
# def check_for_blackjack(score):
#     if score == 21:
#         print("Blackjack!!")
#     return True
#
# def convert_ace(user_score, user_hand):
#     if user_score > 21:
#         if  11 in user_hand:
#             for i, num in enumerate(user_hand):
#                 if num == 11:
#                     user_hand[i] = 1
#                     break
#             user_score = get_score(user_hand)
#     user_score = get_score(user_hand)
#     if user_score > 21:
#         show_final_hands()
#         print("You went over, you lose! :(")
#         sys.exit()
#     check_for_blackjack(user_score)
#     return user_score, user_hand
#
# def show_final_hands():
#     print(f"Your final hand: {user_hand}, final score: {user_score}")
#     print(f"Computers final hand: {computer_hand}")
#
#
# logo = '''
#  ___   ___
# |A  | |10 |
# | ♣ | | ♦ |
# |__A| |_10|
# '''
#
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#
# user_cards = []
# computer_cards = []
#
# play_y_n = input("Do you want to play a game of blackjack? Type 'y' or 'n':\n")
#
# if play_y_n == 'y':
#
#     print(logo)
#     user_hand = [11,11]#[random.choice(cards) for i in range(2)]
#     computer_hand = [random.choice(cards) for i in range(2)]
#
#     user_score = get_score(user_hand)
#     computer_score = get_score(computer_hand)
#
#     if check_for_blackjack(user_score):
#         print("You win! :D")
#     if check_for_blackjack(computer_score):
#         print("You lose! :(")
#     user_score, user_hand = convert_ace(user_score, user_hand)
#
#     show_current_hands()
#
#     answer = input("Do you want to get another card? Type 'y' or 'n':\n")
#
#     #User Plays
#     while answer == 'y':
#         draw_cards(user_hand)
#         user_score = get_score(user_hand)
#
#         check_for_blackjack(user_score)
#         user_score, user_hand = convert_ace(user_score, user_hand)
#
#         show_current_hands()
#
#         answer = input("Do you want to get another card? Type 'y' or 'n':\n")
#
#     # Computer Plays
#     while computer_score < 17:
#         draw_cards(computer_hand)
#         computer_score = get_score(computer_hand)
#         if check_for_blackjack(computer_score):
#             print("Blackjack! Computer wins!")
#         if computer_score > 21:
#             show_final_hands()
#             print("Computer went over, you win! :D")
#         else:
#             if user_score > computer_score:
#                 show_final_hands()
#                 print("Your score was higher, you win! :D")
#             elif user_score < computer_score:
#                 show_final_hands()
#                 print("The computer's score was higher, you lose! :(")
#             else:
#                 show_final_hands()
#                 print("Looks like its a draw!")
#
#
