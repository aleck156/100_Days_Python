from art import logo

print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return 0
    return n1 / n2

def get_first_number():
    return float(input('What\'s the first number?: '))

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def loop_choice():
    print('Choose \'y\' to continue with the current result')
    print('Choose \'n\' to start a new calculation')
    print('Choose \'q\' to end the program')
    return input('Your choice [y/n/q]: ')
    
def calculate_number(first_number, second_number, operation):
    return operations[operation](first_number, second_number)

user_choice = 'y'
first_number = get_first_number()
result = 0

while user_choice != 'q':
    operation = input('Pick an operation [+ - * /]: ')[:1]
    second_number = float(input('What\'s the second number?: '))
    result = calculate_number(first_number, second_number, operation)

    print(f'{first_number} {operation} {second_number} = {result}')
    user_choice = loop_choice()
    if user_choice == 'n':
        first_number = get_first_number()
    elif user_choice == 'y':
        first_number = result
        print(f'Current first number: {first_number}')
