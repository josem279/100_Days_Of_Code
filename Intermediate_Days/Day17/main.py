# # More on OOP

# ############# Building classes
# class User:

#     # Adding attributes
#     def __init__(self, user_id, username):
#         self.user_id = user_id 
#         self.username = username
#         self.followers = 0
#         self.following = 0

#     # Adding methods
#     def follow(self, user):
#         self.followers += 1
#         self.following += 1

# user_1 = User("001", "jose")
# user_2 = User("002", "john")

# print(user_1.username)

# print(user_1.following)
# user_1.follow(user_2)
# print(user_1.following)
# print(user_2.followers)


############### Quiz Project
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    answer = quiz.next_question()

print("You've completed the quiz")

print(f"Your final score is: {quiz.score}/{len(question_bank)}")