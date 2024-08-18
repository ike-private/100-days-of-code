from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    q = Question(i['text'], i['answer'])
    question_bank.append(q)

quiz = QuizBrain(question_bank)


while quiz.still_has_question():
    quiz.next_question()

print(f"You have completed the quiz with a final score of {quiz.score}/{quiz.question_number}")