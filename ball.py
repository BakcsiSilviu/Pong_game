from turtle import Turtle
from random import choice
FIRST_BALL_ANGLES = [[x for x in range(20 , 70)], [x for x in range(110, 161)]]
ANGLE = choice(FIRST_BALL_ANGLES)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ball = Turtle("circle")
        self.speed = 0.4
        self.ball.color("white")
        self.ball.penup()
        self.ball.setheading(choice(ANGLE))

    def move(self):
        
        self.ball.forward(self.speed)

    def bounce(self):
        if self.ball.ycor() > 270 or self.ball.ycor() < -270:
            self.ball.setheading(360 - self.ball.heading())
    
    def bounce_on_paddle(self):
        self.ball.setheading(360 - self.ball.heading() + 180)
        self.speed += 0.1

    def out_of_play(self):
        self.ball.reset()
        
