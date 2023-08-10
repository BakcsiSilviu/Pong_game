from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.p1_points = 0
        self.p2_points = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.update_score()

    def update_score(self):
        self.write(f"{self.p1_points} : {self.p2_points}", False,  ALIGNMENT, FONT)

    def p1_scores(self):
        self.clear()
        self.p1_points += 1
        self.update_score()

    def p2_scores(self):
        self.clear()
        self.p2_points += 1
        self.update_score()