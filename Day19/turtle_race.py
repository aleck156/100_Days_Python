from turtle import Turtle as t, Screen as s
import random

timmy = t()
sc = s()
sc_w = 800
sc_h = 600
user_bet=1

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def init_game(turtle, screen, width, height):
    turtle.shape('turtle')
    user_pick = int(screen.numinput(title="Turtle Race",prompt='Which turtle will win? [1-6]: '))
    screen.colormode(255)
    screen.setup(width=width, height=height)
    return user_pick

def setup_turtles(width, height):
    turtle_race = []
    for index in range(0,6):
        new_turtle = t()
        new_turtle.shape('turtle')
        new_turtle.color(random_color())
        new_turtle.penup()
        new_turtle.goto(- width /2 + 10 , -height / 4 + height * 0.1 * index)
        new_turtle.pendown()
        turtle_race.append(new_turtle)
    return turtle_race


user_bet = init_game(timmy, sc, sc_w, sc_h)
setup_turtles(sc_w, sc_h)



sc.exitonclick()