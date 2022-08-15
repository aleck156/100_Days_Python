programming_dictionary = {
    "Bug":
      "An error in a program that prevents the program from running as expected.",
    "Function": 
      "A piece of code that you can easily call over and over again."
}

programming_dictionary['Loop'] = 'The Action of doing something over and over again. Conditions can be specified ahead of time (for Loop) or on each iteration (while)'

# creating an empty dictionary
empty_dictionary = {}

# wiping out an existing dictionary
# programming_dictionary = {}

# edit an item in a dictionary
programming_dictionary['Bug'] = ''

for k in programming_dictionary:
  print(f'{k}: {programming_dictionary[k]}')