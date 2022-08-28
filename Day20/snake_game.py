from turtle import Turtle, Screen
import random
from functools import partial

score = 0
screen = Screen()

snake = []
for index in range(0, 5):
    new_snake_part = Turtle(shape='square')
    new_snake_part.penup()
    new_snake_part.goto(index * (-20), 0)
    new_snake_part.color('white')
    snake.append(new_snake_part)
print(snake)

screen.setup(width=1600, height=1200)
screen.title('Welcome to the SNAKE GAME')
screen.bgcolor('black')
screen.colormode(255)

def move_snake(snake):
    for piece in snake:
        piece.forward(20)

for _ in range(0,10):
    for seg in snake:
        seg.forward(20)

screen.listen()
# screen.onkey(partial(move_snake,snake), 'space')

screen.exitonclick()

