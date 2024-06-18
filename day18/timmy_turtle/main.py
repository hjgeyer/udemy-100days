from turtle import Turtle, Screen
import heroes as h
from random import randint

tim = Turtle()
tim.shape("turtle")
tim.color()
screen = Screen()
screen.colormode(255)

distance = 25
no_angles = 4

def get_pencolor() -> tuple:
    return (randint(1,255), randint(1, 255), randint(1, 255))

def draw_shapes(no_angles: int, distance: int):
    for i in range(3,no_angles + 1):
        tim.pencolor(get_pencolor())
        tim.pensize(10)
        for _ in range(i):
            tim.pendown()
            tim.forward(distance)
            tim.right(360/i)

#draw_shapes(no_angles, distance)

def draw_random_color_lines():
    for _ in range(1000):
        tim.speed(0)
        tim.forward(distance)
        tim.pencolor(get_pencolor())
        tim.pendown()
        tim.pensize(5)
        tim.setheading(randint(0,3) * 90)

def draw_dot(distance, is_filled: bool, radius: int,  color_line: tuple, color_fill: tuple):
    if color_fill is not None: 
        tim.color(color_line, color_fill)
    else:
        tim.color(color_line)
    tim.pendown()
    if is_filled:
        tim.begin_fill()
    tim.circle(radius)
    if is_filled:
        tim.end_fill()
    tim.penup()
    if is_filled:
        tim.forward(distance)

#draw_random_color_lines()
def draw_circles(distance):
    for c in range(5): # Columns
        for _ in range(5): # Rows
            draw_dot(distance=80, is_filled=True, radius=30, color_line=get_pencolor(), color_fill=get_pencolor())
        tim.setheading(90)
        if c % 2 == 0: 
            tim.forward(130)
            tim.setheading(180)
        else:
            tim.forward(10)
            tim.setheading(0)
        tim.forward(distance)
        
#draw_circles(80)    

def draw_spiro(size_of_gap:int, radius:int):
    for i in range(360//size_of_gap):
        tim.speed(0)
        draw_dot(distance=size_of_gap, is_filled=False, radius=radius, color_line=get_pencolor(), color_fill=None)
        tim.left(size_of_gap)

draw_spiro(size_of_gap=10, radius=200)

#tim.setheading(90)
#tim.forward(100)
#tim.setheading(180)
#tim.forward(100)
#tim.setheading(90)
#tim.forward(100)
#tim.setheading(0)
#tim.forward(100)

screen.exitonclick()