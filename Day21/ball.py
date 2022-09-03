import time
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.shape('circle')
        self.color('red')
        self.penup()

    def move(self):
        new_x = self.xcor() + 0.1
        new_y = self.ycor() + 0.1
        self.goto(new_x, new_y)