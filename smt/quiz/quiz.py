import random

class quiz:

    def __init__(self,number,problem,select,answer):
        self.number = number
        self.problem = problem
        self.select = select
        self.answer = answer

    def setQuiz(self, number, problem, select, answer):
        self.number = number
        self.problem = problem
        self.select = select
        self.answer = answer

    def mixAnswer(self):
        answerNumber = random.randint(0, 3)
        swapData = self.select[answerNumber]
        self.select[answerNumber] = self.select[0]
        self.select[0] = swapData
        self.answer = answerNumber

    def changToDict(self):
        return {
            'number': self.number,
            'problem': self.problem,
            'select': self.select,
            'answer': self.answer
        }