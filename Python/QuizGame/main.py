from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_questions():
    q_input = quiz_brain.next_question()

print("You have completed the quiz")
print(f"Your final score is {quiz_brain.score} out of {quiz_brain.question_number}")