from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_shop = CoffeeMaker()
coffeee_menu = Menu()
money_account = MoneyMachine()


make_coffee = True

while make_coffee:
    user_choice = input(f'What would you like to order? [{coffeee_menu.get_items()}report/quit]: ')[:1].lower()
    if user_choice == 'q':
        print('Thank you for visiting our coffee shop. See you next time!')
        make_coffee = False
    elif user_choice == 'r':
        money_account.report()
        coffee_shop.report()
    else:
        coffee_item = coffeee_menu.find_drink(user_choice)
        if coffee_item:
            if coffee_shop.is_resource_sufficient(coffee_item):
                while not money_account.make_payment(coffee_item.cost):
                    pass
                coffee_shop.make_coffee(coffee_item)