import random
from turtle import Turtle as t, Screen as s
from functools import partial

timmy = t()
timmy.pensize(10)
timmy.shapesize(stretch_wid=2.5, stretch_len=2.5, outline=None)


screen = s()
screen.colormode(255)

def move_forward(turtle):
    turtle.forward(100)

def move_backward(turtle):
    turtle.forward(-100)

def turn_left(turtle):
    turtle.left(90)

def turn_right(turtle):
    turtle.left(-90)

def change_color(turtle, sc):
    print('Changing color')
    turtle.pencolor((random.randint(0,255), random.randint(0,255), random.randint(0,255)))

screen.listen()
screen.onkey(partial(move_forward, timmy), 'Up')
screen.onkey(partial(move_backward, timmy), 'Down')
screen.onkey(partial(turn_left, timmy), 'Left')
screen.onkey(partial(turn_right, timmy), 'Right')
screen.onkey(partial(change_color, timmy, screen), 'space')


screen.exitonclick()