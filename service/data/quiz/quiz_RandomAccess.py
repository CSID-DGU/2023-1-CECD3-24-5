from z3 import *
from service.data.quiz.quiz import *
from service.data.quiz.concept.RandomAccess import *
from service.data.quiz.concept.Enum import *
import random



class quiz_RandomAccess:
    def __init__(self):
        self.quiz = None

    def setQuiz(self,num): 
        number = num
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

