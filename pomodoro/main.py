from tkinter import *
import math
from plyer import notification

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
    global reps
    reps = 1


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    match reps:
        case 1 | 3 | 5 | 7:
            count_down(work_sec)
            title_label.config(text="Working Time", fg=PINK)
            reps += 1
            notification.notify(title='Pomodoro', message="Let's working", app_icon='Tomato.ico')

        case 2 | 4 | 6:
            count_down(short_break_sec)
            title_label.config(text="Break Time", fg=GREEN)
            reps += 1
            notification.notify(title='Pomodoro', message='Take a break time', app_icon='Tomato.ico')

        case 8:
            count_down(long_break_sec)
            title_label.config(text="LONG REST TIME", fg=GREEN)
            reps = 1
            notification.notify(title='Pomodoro', message='Take a Long break time', app_icon='Tomato.ico')


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_min < 10:
        count_min = f'0{count_min}'
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text='Start', highlightthickness=0, border=0.1, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', highlightthickness=0, border=0.1, command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(text='✔', fg=GREEN)
check_mark.grid(column=1, row=3)

window.mainloop()
