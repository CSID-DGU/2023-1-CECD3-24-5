# 9.13 작성.
# z3의 사용 1: 자료구조가 갖고있는 제약조건을 미리 입력하여, 값이 들어간 자료구조를 생성하는데에 사용.
# z3의 사용 2: 각 문제가 가지는 추가적인 문제를 위한 제약조건을 넣어주어, 내가 만든 문제에 대한 해를 구함.

# 문제 예시: 아래 자료구조는 (트리, BST, Heap, Red-Black 트리) 중 하나이다. 해당되는 자료구조를 선택하시오.


from z3 import *
import random
from NormalTree import NormalTree
from MinHeap import MinHeap
from BST import BST

class BstHeapNormalTree:

    def makeQuiz(self):
        selected_tree_type=random.choice(['Normal','BST','Heap'])
        if selected_tree_type=='Normal':
            normal=NormalTree()
            print('normal')
            return normal
        elif selected_tree_type=='BST':
            bst=BST()
            print('bst')
            return bst
        else:
            minHeap=MinHeap()
            print('min-heap')
            return minHeap