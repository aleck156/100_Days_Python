from turtle import Turtle as t, Screen as s
from functools import partial

timmy = t()
screen = s()

def move_forward(turtle):
    turtle.forward(100)

def move_backward(turtle):
    turtle.forward(-100)

def turn_left(turtle):
    turtle.left(90)

def turn_right(turtle):
    turtle.left(-90)

screen.listen()
screen.onkey(partial(move_forward, timmy), 'Up')
screen.onkey(partial(move_backward, timmy), 'Down')
screen.onkey(partial(turn_left, timmy), 'Left')
screen.onkey(partial(turn_right, timmy), 'Right')

screen.exitonclick()