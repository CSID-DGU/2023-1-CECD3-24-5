from z3 import *
from quiz import *
#from service.data.quiz.quiz import *
import random
import sys
import os

# 현재 스크립트의 경로를 가져옴
current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../concept'))
from Stability import *
from Enum import *

class quiz_Unstability:
    def __init__(self):
        self.quiz = None
        
    def setQuiz(self): 
        number=1
        instance=Stability()
        
        # 안정한 알고리즘과 불안정한 알고리즘을 분류
        stable_algos = [name for name, var in instance.dic.items() if instance.model[var]]
        unstable_algos = [name for name, var in instance.dic.items() if not instance.model[var]]
        
        # 불안정한 알고리즘 중 하나를 선택
        unstable_choice = random.choice(unstable_algos)
        
        # 안정한 알고리즘 중 세 개를 선택
        stable_choices = random.sample(stable_algos, 3)
        
        problem = "다음 정렬 알고리즘 중 불안정한 정렬 알고리즘은?"
        
        # 문제의 선택지: 첫 번째 선택지가 안정한 알고리즘
        select = [unstable_choice] + stable_choices
                
        # 정답 인덱스를 설정
        answer = 0   
        self.quiz = quiz(number, problem, select, answer)

        del instance
        import gc
        gc.collect()
        
test = quiz_Unstability()
test.setQuiz()
print(test.quiz.problem)
print(test.quiz.select[0:4])
        

        
        