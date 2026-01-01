from turtle import Turtle


highest_score_file = "highest_score.txt"

def get_highest_score():
    try:
        with open(highest_score_file, mode="r") as file:
            content = file.read().strip()
            if content:
                return int(content)
            return 0
    except FileNotFoundError:
        return 0
    except ValueError:
        return 0

def update_highest_score(score):
    try:
        with open(highest_score_file, mode="w") as file:
            file.write(str(score))
    except FileNotFoundError:
        return 0



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)

        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def get_score(self):
        return self.score

        