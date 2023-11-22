# 9.13 작성.
# z3의 사용 1: 자료구조가 갖고있는 제약조건을 미리 입력하여, 값이 들어간 자료구조를 생성하는데에 사용.
# z3의 사용 2: 각 문제가 가지는 추가적인 문제를 위한 제약조건을 넣어주어, 내가 만든 문제에 대한 해를 구함.

# 문제 예시: 아래 자료구조는 (트리, BST, Heap, Red-Black 트리) 중 하나이다. 해당되는 자료구조를 선택하시오.
from z3 import *
from service.data.quiz.quiz import *
import random
import sys
import os

# 현재 스크립트의 경로를 가져옴
current_path = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.join(current_path, '../structure'))
from structure_NormalTree import NormalTree
from structure_MinHeap import MinHeap
from structure_BST import BST

class quiz_BstHeapNormalTree:
    def __init__(self):
        self.quiz=None
    def setQuiz(self,num):
        number=num
        problem="아래 자료구조는 (일반 트리, 이진 탐색 트리, 최소 힙, Red-Black 트리) 중 하나이다. 해당되는 자료구조를 선택하시오."
        select=[""]
        answer=0
        all_value=['일반 트리','이진 탐색 트리','최소 힙','Red-Black 트리']
        selected_tree_type=random.choice(all_value)
        if selected_tree_type=='Normal':
            normal=NormalTree()
            select[0]='일반 트리'
            problem=problem+"\n"+"a=%d, b=%d, c=%d, d=%d, e=%d, f=%d, g=%d, e=%d, i=%d"%(normal.a,normal.b,normal.c,normal.d,normal.e,normal.f,normal.g,normal.h,normal.i)
        elif selected_tree_type=='BST':
            bst=BST()
            select[0]='이진 탐색 트리'
            problem=problem+"\n"+"a=%d, b=%d, c=%d, d=%d, e=%d, f=%d, g=%d, e=%d, i=%d"%(bst.a,bst.b,bst.c,bst.d,bst.e,bst.f,bst.g,bst.h,bst.i)
        else:
            minHeap=MinHeap()
            select[0]='최소 힙'
            problem=problem+"\n"+"a=%d, b=%d, c=%d, d=%d, e=%d, f=%d, g=%d, e=%d, i=%d"%(minHeap.a,minHeap.b,minHeap.c,minHeap.d,minHeap.e,minHeap.f,minHeap.g,minHeap.h,minHeap.i)
        for item in all_value:
            if item != select[0]:
                select.append(item)
    
        
        self.quiz=quiz(number,problem,select,answer)
        self.quiz.setType(2)