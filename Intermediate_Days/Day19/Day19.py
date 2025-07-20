# Instances, States, and Higher Order Functions

from turtle import Turtle, Screen

jose = Turtle()
screen = Screen()

def move_forwards():
    jose.forward(10)

screen.listen()
# screen.onkey(key="space", fun=move_forwards)



################# Challenge 1 - Create an etch-a-sketch app
def move_backwards():
    jose.backward(10)

def rotate_right():
    heading = jose.heading() + 10
    jose.setheading(heading)
    
def rotate_left():
    heading = jose.heading() - 10
    jose.setheading(heading)
    
def clear():
    jose.clear()
    jose.penup()
    jose.home()
    jose.pendown()
    
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=rotate_left)
screen.onkey(key="d", fun=rotate_right)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="c", fun=clear)



screen.exitonclick()
