import time
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.x_move = 0.1
        self.y_move = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.x_move *= 1.1
        self.y_move *= 1.1

    def reset_position(self):
        self.home()
        self.bounce_x()
        self.x_move = 0.1
        self.y_move = 0.1