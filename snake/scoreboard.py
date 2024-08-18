import turtle
from turtle import *

ALIGNMENT = "centre"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update()

    def update(self):
        self.write(f"Score is: {self.score}")

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update()

    def game_over(self):
        self.write(f"GAME OVER", align=ALIGNMENT)
