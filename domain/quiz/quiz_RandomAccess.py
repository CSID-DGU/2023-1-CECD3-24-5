from z3 import *
from quiz import *
#from service.data.quiz.quiz import *
import random
import sys
import os

# 현재 스크립트의 경로를 가져옴
current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../concept'))
from RandomAccess import *
from Enum import *

class quiz_RandomAccess:
    def __init__(self):
        self.quiz = None
        
    def setQuiz(self): 
        number = 1
        instance = RandomAccess()
    
        can_ra = [name for name, var in instance.dic.items() if instance.model[var]]
        cant_ra = [name for name, var in instance.dic.items() if not instance.model[var]]
        
        ra_choice = random.choice(can_ra)
        
        cra_choices = random.sample(cant_ra, 3)    
        
        problem=f"다음 자료구조 중 Random Access가 가능한 자료구조를 고르시오"
        select = [ra_choice] + cra_choices
        # 정답 인덱스를 설정
        answer = 0   
        self.quiz = quiz(number, problem, select, answer)


        del instance
        import gc
        gc.collect()

        
test = quiz_RandomAccess()
test.setQuiz()
print(test.quiz.problem)
print(test.quiz.select[0:4])
        

        
        