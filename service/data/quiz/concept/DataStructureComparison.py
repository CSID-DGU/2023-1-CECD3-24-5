from z3 import *

class DataStructureComparison:
    def __init__(self):
        self.bst_avg_search = Real('bst_avg_search')
        self.balanced_avg_search = Real('balanced_avg_search')
        self.hash_avg_search = Real('hash_avg_search')
        # 추가 자료구조에 대한 평균 탐색 시간 속성
        self.array_avg_search = Real('array_avg_search')
        self.linkedlist_avg_search = Real('linkedlist_avg_search')
        self.stack_avg_search = Real('stack_avg_search')
        self.queue_avg_search = Real('queue_avg_search')

        s = Solver()
        # 로그 시간과 선형 시간을 상징적인 값으로 설정
        s.add(self.bst_avg_search == 2, self.balanced_avg_search == 2)  # 로그 시간 복잡도
        s.add(self.hash_avg_search == 1)  # 상수 시간 복잡도
        s.add(self.array_avg_search == 3, self.linkedlist_avg_search == 3)  # 선형 시간 복잡도
        s.add(self.stack_avg_search == 3, self.queue_avg_search == 3)

        if s.check() == sat:
            self.model = s.model()
        else:
            raise Exception("솔버가 해결책을 찾지 못했습니다.")

    def get_structures_with_log_search_time(self):

        structures = [
            "이진 탐색 트리 (BST)", 
            "균형 이진 트리 (Balanced Binary Tree)", 
            "해시 테이블 (Hash Table)", 
            "배열 (Array)", 
            "연결 리스트 (Linked List)", 
            "스택 (Stack)", 
            "큐 (Queue)"
        ]

        filtered_structures = []
        for struct in structures:
            avg_search_time = self.model.evaluate(self.get_avg_search_time(struct))
            # 심볼릭 값과 비교할 때는 Z3의 비교 연산자를 사용합니다.
            if self.model.evaluate(avg_search_time <= 2):
                filtered_structures.append(struct)
        return filtered_structures


    def get_avg_search_time(self, struct):
        return {
            "이진 탐색 트리 (BST)": self.bst_avg_search,
            "균형 이진 트리 (Balanced Binary Tree)": self.balanced_avg_search,
            "해시 테이블 (Hash Table)": self.hash_avg_search,
            "배열 (Array)": self.array_avg_search,
            "연결 리스트 (Linked List)": self.linkedlist_avg_search,
            "스택 (Stack)": self.stack_avg_search,
            "큐 (Queue)": self.queue_avg_search
        }[struct]