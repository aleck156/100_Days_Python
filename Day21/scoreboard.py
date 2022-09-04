from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, screen_x, screen_y):
        super(Scoreboard, self).__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-screen_x / 2 + 30, screen_y * 0.4)
        self.write(self.l_score, align='center', font=('Courier', int(screen_y / 15), 'normal'))

        self.goto(screen_x / 2 - 30, screen_y * 0.4)
        self.write(self.r_score, align='center', font=('Courier', int(screen_y / 15), 'normal'))
