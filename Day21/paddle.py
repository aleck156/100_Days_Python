from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, start_x, start_y):
        super(Paddle, self).__init__()
        self.paddle = Turtle()
        self.paddle.shape('square')
        self.paddle.color('white')
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(start_x, start_y)

    def move_up(self):
        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() + 20)

    def move_down(self):
        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() - 20)