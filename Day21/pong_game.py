from turtle import Turtle, Screen

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 1200

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

screen.listen()
screen.onkey(screen.exitonclick, 'space')