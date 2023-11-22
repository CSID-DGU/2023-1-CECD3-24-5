from z3 import *
from Enum import *

# Z3에서 제공하는 열거형 생성. 사용 방식: '열거형의 타입이 담길 변수' , '(열거형의 값의 변수들, , ...)' = EnumSort('열거형 이름', ['값1','값2','값3'...])
# 이렇게하면 이후에 Const로 정의되는 z3 변수는 저 값들 중 하나의 값만 가질 수 있음.

class Features:
    def __init__(self):
        self.values=['인덱스와 인덱스에 대응하는 데이터들로 이루어진 자료구조',
              '다음 item에 대한 link가 있는 item들로 구성된 리스트',
              '가장 최근에 추가된 항목만 제거할 수 있는 항목 모음의 자료구조',
              '가장 먼저 추가된 항목만 액세스할 수 있는 항목 모음의 자료구조',
              '각 항목이 이전 항목과 다음 항목에 대한 링크를 갖는 연결리스트의 변형 자료구조',
              '그래프의 일종으로, 한 노드에서 시작해서 다른 정점들을 순회하여 자기 자신에게 돌아오는 순환이 없는 연결 그래프',
              '모든 노드의 키가 부모의 키보다 크거나 같은 완전한 트리',
              'node와 그 node를 연결하는 edge를 하나로 모아놓은 자료구조',
              '키를 값에 매핑할 수 있는 구조인, 연관 배열 추가에 사용되는 자료 구조'
              ]
        
        self.concept=Defi
        # 각 자료구조에 대한 정의 설정
        self.dic = {
            "배열": Const("배열", self.concept),
            "연결리스트": Const("연결리스트", self.concept),
            "스택": Const("스택", self.concept),
            "큐": Const("큐", self.concept),
            "이중연결리스트": Const("이중연결리스트", self.concept),
            "트리": Const("트리", self.concept),
            "힙": Const("힙", self.concept),
            "그래프": Const("그래프", self.concept),
            "해시": Const("해시", self.concept),
        }

        # z3 solver 초기화
        s = Solver()

        # 각 알고리즘의 시간복잡도 설정
        s.add(self.dic["배열"] == arr)
        s.add(self.dic["연결리스트"] == ll)
        s.add(self.dic["스택"] == sta)
        s.add(self.dic["큐"] == que)
        s.add(self.dic["이중연결리스트"] == dll)
        s.add(self.dic["트리"] == tr)
        s.add(self.dic["힙"] == he)
        s.add(self.dic["그래프"] == grp)
        s.add(self.dic["해시"] == ha)

        if s.check() == sat:
            self.model = s.model()
            #print(self.model[Const("트리", self.concept)]) 
            #print(self.model[0]) 


