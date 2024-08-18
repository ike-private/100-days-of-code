from turtle import *


class Paddle(Turtle):
    def __init__(self, p):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(p)

    def go_up(self):
        y_coor = self.ycor() + 20
        self.goto(self.xcor(), y_coor)

    def go_down(self):
        y_coor = self.ycor() - 20
        self.goto(self.xcor(), y_coor)
