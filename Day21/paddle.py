from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, start_x, start_y):
        super(Paddle, self).__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(start_x, start_y)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)