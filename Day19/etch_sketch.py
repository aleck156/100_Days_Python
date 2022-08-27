from turtle import Turtle as t, Screen as s
from functools import partial

timmy = t()
screen = s()

def move_forward(turtle):
    turtle.forward(100)

screen.listen()
screen.onkey(partial(move_forward, timmy), 'u')
screen.exitonclick()