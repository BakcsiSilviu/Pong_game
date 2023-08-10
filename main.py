from turtle import Screen
from playarea import PlayArea
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width= 800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

play_area = PlayArea()
paddle1 = Paddle((-360, 0))
paddle2 = Paddle((360, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.update()
time.sleep(1)
game_on = True

screen.listen()
screen.onkey(fun=paddle1.up, key="w")
screen.onkey(fun=paddle1.down, key="s")
screen.onkey(fun=paddle2.up, key="Up")
screen.onkey(fun=paddle2.down, key="Down")

while game_on == True:
    screen.update()
    ball.move()
    ball.bounce()
    # Detect paddle collision
    if ball.ball.distance(paddle1.pad) < 20 or (ball.ball.xcor() <= -340 and ball.ball.distance(paddle1.pad) < 50):
        ball.bounce_on_paddle()
    elif ball.ball.distance(paddle2.pad) < 20 or (ball.ball.xcor() >= 340 and ball.ball.distance(paddle2.pad) < 50):
        ball.bounce_on_paddle()
    # Detect goals and update the current score
    if ball.ball.xcor() < -360 or ball.ball.xcor() > 360:
        if ball.ball.xcor() < -360:
            scoreboard.p2_scores()
        elif ball.ball.xcor() > 360:
            scoreboard.p1_scores()
        ball.out_of_play()
        ball = Ball()
        time.sleep(1)

screen.exitonclick()