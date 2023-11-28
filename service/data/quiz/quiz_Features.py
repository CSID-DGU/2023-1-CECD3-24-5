from z3 import *
from service.data.quiz.quiz import *
from service.data.quiz.concept.Features import *
from service.data.quiz.concept.Enum import *
import random
import sys
import os


class quiz_Features:
    def __init__(self):
        self.quiz = None
    def setQuiz(self): 
        number=1
        instance=Features()
        algoName = random.choice(instance.model)
        problem=f"다음 자료구조 {algoName}의 정의로 옳은 것을 고르시오"
        select=[]
        select.append(str(instance.model[Const(str(algoName), instance.concept)]))
        for i in instance.values:
            if i != select[0]:
                select.append(i)
        # 정답 인덱스를 설정
        answer = 0   
        self.quiz = quiz(number, problem, select, answer)

        del instance
        import gc
        gc.collect()

