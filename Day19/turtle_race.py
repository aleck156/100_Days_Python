from turtle import Turtle as t, Screen as s
import random
from functools import partial


sc = s()
sc_w = 800
sc_h = 600
user_bet=1

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def init_game(screen, width, height):
    screen.colormode(255)
    screen.setup(width=width, height=height)
    user_pick = int(screen.numinput(title="Turtle Race",prompt='Which turtle will win? [1-6]: '))
    return user_pick

def setup_turtles(width, height):
    turtles = []
    for index in range(0,6):
        new_turtle = t()
        new_turtle.shape('turtle')
        new_turtle.color(random_color())
        new_turtle.penup()
        new_turtle.goto(- width /2 + 10 , -height / 4 + height * 0.1 * index)
        new_turtle.pendown()
        turtles.append(new_turtle)
    return turtles

def detect_finish(turtles, screen):
    for index, turtle in enumerate(turtles):
        if turtle.xcor() >= screen.screensize()[0] - 25:
            return index
    return False

def start_race(turtles, screen, user_bet):
    # detect_finish(turtles, screen)
    while not detect_finish(turtles, screen):
        for turtle in turtles:
            turtle.forward(random.randint(0, 25))
    winner = detect_finish(turtles, screen) + 1
    print(f'The winner is turtle {winner}')
    print(f'Your bet was turtle {user_bet}')
    if winner == user_bet:
        print('YOU WIN')
    else:
        print('YOU LOSE!')


user_bet = init_game(sc, sc_w, sc_h)
turtles = setup_turtles(sc_w, sc_h)
sc.listen()
sc.onkey(partial(start_race, turtles, sc, user_bet), 'space')


sc.exitonclick()