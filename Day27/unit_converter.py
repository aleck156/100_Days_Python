from tkinter import *

window = Tk()
window.title('Miles to km/h converter')
window.minsize(width=100, height=200)
window.config(padx=20, pady=20)

def convert_unit():
    user_value = float(input_field.get())
    label3.config(text=f'{user_value * 1.609344:.2f}')
    label3.grid(column=1, row=1)

# row 1
input_field = Entry(width=10, justify='center')
input_field.config()
input_field.grid(column=1, row=0)

label1 = Label(text='Miles')
label1.grid(column=2, row=0)

# row 2
label2 = Label(text='is equal to')
label2.grid(column=0, row=1)

label3 = Label(text='0')
label3.grid(column=1, row=1)

label4 = Label(text='km')
label4.grid(column=2, row=1)

# row 3
button = Button(text='Calculate', command=convert_unit)
button.grid(column=1, row=2)

window.mainloop()