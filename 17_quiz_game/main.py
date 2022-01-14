from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
    fqb = Question(text=q["question"], answer=q["correct_answer"])
    question_bank.append(fqb)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz! Your final score is {quiz.score} out of {len(quiz.question_list)}.")