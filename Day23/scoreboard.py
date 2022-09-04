from turtle import Turtle, Screen
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.display_score()

    def update_score(self):
        self.score += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.goto(-300, 250)
        self.write(f'Score: {self.score}', align='left', font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER', align='center', font=FONT)
