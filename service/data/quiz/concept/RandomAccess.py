from z3 import *
from service.data.quiz.concept.Enum import *


class RandomAccess:
    def __init__(self):

        self.values=['배열', '연결리스트', '스택', '큐', '트리', '그래프']

        self.concept = BoolSort()

        self.dic = {
            "배열": Const('배열', self.concept),
            "연결리스트": Const('연결리스트', self.concept),
            "스택": Const('스택', self.concept),
            "큐": Const('큐', self.concept),
            "트리": Const('트리', self.concept),
            "그래프": Const('그래프', self.concept),
        }
        # z3 solver 초기화
        s = Solver()

        s.add(self.dic["배열"] == True)
        s.add(self.dic["연결리스트"] == False)
        s.add(self.dic["스택"] == False)
        s.add(self.dic["큐"] == False)
        s.add(self.dic["트리"] == False)
        s.add(self.dic["그래프"] == False)


        if s.check() == sat:
            self.model = s.model()