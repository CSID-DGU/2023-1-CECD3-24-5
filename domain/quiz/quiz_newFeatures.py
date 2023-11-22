from z3 import *
from quiz import *
#from service.data.quiz.quiz import *
import random
import sys
import os

# 현재 스크립트의 경로를 가져옴
current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../concept'))
from newFeatures import *
from Enum import *

class quiz_newFeatures:
    def __init__(self):
        self.quiz = None
    def setQuiz(self): 
        number=1
        instance=newFeatures()
        algoName = random.choice(instance.model)
        problem=f"다음은 {algoName}에 대한 설명이다. 가장 옳은 것을 고르시오"
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
        
test = quiz_newFeatures()
test.setQuiz()
print(test.quiz.problem)
print(test.quiz.select[0:4])
        

        
        