from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from block import Block
import time
import random

screen = Screen()
screen.bgcolor('black')
screen.setup(width=1200, height=800)
screen.title("Breakout")
screen.tracer(0)

scoreboard = Scoreboard()
mPaddle = Paddle((0, -350))
ball = Ball((0, 0))

# Colors for the rows
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Create blocks
blocks = []
rows = 6
block_gap = 28  # Increased gap between rows by 40%
screen_width = 1200
block_y_start = 260  # Adjusted to move below the score bar

for row in range(rows):
    y_position = block_y_start - row * (40 + block_gap)
    num_blocks = random.randint(5, 10)
    total_gap_width = (num_blocks - 1) * block_gap
    block_width = (screen_width - total_gap_width) / num_blocks / 20  # divide by 20 for the stretch_len
    x_start = -(screen_width // 2) + (block_gap / 2)  # Adjust starting position to fit blocks properly

    for i in range(num_blocks):
        x_position = x_start + i * (block_width * 20 + block_gap)
        block = Block((x_position, y_position), block_width, colors[row])
        blocks.append(block)

def move_left():
    mPaddle.go_left()
    screen.onkeypress(move_left, "Left")

def move_right():
    mPaddle.go_right()
    screen.onkeypress(move_right, "Right")

screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Top bounce
    if ball.ycor() > 380:
        ball.bounce_y()

    # Side collision
    if ball.xcor() > 580 or ball.xcor() < -580:
        ball.bounce_x()

    # Paddle collision
    paddle_width = 100  # Since stretch_len=10 for paddle, the total width is 100 units
    if ball.ycor() < -320 and ball.ycor() > -340 and (mPaddle.xcor() - paddle_width / 2 < ball.xcor() < mPaddle.xcor() + paddle_width / 2):
        ball.paddle_bounce()
        ball.sety(-320)  # Adjust the ball position to avoid multiple bounces

    # Block collision
    for block in blocks:
        if block.check_collision(ball):
            block.hideturtle()
            blocks.remove(block)
            break

    # Bottom collision (lose life)
    if ball.ycor() < -380:
        ball.reset_position()
        mPaddle.goto(0, -350)  # Reset paddle to center
        scoreboard.lose_life()
        if scoreboard.lives == 0:
            game_is_on = False
            scoreboard.goto(0, 0)
            scoreboard.write("Game Over", align="center", font=("Courier", 36, "normal"))

screen.exitonclick()
