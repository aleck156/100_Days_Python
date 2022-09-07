from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.bgpic(image)
# screen.addshape(image)
# turtle.shape(image)
screen.setup(width=725, height=491)

states_coord = pandas.read_csv('50_states.csv')
states_coord_len = len(states_coord)
score = 0

game_is_on = True
while score < states_coord_len and game_is_on:
    answer_state = screen.textinput\
    (
        title=f'{score}/{states_coord_len} Guess the State',
        prompt="What's another state's name"
    ).title()
    if answer_state.lower() in ['q', 'quit', 'e', 'exit']:
        game_is_on = False
    else:
        position = states_coord[states_coord.state == answer_state]
        if not position.empty:
            new_turtle = Turtle()
            new_turtle.penup()
            new_turtle.goto(x=position['x'].values[0], y=position['y'].values[0])
            new_turtle.write(f'{answer_state}',align='center', font=('Arial', 10, 'normal'))
            new_turtle.hideturtle()
            score += 1
        else:
            print(f'There\'s no such state like {answer_state}')

