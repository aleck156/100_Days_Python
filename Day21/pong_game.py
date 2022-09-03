import time
from turtle import Turtle, Screen
from paddle import Paddle

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 1200

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title('Ping-Pong game')

paddle = Paddle(-SCREEN_WIDTH/2 + 40 , 40)

screen.tracer(0)

screen.listen()
screen.onkey(screen.bye, 'space')
screen.onkey(paddle.move_up, 'Up')
screen.onkey(paddle.move_down, 'Down')

game_is_on = True
while game_is_on:
    time.sleep(0.001)
    screen.update()


# screen.onkey(screen.exitonclick, 'space')