import time
from turtle import Turtle, Screen
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard

speed = 10
screen = Screen()

snake = Snake(3)

screen.tracer(0)
screen.update()

screen.setup(width=1600, height=1200)
screen.title('Welcome to the SNAKE GAME')
screen.bgcolor('black')
screen.colormode(255)

snake.move(screen, speed)



screen.listen()
# screen.onkey(partial(move_snake,snake), 'space')

screen.exitonclick()

