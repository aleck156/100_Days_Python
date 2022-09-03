import time
from turtle import Turtle, Screen
from paddle import Paddle

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 1200

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title('Ping-Pong game')

paddle = Paddle()

screen.tracer(0)

screen.listen()
screen.onkey(screen.bye, 'space')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)


# screen.onkey(screen.exitonclick, 'space')