# this program will draw a square using turtle graphics library
from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape("turtle")
turtle.color("Green")

for _ in range(4):
    turtle.forward(100)
    turtle.right(90)

screen = Screen()
screen.exitonclick()