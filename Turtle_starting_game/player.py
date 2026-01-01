from turtle import Turtle
from car_manager import CarManager


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
    
    def move(self):
        self.forward(MOVE_DISTANCE)
    
    def go_to_start(self):
        self.goto(STARTING_POSITION)
    
    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y

    def collision_with_car(self, car_manager):
       for car in car_manager.all_cars:
           if self.distance(car) < 30:
               return True
       return False
        
   