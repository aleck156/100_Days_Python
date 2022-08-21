# Day 15 is all about configuring IDE environment
# Chose to go with PyCharm Community Edition
# ...
#

from menu import MENU, resources

budget = 0.00

def print_resources(res):
    print(f'Resource left:')
    for elem in res:
        print(f'{elem:8s}{res[elem]}')

# print_resources(resources)

def charge_money(coffee_cost):
    """
    Charge user money for the coffee
    Args:
        coffee_cost:

    Returns:
        True - once all the price is paid
        False - when the inserted coins are not enough
    """
    print(f'Please insert coins [quarters/dimes/nickles/pennies]')
    quarters = int(input('How many quarters: '))
    dimes = int(input('How many dimes: '))
    nickles = int(input('How many nickles: '))
    pennies = int(input('How many pennies: '))
    income = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    if income > coffee_cost:
        print(f'Here\'s your ${(income - coffee_cost):.2f} charge')
        return True
    elif income == coffee_cost:
        print('Thank you for purchasing our coffee!')
        return True
    else:
        print('I\'ts not enough ... Money refunded')
        return False
    pass

def update_resources(resource, ingredients):
    """
    Update resources available for future coffee
    Args:
        resource:       resources available for making any kind of coffee
        ingredients:    what it takes to make that coffee

    Returns:
        True if resources were updated
        False if there was not enough resources to make that coffee
    """
    for key in ingredients:
        if ingredients[key] > resource[key]:
            print(f'Sorry, not enough {key}.')
            return False
    for key in ingredients:
        resource[key] -= ingredients[key]


def make_coffee(coffee_type, resource, price):
    """
    Make the coffee, but only when the resources are available
    Args:
        coffee_type:
        resource:
        price:

    Returns:

    """
    if not update_resources(resource, coffee_type['ingredients']):
        while not charge_money(coffee_type['cost']):
            pass
        price += coffee_type['cost']
        print(f'Your coffee is completed! Thanks!')
        print(coffee_type)
        print_resources(resources)

loop_status = True
user_choice = ''
while loop_status:
    user_choice = input('What would you like? [espresso/latte/cappuccino/report/q]: ').lower()[:1]
    if user_choice == 'r':
        print_resources(resources)
        print(f'Thank you for visiting our coffee shop! Have a nice day!')
    elif user_choice == 'e':
        make_coffee(MENU['espresso'], resources, budget)
    elif user_choice == 'l':
        make_coffee(MENU['latte'], resources, budget)
    elif user_choice == 'c':
        make_coffee(MENU['latte'], resources, budget)
    else:
        print(f'See you next time!')
        loop_status = False

# check whether resources are sufficient for the order a user wants to drink
    # def check_resources(ingredients, resources)
# get the money - pick coins - pennies, nickels, dimes, quarters
    # cost - does the entered amount equals to price?

# do you want to make a coffee?
    # select your coffee
    # verify resources
    #    yes -> make it -> charge for it -> go back to the main loop
    #    no -> go back to the main loop
# start making the coffee only after the payment is done
