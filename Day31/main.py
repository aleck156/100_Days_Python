from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

NEGATIVE = "❌"
POSITIVE = "✅"

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.minsize(height=400, width=600)

# ROW 1

# ROW 2
correct_image = PhotoImage(file='./images/right.png')
right_button = Button(image=correct_image, highlightthickness=0, justify='center')
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file='./images/wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0, justify='center')
wrong_button.grid(column=0, row=1)


window.mainloop()