from turtle import Turtle
from random import randint

class Food(Turtle):

    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.create_pellet(screen_width=screen_width, screen_height=screen_height)

    def create_pellet(self, screen_width, screen_height):
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.color("Teal")
        self.food_eaten(screen_width=screen_width, screen_height=screen_height)
        
    def food_eaten(self, screen_width, screen_height):
        rand_x = randint(-1 * ((screen_width - 20) // 2), (screen_width - 20) // 2)
        rand_y = randint(-1 * ((screen_height - 20) // 2), (screen_height - 20) // 2)
        self.goto(rand_x, rand_y)