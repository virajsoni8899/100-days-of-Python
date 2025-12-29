# this program will draw shapes using turtle graphics library like triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon
from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.shape("turtle")

colors = ["red", "green", "blue", "yellow", "purple", "orange", "pink", "brown", "gray", "black"]

for i in range(3, 11):
    angle = 360 / i
    turtle.color(random.choice(colors))
    for _ in range(i):
        
        turtle.forward(100)
        turtle.right(angle)

screen = Screen()
screen.exitonclick()
