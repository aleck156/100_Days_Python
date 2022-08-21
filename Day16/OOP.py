# import another_module
#
# print(another_module.another_variable)

from prettytable import PrettyTable

my_table = PrettyTable()
my_table.add_column('Pokemon name', ["Pikachu", "Squirtie", "Charmander"])
my_table.add_column("Type", ["Electric", "Water", "Fire"])
my_table.align = 'l'

print(my_table)