# this program will draw a random walk using turtle graphics library

from turtle import Turtle, Screen
import random

turtle = Turtle()

turtle.shape("turtle")


def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

directions = [0, 90, 180, 270]

turtle.pensize(10)
turtle.speed(10)

for _ in range(100):
    turtle.color(get_random_color())
    turtle.forward(30)
    turtle.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()