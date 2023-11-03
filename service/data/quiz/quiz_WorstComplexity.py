from z3 import *
#from quiz import *
from service.data.quiz.quiz import *
import random
import sys
import os

# 현재 스크립트의 경로를 가져옴
current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../concept'))
from WorstComplexity import *
from Enum import *

class quiz_WorstComplexity:
    def __init__(self):
        self.quiz=None
    def setQuiz(self,num):
        number=num
        instance=WorstComplexity()
        algoName=random.choice(instance.model)
        problem=f"{algoName}의 최악 시간 복잡도로 올바른 것을 고르시오"
        select=[]
        select.append(str(instance.model[Const(str(algoName), instance.concept)]))
        for i in instance.values:
            if i!=select[0]:
                select.append(i)
        answer=0
        self.quiz=quiz(number,problem,select,answer)

        del instance
        import gc
        gc.collect()
