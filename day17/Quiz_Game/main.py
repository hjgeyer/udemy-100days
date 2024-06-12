from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question['text'], question['answer']))

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_question():
    quiz_brain.next_question()

print("\nYou've completed the quiz.")
print(f"Your final score was:  {quiz_brain.correct_answers} / {quiz_brain.question_number}")