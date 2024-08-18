from paddle import *
from ball import *
import time
from scoreboard import *

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))
ball = Ball()
score_board = ScoreBoard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
sleep = 0.1
while game_is_on:
    time.sleep(sleep)
    screen.update()
    ball.move()
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()
        if sleep > 0:
            sleep *= 0.9

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        sleep = 0.1
        ball.reset()
        score_board.right_point()

    if ball.xcor() < -380:
        sleep = 0.1
        ball.reset()
        score_board.left_point()

screen.exitonclick()