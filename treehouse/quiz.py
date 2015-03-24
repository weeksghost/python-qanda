import datetime
import random

from questions import Add, Multiply


class Quiz:
    questions = []
    answers = []

    def __init__(self):
        question_types = (Add, Multiply)
        for _ in range(10):
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            question = random.choice(question_types)(num1, num2)
            self.questions.append(question)

    def take_quiz(self):
        # log start time
        # ask questions
        # log if correct
        # log end time
        # show summary
        pass

    def ask(self, question):
        # log start time
        # capture answer
        # check answer
        # log end time
        # if right, send back True
        # otherwise send back False
        # send back elapsed time
        pass

    def total_correct(self):
        # return total correct answers
        total = 0
        for answer in self.answers:
            if answer[0]:
                total += 1
        return total

    def summary(self):
        print("You got {} out of {} right.".format(
                self.toatal_correct(), len(self.questions)
        ))
        print("It took you {} seconds total.".format(
            (self.end_time-self.start_time).seconds
        ))