#  Control Flow and Logical Operators
#  Treasure Island Project -> If-else project


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______
*******************************************************************************
''')

print("Welcome to Treasure Island\nYour Mission is to find the treasure.")

choice1 = input("You're at a crossroads. Which direction do you want to go? L or R\n").lower()
if choice1== "l":
    choice2 = input("""
                    You've come to a lake. There is an island in the middle of the lake.
                    To wait for a boat, type 'W'. To swim, type s.
                    """).lower()
    if choice2 == "w":
        choice3 = input("""
                        You arrive at the island unharmed and find a house with 3 different colored doors.
                        Which door do you choose, red (R), blue (B), or Yellow (Y)?
                        """).lower()
        if choice3 == "r":
            print("The door slams shut behind you and the room is on fire. Game Over.")
        elif choice3.lower() == "b":
            print("The door slams shut behind you and you realize there is a sleeping lion in the room. Game Over")
        else:
            print("You are greeted by a shining chest full of gold. You Win!")
    else:
        print("Game Over.")
else:
    print("Game Over.")