#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
import sys
from art import logo

answer = random.randint(1, 100)

print(logo)
print('Welcome to the guessing game')

def set_difficulty():
    """Select between easy and hard mode
    easy - 10 attemps
    hard - 5 attempts
    """
    difficulty = input(f'Choose a difficulty [easy/e/hard/h]: ')[:1].lower()
    if difficulty == 'e':
        return 10
    elif difficulty == 'h':
        return 5
    else:
        print("Could not determine ... choosing the hard way!")

def check_guess(guess):
    global answer
    global attempts_left
    if guess == answer:
        print(f'Your guess was correct! The answer was {guess}')
        sys.exit()
    elif guess > answer:
        print('Too high')
    elif guess < answer:
        print('Too low!')
    attempts_left -= 1

attempts_left = set_difficulty()

while attempts_left > 0:
    print(f'You have {attempts_left} attempts remaining to guess the number')
    guess = int(input('Make a guess: '))
    check_guess(guess)

print('Sorry, you run out of attempts left ...')
