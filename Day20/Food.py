from turtle import Turtle
import random
# from snake_game import SCREEN_WIDTH, SCREEN_HEIGHT

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        # self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('white')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        random_x = random.randint(-800 + 25, 800 - 25)
        random_y = random.randint(-600 + 25, 600 - 25)
        self.goto(random_x, random_y)
