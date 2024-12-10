from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lives = 5
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 350)
        self.write(f"Lives: {self.lives}", align="center", font=("Courier", 24, "normal"))

    def lose_life(self):
        self.lives -= 1
        self.update_scoreboard()
