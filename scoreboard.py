from msilib.schema import Font
from re import A
from this import s
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
FONT_2 = ("Courier", 25, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()

        self.hideturtle()
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.write(f"SCORE: {self.score}", align=ALIGNMENT,
                   font=FONT)

    def score_increase(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT_2)
