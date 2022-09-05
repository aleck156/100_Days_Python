from turtle import Turtle


ALIGNMNET = "center"
FONT = 'Arial'
FONT_SIZE = 24
FONT_TYPE = 'normal'

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())
        # self.high_score = 0
        self.color('white')
        self.penup()
        self.goto(0, 530)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.penup()
        self.goto(0, 530)
        self.write(f'Score: {self.score} HIGH Score: {self.high_score}', align=ALIGNMNET, font=(FONT, FONT_SIZE, FONT_TYPE))
        self.hideturtle()

    def reset(self):
        if self.score > self.high_score
            self.high_score = self.score
            with open('data.txt', mode='w') as data:
                data.write(f'{self.high_score}')
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', align=ALIGNMNET, font=(FONT, FONT_SIZE, FONT_TYPE))


    def add_point(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()