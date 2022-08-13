print('Welcome to the tip calculator.')
total_bill = float(input('What was the total bill? $'))
tip = float(input('What percentage tip would you like to give? 10, 12 or 15? '))
head_count = float(input('How many people to split the bill? '))

per_capita = round(((total_bill * (1 + tip/100)) / head_count), 2)

print(f'Each person should pay: ${per_capita:.2f}')