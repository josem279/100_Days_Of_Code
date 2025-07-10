# Dictionaries, nesting, and secret auction code challenge


############# Dict work:
# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }

# student_grades = {}

# for k, v in student_scores.items():
#     if v >= 91:
#         student_grades[k] = "Outstanding"
#     elif 80 < v  and v <= 90:
#         student_grades[k] = "Exceeds Expectations"
#     elif 70 < v and v <= 80:
#         student_grades[k] = "Acceptable"
#     # elif v <= 70:
#     else:
#         student_scores[k] = "Fail"

# print(student_grades)

################## Blind Auction Program
import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\
'''

bids = {}
auction = True

print(logo)
print("Welcome to the secret auction program.\n")

while auction:
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n$"))
    bids[name] = bid
    other_bidders_y_n = input("Are there any other bidders? Type 'yes' or 'no'\n")

    if other_bidders_y_n == 'no':
        auction = False
    else:
        os.system('cls')
    
winner = ""
w_bid_amount = 0

for k, v in bids.items():
    if v > w_bid_amount:
        winner = k
        w_bid_amount = v

print(f"The winner is {winner}, with a bid of ${w_bid_amount}.")
