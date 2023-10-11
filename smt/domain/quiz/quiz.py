# 모든 quiz_으로 시작하는 파일들은 quiz 객체를 클래스 변수로 가짐.
# quiz 객체는 number(문제번호), problem(문제 텍스트), select(선지 리스트), answer(선지에서 답의 인덱스)로 이루어짐
 

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