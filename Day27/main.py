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
button.place(x=100, y=50)

# Entry component
input = Entry(width=10)
input.pack()

# always the last line of code
window.mainloop()

"""
main layout managers
- Pack
- Place
    precise positioning
    provide (x,y) position
    (0,0) - top left corner
- Grid
    preferred way of working with layouts in Tk

without any of these layouts attached to a widget, it won't be generated on a canvas
you can't mix Grid and Pack in the same program

"""