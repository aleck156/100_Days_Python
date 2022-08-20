import os
import random
import sys
from art import logo, vs
from game_data import data

def game_over(player_score):
    print(f'You\'re wrong! Your final score is {player_score}.')
    sys.exit()

def pick_random(data, data_len):
    pick_a = data[random.randint(0,data_len)]
    pick_b = data[random.randint(0,data_len)]
    return pick_a, pick_b

def display_choices(pick_a, pick_b):
    print(f'Compare A: {pick_a["name"]}, {pick_a["description"]}, from {pick_a["country"]}')
    print(vs)
    print(f'Compare B: {pick_b["name"]}, {pick_b["description"]}, from {pick_b["country"]}')

def check_answer(guess, followers_a, followers_b):
    if followers_a > followers_b:
        return guess == 'a'
    if followers_a < followers_b:
        return guess == 'b'

def compare_picks(guess, followers_a, followers_b, player_score):
    if check_answer(guess, followers_a, followers_b):
        return player_score + 1
    else:
        game_over(player_score)

def init_loop(score):
    os.system('clear')
    print(logo)
    print(f'You\'re right! Current score: {score}')

player_score = 0
data_len = len(data)

while True:
    init_loop(player_score)
    pick_one, pick_two = pick_random(data, data_len)

    display_choices(pick_one, pick_two)
    
    guess = input('Who has more followers? Type \'A\' or \'B\': ').lower()

    player_score = compare_picks(guess, pick_one["follower_count"], pick_two["follower_count"], player_score)
