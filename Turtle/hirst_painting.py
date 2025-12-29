# This program will draw a Hirst-style dot painting using turtle graphics library
import turtle as t
import random
import colorgram

# Extract colors from an image (optional - you can use an image file)
# If you have an image, uncomment the lines below and provide the image path
# colors = colorgram.extract('image.jpg', 30)
# color_list = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

# Curated color palette inspired by Damien Hirst's dot paintings
color_list = [
    (202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), 
    (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), 
    (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), 
    (14, 99, 71), (234, 175, 164), (16, 97, 75), (230, 206, 91),
    (244, 162, 97), (63, 26, 20), (223, 138, 69), (10, 79, 99),
    (219, 80, 121), (255, 230, 109), (174, 185, 215), (53, 126, 155),
    (38, 174, 96), (255, 201, 1), (255, 127, 80), (199, 1, 31),
    (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255)
]

# Setup turtle
tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()

number_of_dots = 10
dot_size = 20
spacing = 50

start_x = -(number_of_dots * spacing) / 2 + spacing / 2
start_y = (number_of_dots * spacing) / 2 - spacing / 2

for row in range(number_of_dots):
    tim.setpos(start_x, start_y - (row * spacing))
    for col in range(number_of_dots):
        tim.dot(dot_size, random.choice(color_list))
        tim.forward(spacing)

screen = t.Screen()
screen.exitonclick()