import tkinter
from tkinter import *


THEME_COLOR = "#375362"
FONT_CONFIG = ('Arial', 20, 'italic')

class QuizzInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        # row 1
        self.score_label = tkinter.Label(text=f'Score: {0}', fg='white', bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        # row 2
        self.canvas = tkinter.Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            (150,125),
            text='testing',
            fill=THEME_COLOR,
            justify='center',
            font=FONT_CONFIG
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # row 3
        self.true_image = PhotoImage(file="./images/true.png")
        self.true_button = tkinter.Button(image=self.true_image, highlightthickness=0)
        self.true_button.grid(row=2, column=0)

        self.false_image = PhotoImage(file="./images/false.png")
        self.false_button = tkinter.Button(image=self.false_image, highlightthickness=0)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()