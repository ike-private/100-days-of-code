from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=250, height=300, bg="White")
        self.question = self.canvas.create_text(130, 150, width=200,
                                                text="Quiz Question",
                                                font=("Arial", 20, "italic"),
                                                fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        true = PhotoImage(file="images/true.png")
        self.true = Button(image=true, highlightthickness=0, command=self.answer_true)
        self.true.grid(column=0, row=2)

        false = PhotoImage(file="images/false.png")
        self.false = Button(image=false, highlightthickness=0, command=self.answer_false)
        self.false.grid(column=1, row=2)

        self.score = Label(text="Score: 0 ", fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text = q_text)
            self.score.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question, text="End of quiz!")
            self.true.config(state="disabled")
            self.false.config(state="disabled")
    def answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg = "green")
        else:
            self.canvas.config(bg = "red")
        self.window.after(1000, self.get_next_question)

