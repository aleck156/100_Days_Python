from turtle import Turtle


ALIGNMNET = "center"
FONT = 'Arial'
FONT_SIZE = 24
FONT_TYPE = 'normal'

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 530)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.penup()
        self.goto(0, 530)
        self.write(f'Score: {self.score}', align=ALIGNMNET, font=(FONT, FONT_SIZE, FONT_TYPE))
        self.hideturtle()

    def add_point(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()