from z3 import *
from quiz import *
#from service.data.quiz.quiz import *
import random
import sys
import os

# 현재 스크립트의 경로를 가져옴
current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../concept'))
from Features import *
from Enum import *

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
        
test = quiz_Features()
test.setQuiz()
print(test.quiz.problem)
print(test.quiz.select[0:4])
        

        
        