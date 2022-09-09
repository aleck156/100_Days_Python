from tkinter import *



# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro App!')
window.config(padx=10, pady=10, bg=PINK)

canvas = Canvas(width=250, height=250, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file='./tomato.png')
canvas.create_image(125, 125, image=image)
canvas.create_text(125, 125, text='25:00', font=(FONT_NAME, 20, 'bold'), fill='white')
canvas.grid(column=0, row=0, columnspan=2)

# create 1 text display


# create 2 buttons - start, stop
# add 2 methods
button_left = Button()
button_left.config(text='Start')
button_left.grid(column=0, row=1)

button_right = Button()
button_right.config(text='Stop')
button_right.grid(column=1, row=1)


# window.minsize(width=400, height=600)
# window.grid()


window.mainloop()