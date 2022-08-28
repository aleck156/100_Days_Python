import time
from turtle import Turtle, Screen
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard

speed = 0.1
screen = Screen()

snake = []

screen.tracer(0)

snake = Snake(3)
screen.update()

screen.setup(width=1600, height=1200)
screen.title('Welcome to the SNAKE GAME')
screen.bgcolor('black')
screen.colormode(255)

def move_snake(snake):
    for piece in snake:
        piece.forward(20)



screen.listen()
# screen.onkey(partial(move_snake,snake), 'space')

screen.exitonclick()

