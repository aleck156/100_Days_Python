from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

NEGATIVE = "❌"
POSITIVE = "✅"

words = pandas.read_csv('./data/french_words.csv')
to_learn = words.to_dict(orient='records')
current_card = {}

def flip_card():
    canvas.itemconfig(canvas_bg_image, image=card_back_image)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')


def next_card():
    global flip_timer, current_card
    current_card = random.choice(to_learn)
    print(current_card['French'])
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_card['French'], fill='black')
    canvas.itemconfig(canvas_bg_image, image=card_front_image)
    flip_timer = window.after(3000, flip_card)

def is_known():
    to_learn.remove(current_card)
    next_card()

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.minsize(height=400, width=600)
window.title('FlashCard')
flip_timer = window.after(0, flip_card)

# ROW 1
# use canvas to layer things on top of each other
canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file='./images/card_front.png')
card_back_image = PhotoImage(file='./images/card_back.png')
canvas_bg_image = canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

card_title = canvas.create_text(
    400, 150,
    text='hello world',
    justify='center',
    font=('Arial', 20, 'bold')
)


card_word = canvas.create_text(
    400, 263,
    text='main text',
    justify='center',
    font=('Arial', 30, 'italic')
)

next_card()

# ROW 2
correct_image = PhotoImage(file='./images/right.png')
right_button = Button(image=correct_image, highlightthickness=0, justify='center', command=is_known)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file='./images/wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0, justify='center', command=next_card)
wrong_button.grid(column=0, row=1)


window.mainloop()