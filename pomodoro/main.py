from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    heading.config(text="Timer")
    tick.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
work_secs = WORK_MIN * 60
short_break_secs = SHORT_BREAK_MIN * 60
long_break_secs = LONG_BREAK_MIN * 60


def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(long_break_secs)
        heading.config(fg=RED, text="Long break")
    elif reps % 2 == 0:
        count_down(short_break_secs)
        heading.config(fg=PINK, text="Short break")
    else:
        heading.config(fg=GREEN, text="Work")
        count_down(work_secs)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
import time


def count_down(count):
    check = []
    count_minute = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            check.append("✓")
        tick.config(text=check)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

heading = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
heading.grid(column=1, row=0)

start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

tick = Label(fg=GREEN, bg=YELLOW)
tick.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
