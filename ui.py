THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain


class UserInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.screen = Tk()
        self.score = 0
        self.screen.title("Quizzler")
        self.screen.config(padx=20, pady=20, height=600, width=400, bg=THEME_COLOR)
        self.label_1 = Label(text=f"Score : {self.score}", fg="white")
        self.label_1.config(bg=THEME_COLOR)
        self.label_1.grid(row=0, column=1)
        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=285, text="Hello world", fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        img = PhotoImage(file="images/false.png")
        self.button = Button(image=img, highlightthickness=0, command=self.is_wrong)
        self.button.grid(row=2, column=0)
        img_2 = PhotoImage(file="images/true.png")
        self.button_2 = Button(image=img_2, highlightthickness=0, command=self.is_right)
        self.button_2.grid(row=2, column=1)
        self.next()
        self.screen.mainloop()

    def next(self):
        self.canvas.config(bg="white")
        text = self.quiz.next_question()
        self.label_1.config(text=f"Score : {self.quiz.score}")
        self.canvas.itemconfig(self.question_text, text=text)

    def is_right(self):
        self.feedback(self.quiz.check_answer("True"))

    def is_wrong(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.screen.after(1000, self.next)
