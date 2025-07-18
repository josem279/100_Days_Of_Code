

####################################### My own solution
def get_score(user_hand):
    score = sum(user_hand)
    return score

def show_current_hands():
    print(f"Your cards: {user_hand}, current score: {user_score}")
    print(f"Computer's first card: {computer_hand[0]}")

def draw_cards(hand):
    hand.append(random.choice(cards))

def check_for_blackjack(score):
    if score == 21:
        print("Blackjack!!")
    return True

def convert_ace(user_score, user_hand):
    if user_score > 21:
        if  11 in user_hand:
            for i, num in enumerate(user_hand):
                if num == 11:
                    user_hand[i] = 1
                    break
            user_score = get_score(user_hand)
    user_score = get_score(user_hand)
    if user_score > 21:
        show_final_hands()
        print("You went over, you lose! :(")
        sys.exit()
    check_for_blackjack(user_score)
    return user_score, user_hand

def show_final_hands():
    print(f"Your final hand: {user_hand}, final score: {user_score}")
    print(f"Computers final hand: {computer_hand}")


logo = '''
 ___   ___
|A  | |10 |
| ♣ | | ♦ |
|__A| |_10|
'''

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
computer_cards = []

play_y_n = input("Do you want to play a game of blackjack? Type 'y' or 'n':\n")

if play_y_n == 'y':

    print(logo)
    user_hand = [11,11]#[random.choice(cards) for i in range(2)]
    computer_hand = [random.choice(cards) for i in range(2)]

    user_score = get_score(user_hand)
    computer_score = get_score(computer_hand)

    if check_for_blackjack(user_score):
        print("You win! :D")
    if check_for_blackjack(computer_score):
        print("You lose! :(")
    user_score, user_hand = convert_ace(user_score, user_hand)

    show_current_hands()

    answer = input("Do you want to get another card? Type 'y' or 'n':\n")

    #User Plays
    while answer == 'y':
        draw_cards(user_hand)
        user_score = get_score(user_hand)

        check_for_blackjack(user_score)
        user_score, user_hand = convert_ace(user_score, user_hand)

        show_current_hands()

        answer = input("Do you want to get another card? Type 'y' or 'n':\n")

    # Computer Plays
    while computer_score < 17:
        draw_cards(computer_hand)
        computer_score = get_score(computer_hand)
        if check_for_blackjack(computer_score):
            print("Blackjack! Computer wins!")
        if computer_score > 21:
            show_final_hands()
            print("Computer went over, you win! :D")
        else:
            if user_score > computer_score:
                show_final_hands()
                print("Your score was higher, you win! :D")
            elif user_score < computer_score:
                show_final_hands()
                print("The computer's score was higher, you lose! :(")
            else:
                show_final_hands()
                print("Looks like its a draw!")


