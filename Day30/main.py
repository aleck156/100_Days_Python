try:
    file = open('a_file.txt')
    a_dictionary = {'key': 'value'}
    print(a_dictionary['asdasd'])
except FileNotFoundError:
    file = open('a_file.txt', mode='w')
    file.write('Hello world!')
except KeyError as error_message:
    print(f'The key {error_message} does not exist')
else:
    context = file.read()
    print(context)
finally:
    file.close()
    print('file was closed')