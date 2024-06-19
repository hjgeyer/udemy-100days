from turtle import Turtle, Screen
from random import randint,choice

leo = Turtle()
leo.shape("turtle")
leo.color("blue")
leo.penup()
raph = Turtle()
raph.shape("turtle")
raph.penup()
raph.color("red")
raph.setpos(0, 40)
mikey = Turtle()
mikey.shape("turtle")
mikey.color("orange")
mikey.penup()
mikey.setpos(0, 80)
donny = Turtle()
donny.shape("turtle")
donny.color("purple")
donny.penup()
donny.setpos(0, 120)
tmnt = [leo, raph, mikey, donny]
screen = Screen()
screen.setup(width=500,height=500)

guess = screen.textinput(title="Guess winner", prompt="Which TMNT will win the race? ").lower()

d_turtles = {
    "leo": leo,
    "raph": raph,
    "mikey": mikey,
    "donny": donny,
}

d_tmnt = {
    leo: "blue",
    raph: "red",
    mikey: "orange",
    donny: "purple",
}

t_guess = d_turtles[guess]

def goto_start(turtle: Turtle):
    turtle.goto((screen.window_width() // 2 - 15) * -1, turtle.position()[1])

def move_forward():
    leo.forward(10)

def move_backward():
    leo.backward(10)

def turn_left():
    leo.left(10)

def turn_right():
    leo.right(10)

def check_finisher(turtle: Turtle) -> bool:
    return (turtle.position()[0] * 2 > screen.window_width() - 50)


def sprint(turtle: Turtle):
    turtle.forward(randint(1, 10))

def reset():
    leo.penup()
    leo.home()
    leo.pendown()
    #screen.clearscreen()

def clear_the_screen():
    screen.resetscreen()
    
for turtle in tmnt:    
    goto_start(turtle)

turt = tmnt[0]
while not check_finisher(turt):
    turt = choice(tmnt)
    sprint(turtle=turt)

if d_tmnt[t_guess] == d_tmnt[turt]:
    print(f"Your {guess} won.")
else:
    print(f"You lose. {d_tmnt[turt]} won.")


#screen.listen()
#screen.onkey(key="w", fun=move_forward)
#screen.onkey(key="s", fun=move_backward)
#screen.onkey(key="a", fun=turn_left)
#screen.onkey(key="d", fun=turn_right)
#screen.onkey(key="r", fun=reset)
#screen.onkey(key="c", fun=clear_the_screen)

screen.exitonclick()