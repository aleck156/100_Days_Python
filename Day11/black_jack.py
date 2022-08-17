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
import sys
from traceback import print_tb
from art import logo

player_hand = []
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

player_choice = 'y'

def init(player, computer):
    player.append(pick_card())
    player.append(pick_card())
    computer.append(pick_card())
    computer.append(pick_card())
    print(f'Your current hand is {player} and score {count_score(player)}')
    print(f'Computer hand is {computer} and score {count_score(computer)}')

init(player_hand, computer_hand)

while player_choice == 'y':
    player_choice = input('Do you want to pick a card [y/n]? ')
    if player_choice == 'y':
        computer_hand.append(pick_card())
        computer_score = count_score(computer_hand)
        print(f'Computer score is {computer_score}')
        if computer_score > 21:
            print(f'You have won the game! Computer score is {computer_score}, your score is {player_score}.')
            break
        player_hand.append(pick_card())
        player_score = count_score(player_hand)
        print(f'Your current hand is {player_hand} and score {player_score}')
        if player_score > 21:
            print(F'You have lost the game! Computer score is {computer_score}, your score is {player_score}.')
            break
        
    elif player_choice == 'n':
        computer_score = count_score(computer_hand)
        player_score = count_score(player_hand)
        if computer_score > player_score:
            print(F'You have lost the game! Computer score is {computer_score}, your score is {player_score}.')
        elif computer_score < player_score:
            print(f'You have won the game! Computer score is {computer_score}, your score is {player_score}.')
        else:
            print(f'It\'s a tie!')            
        print(f'Your final score is {count_score(player_hand)}')

print(f'Randomized computer cards: {computer_hand} -> {count_score(computer_hand)}')