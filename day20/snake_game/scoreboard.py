from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")

class Scoreboard(Turtle):

    def __init__(self, screen_height: int):
        super().__init__()
        self.score = -1 
        self.screen_height = screen_height
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_score()
        

    def update_score(self):
        self.clear()
        self.goto(0, (self.screen_height // 2) - 20)
        self.score += 1
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)


    def end_game(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER!", align=ALIGNMENT, font=FONT)