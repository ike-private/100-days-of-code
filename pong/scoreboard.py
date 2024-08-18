from turtle import *


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

    def update(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score, align="centre", font=("Courier", 80, "normal"))
        self.goto(100,200)
        self.write(self.r_score, align="centre", font=("Courier", 80, "normal"))


    def left_point(self):
        self.l_score += 1
        self.update()

    def right_point(self):
        self.update()
        self.r_score += 1
