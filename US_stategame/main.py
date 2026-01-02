from turtle import Turtle, Screen
import turtle
import pandas as pd

screen = Screen()

screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# text input for the state name
user_answer = screen.textinput(title="Guess the State", prompt="What's another state's name?")

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()

while len(all_states) > 0:
    answer_state = user_answer.title()
    if answer_state in all_states:
        print(f"You've guessed {answer_state} correctly!")
        t = Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(data[data.state == answer_state].x), int(data[data.state == answer_state].y))
        t.write(answer_state)
        all_states.remove(answer_state)
    else:
        print(f"You've guessed {answer_state} incorrectly!")

    user_answer = screen.textinput(title="Guess the State", prompt="What's another state's name?")













screen.exitonclick()

