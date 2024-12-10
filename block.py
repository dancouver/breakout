from turtle import Turtle
import random

class Block(Turtle):

    def __init__(self, position, length, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=1, stretch_len=length)
        self.penup()
        self.goto(position)
        self.length = length

    def check_collision(self, ball):
        ball_top = ball.ycor() + 10
        ball_bottom = ball.ycor() - 10
        ball_left = ball.xcor() - 10
        ball_right = ball.xcor() + 10

        block_top = self.ycor() + 10
        block_bottom = self.ycor() - 10
        block_left = self.xcor() - (10 * self.length)
        block_right = self.xcor() + (10 * self.length)

        if block_left < ball_right < block_right and block_bottom < ball_top < block_top:
            if abs(ball_left - block_right) < 10 or abs(ball_right - block_left) < 10:
                ball.bounce_x()
            else:
                ball.bounce_y()
            return True
        return False
