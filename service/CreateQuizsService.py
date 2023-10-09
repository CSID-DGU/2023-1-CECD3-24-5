from util.Quiz import *

class CreateQuizsService:
    def createQuizs(scope, number):
        quizes = []
        for i in range(0, int(number)):
            #문제 생성 함수()
            quiz = Quiz()
            quiz.setQuiz(1, 'test', [1,2,3,4], 0)
            #여기까지 문제 생성
            quiz.mixAnswer()
            #직렬화
            quizes.append(quiz.changToDict())
        return quizes

