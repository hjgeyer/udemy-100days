from turtle import Turtle

SCREEN_WIDTH = (800 // 2) - 20
SCREEN_HEIGHT = (600 // 2) - 20

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        #self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.color("white")
        self.penup()

    def move_ball(self):
        if self.ycor() > SCREEN_HEIGHT - 10:
            self.setheading(self.heading() + 60)
        #elif self.xcor() > SCREEN_WIDTH - 10:
        #    self.setheading(self.heading() - 225)
        elif self.ycor() < -SCREEN_HEIGHT + 10:
            self.setheading(self.heading() - 225)
        #elif self.xcor() < -SCREEN_WIDTH + 10:
        #    self.setheading(self.heading() + 225)
        self.forward(20)