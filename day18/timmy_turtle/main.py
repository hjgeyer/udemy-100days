from turtle import Turtle, Screen
import heroes as h

tim = Turtle()
tim.shape("turtle")
tim.color("red")

for _ in range(4):
    tim.forward(100)
    tim.right(90)

print(h.gen())

screen = Screen()
screen.exitonclick()