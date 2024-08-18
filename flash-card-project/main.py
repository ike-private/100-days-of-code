from tkinter import *

import pandas
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
try:
    file = "data/words_to_learn.csv"
    df = pd.read_csv(file)
except FileNotFoundError:
    file = "data/french_words.csv"
    df = pd.read_csv(file)

to_learn = df.to_dict(orient="records")
random_word = {}

def read_data():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(to_learn)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=random_word["French"], fill="black")
    canvas.itemconfig(front, image=front_img)
    flip_timer = window.after(3000, func=show_translation)

def correct():
    to_learn.remove(random_word)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    read_data()
def show_translation():
    canvas.itemconfig(front, image=back_img)
    canvas.itemconfig(language, fill="white", text="English")
    canvas.itemconfig(word, fill="white", text= random_word["English"])

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=show_translation)

canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
front = canvas.create_image(400, 263, image=front_img)


language = canvas.create_text(400,150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400,263, text="", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)


cross_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_img, highlightthickness=0, command=read_data)
unknown_button.grid(column=0, row=1)

check_img = PhotoImage(file="images/right.png")
right_button = Button(image=check_img, highlightthickness=0, command=read_data and correct)
right_button.grid(column=1, row=1)
read_data()

window.mainloop()
