from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[Question(question_data[i]['question'], question_data[i]['correct_answer']) for i in range(0,len(question_data))]

quiz=QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

quiz.end_game()