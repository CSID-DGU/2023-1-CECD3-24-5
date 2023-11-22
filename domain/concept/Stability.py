from z3 import *
from Enum import *

# Z3에서 제공하는 열거형 생성. 사용 방식: '열거형의 타입이 담길 변수' , '(열거형의 값의 변수들, , ...)' = EnumSort('열거형 이름', ['값1','값2','값3'...])
# 이렇게하면 이후에 Const로 정의되는 z3 변수는 저 값들 중 하나의 값만 가질 수 있음.

class Stability:
    def __init__(self):
        
        self.values=['선택정렬', '힙정렬', '합병정렬', '퀵정렬', '버블정렬', '삽입정렬', '버킷정렬', '기수정렬', '쉘정렬']
        
        self.concept = BoolSort()
    
        self.dic = {
            "선택정렬": Const("선택정렬", self.concept),
            "힙정렬": Const("힙정렬", self.concept),
            "합병정렬": Const("합병정렬", self.concept),
            "퀵정렬": Const("퀵정렬", self.concept),
            "버블정렬": Const("버블정렬", self.concept),
            "삽입정렬": Const("삽입정렬", self.concept),
            "버킷정렬": Const("버킷정렬", self.concept),
            "기수정렬": Const("기수정렬", self.concept),
            "쉘정렬": Const("쉘정렬", self.concept)
        }

        # z3 solver 초기화
        s = Solver()

        # 각 알고리즘의 시간복잡도 설정
        s.add(self.dic["선택정렬"] == False)
        s.add(self.dic["힙정렬"] == True)
        s.add(self.dic["합병정렬"] == True)
        s.add(self.dic["퀵정렬"] == False)
        s.add(self.dic["버블정렬"] == True)
        s.add(self.dic["삽입정렬"] == True)
        s.add(self.dic["버킷정렬"] == True)
        s.add(self.dic["기수정렬"] == True)
        s.add(self.dic["쉘정렬"] == False)

        if s.check() == sat:
            self.model = s.model()
            #print(self.model[Const(self.dic["삽입정렬"], self.concept)]) 
            #print(self.model[0])