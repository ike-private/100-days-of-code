FONT = ("Courier", 24, "normal")
from turtle import *


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.penup()
        self.goto(-280,260)
        self.update_scoreboard()
        self.hideturtle()


    def update_scoreboard(self):
        self.write(f"Level: {self.level}", font=FONT, align="left")

    def increase_score(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def end_game(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER!", font=FONT, align="center")
