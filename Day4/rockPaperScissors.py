import random
import sys

def print_rock():
  print("""
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
  """)

# Paper
def print_paper():
  print("""
      _______
  ---'    ____)____
            ______)
            _______)
          _______)
  ---.__________)
  """)

# Scissors
def print_scissors():
  print("""
      _______
  ---'   ____)____
            ______)
        __________)
        (____)
  ---.__(___)
  """)

def print_choice(choice):
  if (choice > 2 or choice < 0):
    print('Index out of bound, you lose!')
    sys.exit()

  if choice == 0:
    print_rock()
  elif choice == 1:
    print_paper()
  else:
    print_scissors() 

message = {
  -1: 'You have lost the game!',
  0 : 'It\'s a draw!',
  1 : 'You have won the game! Congratulations!'
} 

def print_message(message):
  print(message)
  sys.exit()

machine0 = [0, -1, 1]
machine1 = [1, 0, -1]
machine2 = [-1, 1, 0]
user = [machine0, machine1, machine2]

print('0 - ROCK // 1 - PAPER // 2 - SCISSORS')
player_choice = int(input('What do you choose? '))
print(f'Your choice is {player_choice}')
print_choice(player_choice)

computer_choice = random.randint(0,2)
print(f'Computer choice: {computer_choice}')
print_choice(computer_choice)

print_message(message[user[player_choice][computer_choice]])





# def determine_results(player,computer):
#   if player == 0:
#     if computer == 0:
#       draw()
#     if computer == 1:
#       game_lost()
#     if computer == 2:
#       game_won()

#   if player == 1:
#     if computer == 0:
#       game_won()
#     if computer == 1:
#       draw()
#     if computer == 2:
#       game_lost()

#   if player == 2:
#     if computer == 0:
#       game_lost()
#     if computer == 1:
#       game_won()
#     if computer == 2:
#       draw()

# determine_results(player_choice, computer_choice)
