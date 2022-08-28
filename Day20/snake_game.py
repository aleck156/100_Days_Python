from turtle import Turtle as t, Screen as s
import random

score = 0

snake = []
for index in range(0, 3):
    new_snake_part = t()
    new_snake_part.setx(index * (-25))
    new_snake_part.color('white')
    new_snake_part.shape('square')
    snake.append(t())

screen = s()
screen.setup(width=1600, height=1200)
screen.title('Welcome to the SNAKE GAME')
screen.bgcolor('black')
screen.colormode(255)
screen.listen()

screen.exitonclick()

