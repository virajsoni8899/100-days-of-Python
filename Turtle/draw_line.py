# this program will draw a dashed line using turtle graphics library

from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape("turtle")
turtle.color("Green")

for _ in range(15):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()

screen = Screen()
screen.exitonclick()