# Creating functions and working with While loops

# Code to be used with Reborg's World Maze World:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if front_is_clear() and not right_is_clear():
        move()
    else:
        if right_is_clear():
            turn_right()
            if front_is_clear():
                move()
        elif not right_is_clear() and not front_is_clear():
            turn_left()
            if not right_is_clear() and not front_is_clear():
                turn_left()
        else:
            move()