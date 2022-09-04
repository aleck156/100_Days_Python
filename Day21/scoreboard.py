from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, screen_x, screen_y):
        super(Scoreboard, self).__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.screen_x = screen_x
        self.screen_y = screen_y
        self.display_scores()

    def display_scores(self):
        self.clear()
        self.goto(-self.screen_x / 2 + 30, self.screen_y * 0.4)
        self.write(self.l_score, align='center', font=('Courier', int(self.screen_y / 15), 'normal'))

        self.goto(self.screen_x / 2 - 30, self.screen_y * 0.4)
        self.write(self.r_score, align='center', font=('Courier', int(self.screen_y / 15), 'normal'))
    def l_point(self):
        self.l_score += 1
        self.display_scores()

    def r_point(self):
        self.r_score += 1
        self.display_scores()