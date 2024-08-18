from turtle import *
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("yellow")
        self.speed("fastest")
        x_coordinate = random.randint(-280,280)
        y_coordinate = random.randint(-280,280)
        self.goto(x_coordinate, y_coordinate)

    def refresh(self):
        x_coordinate = random.randint(-280, 280)
        y_coordinate = random.randint(-280, 280)
        self.goto(x_coordinate, y_coordinate)