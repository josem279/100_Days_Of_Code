# U.S States Game
import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = r'Intermediate_Days\Day25\blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv(r"Intermediate_Days\Day25\50_states.csv")
all_states = data.state.to_list()
guessed_states = []

        
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    # If User writes 'Exit' the nwe add the states you've missed to a csv file and exit loop

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv(r"Intermediate_Days\Day25\states_to_learn.csv")
        break
    # Check if answer is in 50 states
    if answer_state in all_states:
        # If right - create a turtle to write the name of the sate at give x, y coords
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
