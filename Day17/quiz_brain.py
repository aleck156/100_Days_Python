import random

from question_model import Question

class QuizzBrain:
    def __init__(self, questions):
        self.score = 0
        self.question_bank = []
        for q in questions:
            self.question_bank.append(Question(q['text'], q['answer']))

    def print_questions(self):
        for index, question in enumerate(self.question_bank):
            print(f'Q.{index}: {question.text}')
            print(f'A.{index}: {question.answer}')

    def pick_random_question(self):
        print(f'Questions left in the bank: {len(self.question_bank)}')
        if len(self.question_bank) > 0:
            random_pick_number = random.randint(0, len(self.question_bank)-1)
            print(f'Picking a random question ... {random_pick_number}')
            question_picked = self.question_bank[random_pick_number]
            self.question_bank.pop(random_pick_number)
            return question_picked
        else:
            return False

    def player_score(self):
        return self.score

    def player_score_increase(self):
        self.score += 1

