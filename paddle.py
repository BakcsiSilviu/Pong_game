from turtle import Turtle

player2_paddle = []
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.pad = Turtle("square")
        self.pad.shapesize(5, 1)
        self.pad.color("white")
        self.pad.penup()
        self.pad.goto(position)

    def up(self):
        if self.pad.ycor() == 220:
            pass
        else:
            new_y = self.pad.ycor() + 30
            self.pad.goto(self.pad.xcor(), new_y)

    def down(self):
        if self.pad.ycor() == -220:
            pass
        else:
            new_y = self.pad.ycor() - 30
            self.pad.goto(self.pad.xcor(), new_y)

            

