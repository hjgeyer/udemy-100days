from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title(titlestring="Pong Game")
screen.tracer(0)
screen.listen()

paddle = Paddle()
ball = Ball()

is_game_over = False

while not is_game_over:
    time.sleep(.20)
    paddle.move_paddle()
    ball.move_ball()
    print(f"Distance Paddle[0]: {ball.distance(paddle.paddles[0].position())}")
    print(f"Distance Paddle[1]: {ball.distance(paddle.paddles[1].position())}")
    if ball.distance(paddle.paddles[0].position()) < 25 or ball.distance(paddle.paddles[1].position()) < 25:
        print('Hit')
        ball.setheading(ball.heading() + 225)
        ball.forward(20)

    screen.update()
    screen.onkeypress(key="Up", fun=paddle.move_right_paddle_up)
    screen.onkeypress(key="Down", fun=paddle.move_right_paddle_down)
    screen.onkeypress(key="w", fun=paddle.move_left_paddle_up)
    screen.onkeypress(key="s", fun=paddle.move_left_paddle_down)

screen.exitonclick()