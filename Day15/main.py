# Day 15 is all about configuring IDE environment
# Chose to go with PyCharm Community Edition
# ...
#
import sys

from menu import MENU, resources

income = 0.00

def print_resources(res):
    print(f'Resource left:')
    for elem in res:
        print(f'{elem:8s}{res[elem]}')

print_resources(resources)

loop_status = True
user_choice = ''
while loop_status:
    user_choice = input('What would you like? [espresso/latte/cappuccino/report]: ').lower()[:1]
    if user_choice == 'r':
        print_resources(resources)
        print(f'Thank you for visiting our coffee shop! Have a nice day!')
    if user_choice == 'e':
        pass
    if user_choice == 'l':
        pass
    if user_choice == 'c':
        pass

# check whether resourcs are sufficient for the order an user wants to drink
    # def check_resources(ingredients, resources)
# get the money - pick coins - pennies, nickels, dimes, quarters
    # cost - does the entered amount equals to price?

# do you want to make a coffee?
    # select your coffee
    # verify resources
    #    yes -> make it -> charge for it -> go back to the main loop
    #    no -> go back to the main loop
# start making the coffee only after the payment is done