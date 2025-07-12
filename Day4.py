# Randomisation and Python Lists
import random

random_integer = random.randint(1,3)

print("Rock, Paper, Scissors!")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = input("Pick, rock (r), paper (p), or scissors (s):\n")

if user_choice.lower() not in ["r", "p", "s"]:
    print("Invalid user choice. You lose!")

if random_integer == 1:
    computer_choice = "r"
elif random_integer == 2:
    computer_choice = "p"
else:
    computer_choice = "s"

if user_choice.lower() == computer_choice:
    print("Draw, no winner")
elif user_choice.lower() == "r":
    print(f"You picked: {rock}")
    if computer_choice == "p":
        print(f"Computer picked:{paper}. Computer wins!")
    else:
        print(f"Computer picked: {scissors}. You win!")
elif user_choice.lower() == "p":
    print(f"You picked: {paper}")
    if computer_choice == "s":
        print(f"Computer picked, {scissors}. Computer wins!")
    else:
        print(f"Computer picked: {rock}. You win!")
elif user_choice.lower() == "s":
    print(f"You picked: {scissors}")
    if computer_choice == "r":
        print(f"Computer picked: {rock}. Computer wins!")
    else:
        print(f"Computer picked: {paper}. You win!")

