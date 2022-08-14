# arguments is what you throw at function calls, an actual piece of data that is being passed over

# parameters is wht functions are defined with to handle

from sys import exit
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

print(direction, text, shift)

def text_modification(text, shift, direction):
    text_encoded = []
    alphabet_length = len(alphabet)
    for letter in text:
        try:
            position = alphabet.index(letter)
        except ValueError:
            print(f'The sign [{letter}] is not in alphabet. Aborting ...')
            exit()

        if direction:
            new_position = position + shift        
            if (new_position >= alphabet_length):
                new_position -= alphabet_length
        else:
            new_position = position - shift        
            if (new_position < 0):
                new_position += alphabet_length
        text_encoded.append(alphabet[new_position])

    return ''.join(text_encoded)

def encrypt(text, shift):
    print(f'You have chosen to encode the text')
    print(f'Original:\t{text}')
    print(f'Shift:\t\t{shift}')
    print(f'Encoded:\t{text_modification(text, shift, True)}')


def decrypt(text, shift):
    print(f'You have chosen to decode the text')
    print(f'Original:\t{text}')
    print(f'Shift:\t\t{shift}')
    print(f'Decoded:\t{text_modification(text, shift, False)}')

if direction in ['encode', 'e']:
    encrypt(text, shift)
elif direction in ['decode', 'd']:
    decrypt(text, shift)
else:
    print('Wrong direction. Please choose [encode/e/decode/d] next time')

