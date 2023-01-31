import time
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz=quiz_brain
        self.window= Tk()
        self.window.title('QuizApp')
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)

        self.score_label=Label(text='Score: 0', fg='white', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150,
                                                     150,
                                                     text='Some question text',
                                                     font=('Arial', 20, 'italic'),
                                                     width=250
                                                     )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        my_image_right = PhotoImage(file="images/true.png")
        self.right_button = Button(image=my_image_right, highlightthickness=0, command=self.true_press)
        self.right_button.grid(column=0, row=3)
        self.right_button.config(padx=10, pady=10)

        my_image_wrong = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=my_image_wrong, highlightthickness=0, command=self.false_press)
        self.wrong_button.grid(column=1, row=3)
        self.wrong_button.config(padx=50, pady=50)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='You have reached the end of the quiz')
            self.right_button.config(state='disabled')
            self.wrong_button.config(state='disabled')


    def true_press(self):
        is_right=self.quiz.check_answer('True')
        self.give_feedback(is_right)


    def false_press(self):
        is_right=self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
