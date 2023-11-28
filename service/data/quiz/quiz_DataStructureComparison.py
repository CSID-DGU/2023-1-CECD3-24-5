from z3 import *
from service.data.quiz.quiz import *
from service.data.quiz.concept.DataStructureComparison import *
import random
import sys
import os


class quiz_DataStructureComparison:
    def __init__(self):
        self.quiz = None


    def setQuiz(self,num):
        instance = DataStructureComparison()
        number=num
        # 자료구조 목록을 가져옴
        structures = [
            "이진 탐색 트리 (BST)",
            "균형 이진 트리 (Balanced Binary Tree)",
            "해시 테이블 (Hash Table)",
            "배열 (Array)",
            "연결 리스트 (Linked List)",
            "스택 (Stack)",
            "큐 (Queue)"
        ]

        # 평균 탐색 시간 복잡도가 2 이하인 자료구조 선택
        filtered_structures = instance.get_structures_with_log_search_time()

        if len(filtered_structures) == 0:
            raise Exception("조건을 만족하는 자료구조가 없습니다.")

        # 정답을 항상 0번 인덱스에, 나머지는 오답 선지로 배치
        random.shuffle(structures)
        correct_answer = random.choice(filtered_structures)
        wrong_answers = [struct for struct in structures if struct not in filtered_structures]
        wrong_answers = random.sample(wrong_answers, 3)  # 3개의 오답 선지 선택

        options = [correct_answer] + wrong_answers

        problem = "평균 케이스에서 탐색 시간 복잡도가 O(log n) 이하인 자료구조는 무엇입니까?"

        self.quiz = quiz(number,problem, options, 0)  # 정답 인덱스는 항상 0

