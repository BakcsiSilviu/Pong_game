from turtle import Turtle

class PlayArea(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.draw_area()

    def draw_area(self):
        self.penup()
        self.goto(-380, - 280)
        self.pendown()
        for _ in range(2):
            self.forward(380*2)
            self.left(90)
            self.forward(280*2)
            self.left(90)

