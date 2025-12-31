# creating right and left paddles for the pong game
from turtle import Turtle

class RightPaddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(350, 0)
    
    def move_up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)

class LeftPaddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(-350, 0)
    
    def move_up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)
        
    def move_down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)

