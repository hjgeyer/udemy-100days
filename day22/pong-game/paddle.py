from turtle import Turtle

UP = 90
DOWN = 270
SCREEN_WIDTH = (800 // 2) - 20
SCREEN_HEIGHT = (600 // 2) - 20
SPEED = 20

class Paddle():

    
    def __init__(self):
        super().__init__()
        self.paddles = []
        self.paddles.append(self.create_paddle(start_x=SCREEN_WIDTH, start_y=0))
        self.paddles.append(self.create_paddle(start_x=-SCREEN_WIDTH - 7,start_y=0))


    def create_paddle(self, start_x, start_y):
        paddle = Turtle()
        paddle.shape("square")
        paddle.color("white")
        paddle.penup()
        paddle.shapesize(stretch_wid=1, stretch_len=5)
        paddle.goto(x=start_x, y=start_y)
        paddle.setheading(UP)
        return paddle

    def move_paddle(self):
        for paddle in self.paddles:
            if paddle.heading() == UP and paddle.ycor() > SCREEN_HEIGHT - 40:
                paddle.setheading(DOWN)
            if paddle.heading() == DOWN and paddle.ycor() < -SCREEN_HEIGHT + 40:
                paddle.setheading(UP)
            paddle.forward(SPEED)   

    def move_left_paddle_up(self):
        self.paddles[1].setheading(UP)
        
    def move_left_paddle_down(self):
        self.paddles[1].setheading(DOWN)
        
    def move_right_paddle_up(self):
        self.paddles[0].setheading(UP)
        
    def move_right_paddle_down(self):
        self.paddles[0].setheading(DOWN)
    