# Importing modules, installing packaged, and working with aliases
# Working with GUI 

import turtle as t
import random

t.colormode(255)

colors = ["red", "blue", "green", "pink", "yellow", "orange", "purple", "coral"]
direction = [0, 90, 180, 270]

# Intro
timmy_the_turtle = t.Turtle()
timmy_the_turtle.speed('fastest')
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.pensize(10)
# timmy_the_turtle.color("coral")
# timmy_the_turtle.fd(100)
# timmy_the_turtle.right(90)

#################### Challenge 1 - Draw a square

# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)

#################### Challenge 2 - Draw a dashed line

# for i in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

#################### Challenge 3 - Draw shapes

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for i in range(num_sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)    

# for shape_side_n in range(3, 9):
#     timmy_the_turtle.color(random.choice(colors))
#     draw_shape(shape_side_n)

#################### Challenge 4 - Draw a random walk

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def random_step():
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.right(random.choice(direction))

# for i in range(1, 50):
#     random_step()
#     timmy_the_turtle.forward(30)


#################### Challenge 5 - Draw a spirograph

def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gap)
        

draw_spirograph(5)

# Control Screen
screen = t.Screen()
screen.exitonclick()
