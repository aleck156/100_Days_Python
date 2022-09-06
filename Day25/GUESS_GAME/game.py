import time
from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.bgpic('./us-states-game-start/blank_states_img.gif')


screen.tracer(0)

screen.listen()
screen.onkey(screen.bye, 'space')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
