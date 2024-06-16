from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Score

screen = Screen()
tur = Turtle()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
score = Score()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
ball = Ball()
game = True
while game:
    ball.speed(0)
    time.sleep(0.05)
    screen.update()
    score.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50:
        ball.bounce_x()
    if ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset_pos()
        score.clear()
        score.l_score += 1
    if ball.xcor() < -380:
        ball.reset_pos()
        score.clear()
        score.r_score += 1

screen.exitonclick()
