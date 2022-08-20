import random
import sys
from art import logo, vs
from game_data import data

def game_over(player_score):
    print(f'You\'re wrong! Your final score is {player_score}.')
    sys.exit()

def player_wins(player_score):
    player_score +=1
    print(f'You\'re right! Current score: {player_score}')
    return player_score

player_score = 0
data_len = len(data)

print(logo)

while True:
    pick_one = data[random.randint(0,data_len)]
    pick_two = data[random.randint(0,data_len)]
    
    print(f'Compare A: {pick_one["name"]}, {pick_one["description"]}, from {pick_one["country"]}')
    print(vs)
    print(f'Compare B: {pick_two["name"]}, {pick_two["description"]}, from {pick_two["country"]}')

    guess = input('Who has more followers? Type \'A\' or \'B\': ')

    if guess == 'A':
        if pick_one['follower_count'] > pick_two['follower_count']:
            player_score = player_wins(player_score)
        else:
            game_over(player_score)
    elif guess == 'B':
        if pick_one['follower_count'] < pick_two['follower_count']:
            player_score = player_wins(player_score)
        else:
            game_over(player_score)

