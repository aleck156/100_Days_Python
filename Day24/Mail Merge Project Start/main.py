#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('./Input/Letters/starting_letter.txt') as starting_letter:
    letter_template = starting_letter.read()

# print(letter_template)

with open('./Input/Names/invited_names.txt') as names:
    names = names.read().split('\n')
    for name in names:
        new_letter = letter_template.replace('[name]', name)
        # save the new template
        with open(f'./Output/ReadyToSend/{name}', mode='w') as output_file:
            output_file.write(new_letter)