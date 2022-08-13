print("Welcome to the rollercoaster!")
height = int(input('What is your height in cm? '))
age = int(input('Waht is your age in years? '))
bill = 0;

if height >= 120:
  if age > 18:
    bill = 18
  elif age > 12 and age <=18 :
    bill = 9
  else:
    bill = 6
  print('Enjoy the ride!')

  wants_photo = input("Do you want ta photo taken? [Y/N]:")
  if wants_photo:
    bill += 3


else:
  print('Sorry, your password is not long enough!')

print(f'The ticket is ${bill}')