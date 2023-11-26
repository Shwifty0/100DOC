from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random

question_bank = []
for i in range(len(question_data)):
    #question = question_data["results"][i]["question"]
    question = Question(question_data[i]["question"], question_data[i]["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    
    quiz.next_question()
    

print(f"You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
        
