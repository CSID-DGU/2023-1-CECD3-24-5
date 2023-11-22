from z3 import *
from Enum import *


class StableInPlace:
    def __init__(self):
        
        self.values=['선택정렬', '힙정렬', '합병정렬', '퀵정렬', '버블정렬', '삽입정렬', '버킷정렬', '기수정렬', '쉘정렬']
        
        self.unstable = BoolSort()
        self.inplace = BoolSort()

        self.dic = {
            "선택정렬": (Const("선택정렬_unstable", self.unstable), Const("선택정렬_inplace", self.inplace)),
            "힙정렬": (Const("힙정렬_unstable", self.unstable), Const("힙정렬_inplace", self.inplace)),
            "합병정렬": (Const("합병정렬_unstable", self.unstable), Const("합병정렬_inplace", self.inplace)),
            "퀵정렬": (Const("퀵정렬_unstable", self.unstable), Const("퀵정렬_inplace", self.inplace)),
            "버블정렬": (Const("버블정렬_unstable", self.unstable), Const("버블정렬_inplace", self.inplace)),
            "삽입정렬": (Const("삽입정렬_unstable", self.unstable), Const("삽입정렬_inplace", self.inplace)),
            "버킷정렬": (Const("버킷정렬_unstable", self.unstable), Const("버킷정렬_inplace", self.inplace)),
            "기수정렬": (Const("기수정렬_unstable", self.unstable), Const("기수정렬_inplace", self.inplace)),
            "쉘정렬": (Const("쉘정렬_unstable", self.unstable), Const("쉘정렬_inplace", self.inplace))
        }

        # z3 solver 초기화 및 각 알고리즘의 특성 정의
        s = Solver()
        s.add(self.dic["선택정렬"] == (True, True))   # 불안정, 제자리
        s.add(self.dic["힙정렬"] == (True, True))     # 불안정, 제자리
        s.add(self.dic["합병정렬"] == (False, False)) # 안정, 제자리 아님
        s.add(self.dic["퀵정렬"] == (True, True))     # 불안정, 제자리
        s.add(self.dic["버블정렬"] == (False, True))  # 안정, 제자리
        s.add(self.dic["삽입정렬"] == (False, True))  # 안정, 제자리
        s.add(self.dic["버킷정렬"] == (False, False)) # 안정, 제자리 아님
        s.add(self.dic["기수정렬"] == (False, False)) # 안정, 제자리 아님
        s.add(self.dic["쉘정렬"] == (True, True))     # 불안정, 제자리

        if s.check() == sat:
            self.model = s.model()  # Solver의 모델을 저장
        else:
            raise Exception("솔버가 해결책을 찾지 못했습니다.")
        
