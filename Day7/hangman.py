import random
import os
from hangman_art import stages, logo
from hangman_words import word_list

password = word_list[random.randint(0,len(word_list)-1)]
password_len = len(password)
hidden_word = ["_" for x in range(0,password_len)]
failed_letters = []

lives = len(stages) - 1

print(logo)

while lives > 0 and ('_' in hidden_word):
  print(stages[lives])
  print(f'Lives left: {lives}')
  print(f'Failed letters: {failed_letters}')
  print('Guess word: ' + ''.join(hidden_word))

  guess = input('Guess a letter: ').lower()

  if guess not in password:
    lives -= 1
    if guess not in failed_letters:
      failed_letters.append(guess)

  elif guess in hidden_word:
    print(f'You have already entered the letter: {guess}')

  else:
    for index, letter in enumerate(password):
      if guess == letter:
        hidden_word[index] = guess

  os.system('clear')

if ''.join(hidden_word) == password and lives > 0:
  print('You have won!')

if lives == 0:
  print(stages[0])
  print('You have lost the game!')
  print(f'The hidden word was: {password}')


'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
----------
'''