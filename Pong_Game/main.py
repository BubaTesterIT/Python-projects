from turtle import  Screen
from paddle import Paddle
from ball import Ball
import time

from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down,"Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_over = False

while not game_over:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()

    # Detect r_paddle missed
    if ball.xcor() > 400:
        ball.reset_ball()
        scoreboard.l_point()

    # Detect l_paddle missed
    if ball.xcor() < -400:
        ball.reset_ball()
        scoreboard.r_point()


    # Detect collision with the paddle
    if ball.distance(r_paddle) < 30 and ball.xcor() < 360 or ball.distance(l_paddle) < 30 and ball.xcor() > -360:
        ball.bounce_x()

screen.exitonclick()
