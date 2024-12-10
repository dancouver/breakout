from turtle import Turtle
import random
import math

class Ball(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color('white')
        self.shape("circle")
        self.penup()
        self.speed_multiplier = 1.3  # Initial speed increase by 30%
        self.x_move = 6.5 * self.speed_multiplier  # Initial speed
        self.y_move = 6.5 * self.speed_multiplier  # Initial speed
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.adjust_speed()

    def bounce_x(self):
        self.x_move *= -1
        self.adjust_speed()

    def reset_position(self):
        self.goto(0, -320)
        self.setheading(45)
        self.x_move = 6.5 * self.speed_multiplier * math.cos(math.radians(45))
        self.y_move = 6.5 * self.speed_multiplier * math.sin(math.radians(45))
        self.move_speed = 0.1

    def adjust_speed(self):
        # Adjust speed by -20% to 20%
        speed_factor = random.uniform(0.8, 1.2)
        self.x_move *= speed_factor
        self.y_move *= speed_factor

    def paddle_bounce(self):
        # Randomly adjust the angle slightly when bouncing off the paddle
        angle = math.atan2(self.y_move, self.x_move)
        angle_adjustment = random.uniform(-15, 15)  # Adjust angle by -15 to 15 degrees
        new_angle = angle + math.radians(angle_adjustment)

        # Ensure the ball bounces upwards or downwards
        if self.y_move > 0:
            self.y_move = abs(math.sin(new_angle)) * math.hypot(self.x_move, self.y_move)
        else:
            self.y_move = -abs(math.sin(new_angle)) * math.hypot(self.x_move, self.y_move)

        self.x_move = math.cos(new_angle) * math.hypot(self.x_move, self.y_move)
