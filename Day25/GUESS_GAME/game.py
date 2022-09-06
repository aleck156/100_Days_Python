import time
from turtle import Turtle, Screen
import pandas
from states import States

screen = Screen()
screen.title('U.S. States Game')
screen.bgpic('./us-states-game-start/blank_states_img.gif')
screen.setup(width=725, height=491)

states = States()

screen.tracer(0)

screen.listen()
screen.onkey(screen.exitonclick, 'space')

game_is_on = True
while game_is_on:
    user_input = screen.textinput(f'states correct', "What's another state name?")
    print(states.check_state(user_input)['x'])
    time.sleep(0.1)
    screen.update()
