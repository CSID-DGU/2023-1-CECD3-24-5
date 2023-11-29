from z3 import *
from service.data.quiz.quiz import *
from service.data.quiz.concept.StableInPlace import *
from service.data.quiz.concept.Enum import *
import random



class quiz_StableInPlace:
    def __init__(self):
        number = 1
        self.quiz = None


    def setQuiz(self,num, unstable, inplace): 
        instance = StableInPlace()
        number=num

        # 조건에 맞는 알고리즘 선택
        selected_algos = [name for name, (unst, inpl) in instance.dic.items() if is_true(instance.model[unst]) == unstable and is_true(instance.model[inpl]) == inplace]

        # 선지 생성
        correct_answer = random.choice(selected_algos)
        other_algos = [name for name in instance.values if name != correct_answer]
        random.shuffle(other_algos)
        choices = [correct_answer] + other_algos[:3]

        problem = f"다음 중 {'불안정 정렬이고' if unstable else '안정 정렬이면서'} {'제자리 정렬인' if inplace else '제자리 정렬이 아닌'} 정렬 방법은?"

        # 정답 인덱스 설정
        answer = 0   
        self.quiz = quiz(number, problem, choices, answer)

        del instance
        import gc
        gc.collect()
