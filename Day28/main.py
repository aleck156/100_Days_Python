from tkinter import *
import math
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
TICK_COUNT = 1

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global TICK_COUNT
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if TICK_COUNT % 8 == 0:
        count_down(long_break_sec)
        change_label('LONG BREAK', GREEN)
    elif TICK_COUNT % 2 != 0:
        count_down(work_sec)
        change_label('WORK', RED)
    elif TICK_COUNT % 2 == 0:
        count_down(short_break_sec)
        change_label('SHORT BREAK', PINK)

def change_label(text, color):
    global top_label
    top_label.config(text=text, fg=color)
    top_label.grid(column=0, row=0, columnspan=3)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global TICK_COUNT
    if count >= 0:
        minutes = math.floor(count / 60)
        seconds = count % 60
        canvas.itemconfig(timer_text,{'text': f'{minutes}:{seconds:02d}'})
        window.after(1000, count_down, count - 1)
    else:
        print('break!')
        TICK_COUNT += 1
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro App!')
window.config(padx=10, pady=10, bg=YELLOW)

# window.after(1000, count_down, WORK_MIN * 60)

canvas = Canvas(width=350, height=300, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file='./tomato.png')
canvas.create_image(175, 150, image=image)
timer_text = canvas.create_text(175, 175, text='25:00', font=(FONT_NAME, 20, 'bold'), fill='white')
canvas.grid(column=0, row=1, columnspan=3)

# create 1 text display on top
top_label = Label()
top_label.config(text='TIMER', font=(FONT_NAME, 20, 'bold'), bg=YELLOW)
top_label.grid(column=0, row=0, columnspan=3)

# buttons - start, stop
button_left = Button()
button_left.config(text='Start', font=(FONT_NAME, 15, 'bold'), bg=YELLOW, highlightthickness=0, command=start_timer)
button_left.grid(column=0, row=2)

button_right = Button()
button_right.config(text='Stop', font=(FONT_NAME, 15, 'bold'), bg=YELLOW)
button_right.grid(column=2, row=2)

# bottom tick
text = Label()
current_ticks = ''.join([TICK_SYMBOL for _ in range(0, math.floor(TICK_COUNT/2))])
text.config(text=current_ticks, font=(FONT_NAME, 25, 'bold'), bg=YELLOW, fg=GREEN)
text.grid(column=1, row=3)

# the end
window.mainloop()