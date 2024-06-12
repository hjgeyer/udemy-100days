class QuizBrain:

    def __init__(self, question_list: list):
        self.question_number = 0
        self.question_list = question_list
        self.correct_answers = 0
        
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        current_answer = current_question.answer
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)? ").lower()
        self.check_answer(user_answer, current_answer)        
    
    def still_has_question(self):
        return (self.question_number < (len(self.question_list)))
    
    def check_answer(self, guess, answer):
        if guess == answer.lower():
            self.correct_answers += 1
            print('You answered correctly.')
        else:
            print("Your answer was wrong.")
        
        print(f"The answer to the question was {answer}")
        print(f"Your Score: {self.correct_answers} / {self.question_number}\n")