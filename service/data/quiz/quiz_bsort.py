from z3 import *
from service.data.quiz.quiz import *
from service.data.quiz.structure.structure_bsort_list import *


class quiz_bsort:

    def __init__(self):
        self.quiz=None

    #2회전을 확인하는 함수
    def check_two_pass(self,s, arr):
        s.push()
        #배열의 마지막 원소가 배열의 나머지 원소보다 커야 함
        for i in range(len(arr) - 2):
            s.add(arr[len(arr)-1] > arr[i])
        
        #배열의 마지막에서 두번째인 원소가 마지막 원소를 제외한 나머지 원소보다 커야 함
        for i in range(len(arr) - 3):
            s.add(arr[len(arr)-2] > arr[i])
        
        #배열의 마지막에서 세번째인 원소가 마지막 원소, 그 이전 원소를 제외한 나머지 원소보다 모두 크지 않아야 함.
        conditions = [arr[len(arr)-3] < arr[i] for i in range(len(arr) - 4)]
        s.add(Or(*conditions))

        #결과가 sat면 result에 해당 회전 결과 들어감
        result = s.check() == sat
        #solver 상태 복구
        s.pop()

        return result

    def setQuiz(self,num):
        # solver 초기화
        s = Solver()

        init_value, all_value = makeNum()
        a, b, c, d, e, f = Ints('a b c d e f')
        init = [a, b, c, d, e, f]

        # init의 각 원소, 즉 solver 변수들에 초기값 할당하기
        for var, value in zip(init, init_value): 
            s.add(var == value)

        #버블정렬을 적용한 전체 결과를 check_two_pass에 넣고, sat한 결과(2회전결과)를 도출하기
        select = ["","","","",""]
        i=1
        for arr in all_value:
            if self.check_two_pass(s, arr):
                select[0]=', '.join(map(str, arr))
            else:
                select[i]=', '.join(map(str, arr))
                i=i+1
        select.pop()

        #select[0]이 답이 됨.


        if select[0]:
            number=num
            problem=f"다음과 같은 숫자 배열이 주어졌을 때 : {init_value}, \n버블 정렬(Bubble Sort) 알고리즘을 사용하여 정렬한다고 가정하면 두 번째 통과 후의 배열 상태는 어떻게 되는가?"
            answer=0
            self.quiz=quiz(number,problem,select,answer)
        else:
            print("문제 생성 실패")

