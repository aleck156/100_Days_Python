
from data import question_data
from data_cs import question_data_cs

from quiz_brain import QuizzBrain

brain = QuizzBrain(question_data_cs)

answer = True
while answer:
    question = brain.pick_random_question()
    if question:
        print(question.text)
        user_choice = input(f'True or False? [true/false]: ').lower()[:1]
        if user_choice == question.answer.lower()[:1]:
            brain.player_score_increase()
            print(f'You current score is {brain.score}')
        else:
            answer = False
    else:
        print(f'Congratulations! You have answered all of the questions correctly.')
        answer = False

print(f'Your final score is {brain.score}')

# TODO
# remove the question from the list once it's been picked
# the game runs till the user fails to give correct answer OR the game runs out of questions