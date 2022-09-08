from tkinter import *

window = Tk()
window.title('My first GUI program')
window.minsize(width=800, height=600)

# labels
my_label = Label(text='I am the label!', font=('Arial', 28, 'bold'))
my_label.pack(side='left')

def button_clicked():
    print("I've got clicked!")
    my_label.config(text='and I\'ve got changed too!')
    my_label.pack()
    user_text = input.get()
    print(user_text)
    if user_text:
        my_label.config(text=f'Text: {user_text}')
        my_label.pack()


button = Button(text='click me!', command=button_clicked)
button.pack()

# Entry component
input = Entry(width=10)
input.pack()

# always the last line of code
window.mainloop()