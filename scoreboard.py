from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()

    def update(self):
        self.goto(-100, 200)
        self.write(self.l_score, font=("courier", 50, "normal"), align="center")
        self.goto(100, 200)
        self.write(self.r_score, font=("courier", 50, "normal"), align="center")
