import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 1200

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title('Ping-Pong game')

l_paddle = Paddle(-SCREEN_WIDTH/2 + 40 , 40)
r_paddle = Paddle(SCREEN_WIDTH/2 - 40 , 40)
ball = Ball()

screen.tracer(0)

screen.listen()
screen.onkey(screen.bye, 'space')
screen.onkey(l_paddle.move_up, 'Up')
screen.onkey(l_paddle.move_down, 'Down')
screen.onkey(r_paddle.move_up, 'w')
screen.onkey(r_paddle.move_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(0.001)
    screen.update()
    ball.move()


# screen.onkey(screen.exitonclick, 'space')