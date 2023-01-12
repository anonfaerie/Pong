from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "o")
screen.onkey(r_paddle.down, "l")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    if ball.ycor() > l_paddle.ycor() - 50 and ball.ycor() < l_paddle.ycor() + 50 and ball.xcor() - 10 == l_paddle.xcor():
        ball.bounce_x()

    if ball.ycor() > r_paddle.ycor() - 50 and ball.ycor() < r_paddle.ycor() + 50 and ball.xcor() + 10 == r_paddle.xcor():
        ball.bounce_x()


    #Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect a miss R and L paddles
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()







screen.exitonclick()

