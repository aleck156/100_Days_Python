import time
from turtle import Turtle, Screen
import random
from functools import partial

score = 0
speed = 0.1
screen = Screen()

snake = []

screen.tracer(0)
for index in range(0, 3):
    new_snake_part = Turtle(shape='square')
    new_snake_part.penup()
    new_snake_part.goto(index * (-20), 0)
    new_snake_part.color('white')
    snake.append(new_snake_part)

screen.update()

screen.setup(width=1600, height=1200)
screen.title('Welcome to the SNAKE GAME')
screen.bgcolor('black')
screen.colormode(255)

def move_snake(snake):
    for piece in snake:
        piece.forward(20)

for _ in range(0,10):
    screen.delay(5)
    for seg_num in range(len(snake)-1, 0, -1):
        new_x = snake[seg_num-1].xcor()
        new_y = snake[seg_num-1].ycor()
        snake[seg_num].goto(new_x, new_y)
    snake[0].forward(20)
    time.sleep(speed)
    screen.update()

screen.listen()
# screen.onkey(partial(move_snake,snake), 'space')

screen.exitonclick()

