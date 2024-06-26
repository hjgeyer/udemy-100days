from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

continue_moving = True

screen.listen()

score = Scoreboard(screen.window_height())
snake = Snake()
pellet = Food(screen.window_width(), screen.window_height())

s_height = screen.window_height()
s_width = screen.window_width()


print(snake.head.heading())

while continue_moving:
    snake.move()
    screen.update()
    time.sleep(.5)
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Right", fun=snake.right)
    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)
    
    if ((snake.head.xcor() + 20 >= s_width // 2) or
        (snake.head.xcor() - 15 <= -s_width // 2) or
        (snake.head.ycor() + 15 >= s_height // 2) or
        (snake.head.ycor() - 15 <= -s_height // 2) or 
        snake.eat_body()):
        continue_moving = False
        score.end_game()
    
    if pellet.distance(snake.location()) <= 15: 
        snake.add_snake_part()
        pellet.food_eaten(s_width, s_height)
        score.update_score()
        

screen.exitonclick()