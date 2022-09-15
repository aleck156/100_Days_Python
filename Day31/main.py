from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

NEGATIVE = "❌"
POSITIVE = "✅"

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.minsize(height=400, width=600)
window.title('FlashCard')

# use canvas to layer things on top of each other
canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file='./images/card_front.png')
card_back_image = PhotoImage(file='./images/card_back.png')
canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

canvas.create_text(
    400, 150,
    text='hello world',
    justify='center',
    font=('Arial', 20, 'bold')
)


canvas.create_text(
    400, 263,
    text='main text',
    justify='center',
    font=('Arial', 30, 'italic')
)

# ROW 1

# ROW 2
correct_image = PhotoImage(file='./images/right.png')
right_button = Button(image=correct_image, highlightthickness=0, justify='center')
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file='./images/wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0, justify='center')
wrong_button.grid(column=0, row=1)


window.mainloop()