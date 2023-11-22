from z3 import *
from quiz import *
import random
import sys
import os


# 현재 스크립트의 경로를 가져옴
current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../concept'))

from StableInPlace import *
from Enum import * 


class quiz_StableInPlace:
    def __init__(self):
        number = 1
        self.quiz = None
     
     
    def setQuiz(self, unstable, inplace): 
        instance = StableInPlace()

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
        self.quiz = quiz(1, problem, choices, answer)

        del instance
        import gc
        gc.collect()

# 테스트
test = quiz_StableInPlace()
test.setQuiz(False, False)  # 예시: 안정 정렬이면서 제자리 정렬이 아닌 알고리즘 찾기
print(test.quiz.problem)
print(test.quiz.select[0:4])
     
        
    