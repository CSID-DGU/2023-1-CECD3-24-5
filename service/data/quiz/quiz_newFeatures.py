from z3 import *
from service.data.quiz.quiz import *
from service.data.quiz.concept.newFeatures import *
from service.data.quiz.concept.Enum import *
import random


class quiz_newFeatures:
    def __init__(self):
        self.quiz = None
    def setQuiz(self,num): 
        number=num
        instance=newFeatures()
        algoName = random.choice(instance.model)
        problem=f"다음은 {algoName}에 대한 설명이다. 가장 옳은 것을 고르시오"
        select=[]
        select.append(str(instance.model[Const(str(algoName), instance.concept)]))
        count=1
        for i in instance.values:
            if count==4:
                break
            if i != select[0]:
                select.append(i)
                count=count+1
        # 정답 인덱스를 설정
        answer = 0   
        self.quiz = quiz(number, problem, select, answer)

        del instance
        import gc
        gc.collect()

