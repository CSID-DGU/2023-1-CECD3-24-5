import sys
import os
current_path = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.join(current_path, '../domain'))
from quiz.quiz import *

class CreateQuizsService:
    def createQuizs(scope, number):
        quizes = []
        for i in range(0, int(number)):
            #문제 생성 함수()
            new_quize = Quiz(1, 'test', [1,2,3,4],0)
            new_quize.setQuiz(1, 'test', [1,2,3,4], 0)
            #여기까지 문제 생성
            new_quize.mixAnswer()
            #직렬화
            quizes.append(new_quize.changToDict())
        return quizes