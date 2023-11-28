from z3 import *
from service.data.quiz.concept.Enum import *

# Z3에서 제공하는 열거형 생성. 사용 방식: '열거형의 타입이 담길 변수' , '(열거형의 값의 변수들, , ...)' = EnumSort('열거형 이름', ['값1','값2','값3'...])
# 이렇게하면 이후에 Const로 정의되는 z3 변수는 저 값들 중 하나의 값만 가질 수 있음.

class newFeatures:
    def __init__(self):
        self.values=["분할 정복 방법을 사용함",
    "피벗을 사용하여 배열을 분할",
    "각 단계에서 최소값을 찾아 위치를 교환",
    "정렬된 데이터의 빠른 검색을 가능하게 함",
    "키를 사용하여 데이터에 빠르게 접근",
    "인접한 요소를 비교하고 교환하여 정렬",
    "후입선출(LIFO) 방식으로 데이터 관리",
    "선입선출(FIFO) 방식으로 데이터 관리",
    "완전 이진 트리를 사용하여 최대값 또는 최소값에 빠르게 접근",
    "정렬된 배열에서 중간점을 기준으로 검색 범위를 줄여가며 탐색",
    "노드와 간선을 사용하여 항목 간의 관계를 표현",
    "가장 깊은 노드를 우선적으로 탐색",
    "같은 레벨의 노드를 우선적으로 탐색",
    "그래프에서 최단 경로를 찾는 알고리즘",
    "부분 문제의 결과를 저장하여 전체 문제 해결",
    "매 단계에서 최선의 선택을 하는 방식"
     ]

        self.concept=Feats
        # 각 자료구조에 대한 정의 설정
        self.dic = {
            "합병정렬": Const("합병정렬", self.concept),
            "퀵정렬": Const("퀵정렬", self.concept),
            "선택정렬": Const("선택정렬", self.concept),
            "이진탐색트리": Const("이진탐색트리", self.concept),
            "해시테이블": Const("해시테이블", self.concept),
            "버블정렬": Const("버블정렬", self.concept),
            "스택": Const("스택", self.concept),
            "큐": Const("큐", self.concept),
            "힙": Const("힙", self.concept),
            "이진탐색": Const("이진탐색", self.concept),
            "그래프": Const("그래프", self.concept),
            "깊이 우선 탐색(DFS)": Const("깊이 우선 탐색(DFS)", self.concept),
            "너비 우선 탐색(BFS)": Const("너비 우선 탐색(BFS)", self.concept),
            "다익스트라 알고리즘": Const("다익스트라 알고리즘", self.concept),
            "동적 프로그래밍": Const("동적 프로그래밍", self.concept),
            "그리디 알고리즘": Const("그리디 알고리즘", self.concept)
        }

        # z3 solver 초기화
        s = Solver()

        # 각 알고리즘의 시간복잡도 설정
        s.add(self.dic["합병정렬"] == ms)
        s.add(self.dic["퀵정렬"] == qs)
        s.add(self.dic["선택정렬"] == ss)
        s.add(self.dic["이진탐색트리"] == bst)
        s.add(self.dic["해시테이블"] == ht)
        s.add(self.dic["버블정렬"] == bs)
        s.add(self.dic["스택"] == stac)
        s.add(self.dic["큐"] == queu)
        s.add(self.dic["힙"] == hea)
        s.add(self.dic["이진탐색"] == bse)
        s.add(self.dic["그래프"] == gra)
        s.add(self.dic["깊이 우선 탐색(DFS)"] == dfs)
        s.add(self.dic["너비 우선 탐색(BFS)"] == bfs)
        s.add(self.dic["다익스트라 알고리즘"] == dja)
        s.add(self.dic["동적 프로그래밍"] == dyp)
        s.add(self.dic["그리디 알고리즘"] == ga)

        if s.check() == sat:
            self.model = s.model()
            #print(self.model[Const("트리", self.concept)]) 
            #print(self.model[0]) 