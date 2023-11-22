from z3 import *
import random
from service.data.quiz.quiz import *


class quiz_findElementInStack:
    def __init__(self):
        self.quiz = None
        
    def setQuiz(self, num):
        number = num
        stack_size = random.randrange(5, 10)
        #stack = [random.randrange(0, 21) for _ in range(stack_size)]
        stack = random.sample(range(21), stack_size)
        target = random.choice(stack)  # 스택에서 무작위로 선택한 원소를 목표 원소로 설정
        problem = f"아래와 같은 스택에서, 목표 원소 ({target})가 Top에 위치하기 위해 필요한 최소한의 pop 연산 횟수를 계산하시오.\n스택: {stack}"

        s = Solver()
        num_pops = Int('num_pops')  # pop 연산의 횟수
        conditions = []

        # num_pops가 각각의 값일 때 조건을 추가
        for i in range(stack_size):
            if i < len(stack) and stack[-(i+1)] == target:
                conditions.append(num_pops == i)

        s.add(Or(conditions))
        s.add(num_pops >= 0, num_pops < stack_size)  # pop 연산의 횟수는 스택 크기 범위 내에서 설정
        
        if s.check() == sat:
            m = s.model()
            answer = m[num_pops].as_long()  # 정답 추출
            select = [answer, answer + 1, answer - 1, answer + 2]  # 선택지 생성
            self.quiz = quiz(number, problem, select, 0)
        else:
            print("해를 찾을 수 없습니다.")
