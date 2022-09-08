from tkinter import *

window = Tk()
window.config(width=300, height=400)

field_value = 1

label = Label()
label.config(text=f'Hello world!\n{field_value}', width=30, height=30)
label.grid(column=0, row=0)

def increase_counter():
    global field_value
    field_value += 1
    print(field_value)
    label.config(text=f'Hello world!\n{field_value}', width=30, height=30)
    label.grid()


def decrease_counter():
    global field_value
    field_value -= 1
    print(field_value)
    label.config(text=f'Hello world!\n{field_value}', width=30, height=30)
    label.grid()


button1 = Button(text='+', command=increase_counter)
button1.grid(column=0, row=1)

button2 = Button(text='-', command=decrease_counter)
button2.grid(column=1, row=1)

# the line that's always at the end of a file
window.mainloop()