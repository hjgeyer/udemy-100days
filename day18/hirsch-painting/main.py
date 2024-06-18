import colorgram
from turtle import Turtle, Screen
from random import randint,choice

tim = Turtle()
tim.shape("turtle")
tim.color()
screen = Screen()
screen.colormode(255)



colors = colorgram.extract(".\\day18\\hirsch-painting\\damien-hirst-severed-spots.jpg", 20)

t_colors = [(col.rgb.r, col.rgb.g, col.rgb.b) for col in colors]
print(t_colors)

def get_pencolor() -> tuple:
    return (choice(t_colors))

def draw_circles(distance):
    for c in range(10): # Columns
        for _ in range(10): # Rows
            draw_dot(distance=50, is_filled=True, radius=20, color_line=get_pencolor(), color_fill=get_pencolor())
        tim.setheading(90)
        if c % 2 == 0: 
            tim.forward(2*distance-15)
            tim.setheading(180)
        else:
            tim.forward(10)
            tim.setheading(0)
        tim.forward(distance)

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

tim.speed(0)
draw_circles(50)
screen.exitonclick()