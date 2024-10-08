class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        q = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f" Q.{self.question_number}: {q.text} (True or False)?: ")
        self.check_answer(user_answer, q.answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self ,user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct Answer! ")
            self.score += 1
        else:
            print("Wrong Answer!")
        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number} \n")