## Rules
# there are no jokers
# the jack/queen/king count as 10
# The Ace can count as either 11 or 1
# The cards in the deck list have equal probability of being drawn
# The omputer is the dealer
# cards are not removed from the deck
# computer picks cards until it gets score over 17

## The code
import random
from art import logo

player_hand = [7, 4, 11]
computer_hand = []
deck = [3,4,5,6,7,8,9,10,10,10,11]

def count_score(card_list):
    score = 0
    aces_count = 0
    for card in card_list:
        if card == 11:
            aces_count += 1
            score += 11
        else:
            score += card
        if score > 21 and aces_count >0:
            score -= 10
            aces_count -= 1
    return score

def pick_card():
    return deck[random.randint(0,len(deck)-1)]

print(logo)

print(f'{player_hand} -> {count_score(player_hand)}')

while count_score(computer_hand) <= 17:
    computer_hand.append(pick_card())

print(f'Randomized computer cards: {computer_hand} -> {count_score(computer_hand)}')