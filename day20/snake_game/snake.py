from turtle import Turtle

MOVEMENT_SPEED = 20
UP = 90
LEFT = 180
RIGHT = 0
DOWN = 270

class Snake:

    snake_body = []

    def __init__(self,):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for i in range(0, 60, 20):
            snake_part = Turtle(shape="square")
            snake_part.color("white")
            snake_part.penup()
            snake_part.goto(-i,0)
            self.snake_body.append(snake_part)

    def location(self):
        return self.head.position()

    def move(self):
        for snake_part in range(len(self.snake_body) - 1, 0, -1): 
            self.snake_body[snake_part].goto(self.snake_body[snake_part - 1].pos())
            
        self.head.forward(MOVEMENT_SPEED)

    def eat_body(self) -> bool: 
        for snake_part in self.snake_body[1:]:
            if snake_part.distance(self.head) < 15:
                return True
        return False
                
    def add_snake_part(self):
        last_snake_part = self.snake_body[- 1]
        new_snake_part = Turtle(shape="square")
        new_snake_part.color("white")
        new_snake_part.penup()

        self.snake_body.append(new_snake_part)
            
    def left(self,):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
