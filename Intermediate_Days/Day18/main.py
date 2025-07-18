# The Hirst Paining Project
import colorgram
import turtle as t
import random

# Extracting color tuples from hirst image in following location:
# colors = colorgram.extract(r'INSERT_PATH_HERE', 30)

# rgb_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_list.append(new_color)

# # List of colors extracted:     
# print(rgb_list)

t.colormode(255)

color_list = [(218, 217, 228), (236, 231, 236), (228, 213, 200), (218, 195, 147), (223, 171, 92), (148, 174, 184), (196, 158, 178), (209, 217, 214), (141, 179, 163), (207, 149, 26), (54, 159, 183), (171, 201, 191), (210, 179, 190), (38, 131, 191), (222, 181, 172), (214, 87, 53), (80, 152, 115), (135, 87, 70), (196, 100, 165), (108, 91, 95), (65, 41, 39), (174, 199, 202), (62, 39, 41), (80, 141, 106), (79, 56, 53), (182, 190, 207), (80, 55, 57), (74, 134, 187)]

jose = t.Turtle()
jose.penup()

def draw_row():
    for _ in range(10):
        jose.color(random.choice(color_list))
        jose.dot(20)
        jose.forward(50)
        
        
def turn():
    dir = jose.heading()
    if dir == 0.0:
        jose.left(90)
        jose.forward(50)
        jose.left(90)
        jose.forward(50)
    else:
        jose.right(90)
        jose.forward(50)
        jose.right(90)
        jose.forward(50)
      
jose.setheading(225)
jose.forward(250)
jose.setheading(0)
      
for _ in range(10):
    draw_row()
    turn()


screen = t.Screen()
screen.exitonclick()
