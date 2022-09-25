import tkinter
from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
FONT_CONFIG = ('Arial', 20, 'italic')

class QuizzInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
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
            font=FONT_CONFIG,
            width=250
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # row 3
        self.true_image = PhotoImage(file="./images/true.png")
        self.true_button = tkinter.Button(
            image=self.true_image,
            highlightthickness=0,
            command=self.true_pressed
        )
        self.true_button.grid(row=2, column=0)

        self.false_image = PhotoImage(file="./images/false.png")
        self.false_button = tkinter.Button(
            image=self.false_image,
            highlightthickness=0,
            command=self.false_pressed
        )
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)

    def get_next_question(self):
        self.canvas.config(bg='white')
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)