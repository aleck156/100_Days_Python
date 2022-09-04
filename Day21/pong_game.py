import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title('Ping-Pong game')

l_paddle = Paddle(-SCREEN_WIDTH/2 + 40, 40)
r_paddle = Paddle(SCREEN_WIDTH/2 - 40, 40)

ball = Ball()

scoreboard = Scoreboard(SCREEN_WIDTH, SCREEN_HEIGHT)

screen.tracer(0)

screen.listen()
screen.onkey(screen.bye, 'space')
screen.onkey(l_paddle.move_up, 'w')
screen.onkey(l_paddle.move_down, 's')
screen.onkey(r_paddle.move_up, 'Up')
screen.onkey(r_paddle.move_down, 'Down')

game_is_on = True
while game_is_on:
    time.sleep(0.001)
    screen.update()
    ball.move()

    if ball.ycor() > SCREEN_HEIGHT / 2 - 20 or ball.ycor() < -SCREEN_HEIGHT / 2 + 20:
        ball.bounce_y()

    if ball.xcor() > SCREEN_HEIGHT / 2 - 20 and ball.distance(r_paddle.pos()) < 50:
        ball.bounce_x()

    if ball.xcor() < -SCREEN_HEIGHT / 2 + 20 and ball.distance(l_paddle.pos()) < 50:
        ball.bounce_x()

    if ball.xcor() > SCREEN_WIDTH / 2:
        ball.reset_position()

    if ball.xcor() < -SCREEN_WIDTH / 2:
        ball.reset_position()

    # if ball.xcor() > SCREEN_HEIGHT / 2 - 50 or ball.xcor() < -SCREEN_HEIGHT / 2 + 50:
    #     if ball.distance(r_paddle.pos()) > 40 and ball.distance(l_paddle.pos()) > 40:
    #         print('GAME OVER')


# screen.onkey(screen.exitonclick, 'space')