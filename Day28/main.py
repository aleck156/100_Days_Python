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

TICK_SYMBOL = '✔'
TICK_COUNT = 7

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro App!')
window.config(padx=10, pady=10, bg=YELLOW)

canvas = Canvas(width=350, height=350, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file='./tomato.png')
canvas.create_image(175, 175, image=image)
canvas.create_text(175, 200, text='25:00', font=(FONT_NAME, 20, 'bold'), fill='white')
canvas.grid(column=0, row=1, columnspan=3)

# create 1 text display on top
top_label = Label()
top_label.config(text='TIMER', font=(FONT_NAME, 20, 'bold'), bg=YELLOW)
top_label.grid(column=0, row=0, columnspan=3)


# create 2 buttons - start, stop
# add 2 methods
button_left = Button()
button_left.config(text='Start', font=(FONT_NAME, 15, 'bold'), bg=YELLOW)
button_left.grid(column=0, row=2)

button_right = Button()
button_right.config(text='Stop', font=(FONT_NAME, 15, 'bold'), bg=YELLOW)
button_right.grid(column=2, row=2)

# bottom tick
text = Label()
current_ticks = ''.join([TICK_SYMBOL for _ in range(0, TICK_COUNT)])
text.config(text=current_ticks, font=(FONT_NAME, 12, 'bold'), bg=YELLOW)
text.grid(column=1, row=3)


# window.minsize(width=400, height=600)
# window.grid()


window.mainloop()