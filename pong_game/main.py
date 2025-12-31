# setting up the screen for the pong game
from turtle import Screen, Turtle
from paddle import RightPaddle, LeftPaddle
from ball import Ball
from scoreboard import Scoreboard
import time

# setting up the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


# creating the paddles
right_paddle = RightPaddle()
left_paddle = LeftPaddle()
screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

# creating the ball
ball = Ball()

# creating the scoreboard
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    # detect collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    # detect collision with paddle
    if ball.distance(right_paddle)<60 and ball.xcor()>320 or ball.distance(left_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()
        ball.increase_speed()
    #detect when the ball goes out of bounds
    if ball.xcor()>380:
        ball.reset_position()
        ball.reset_speed()
        scoreboard.l_point()
    if ball.xcor()<-380:
        ball.reset_position()
        ball.reset_speed()
        scoreboard.r_point()


screen.exitonclick()