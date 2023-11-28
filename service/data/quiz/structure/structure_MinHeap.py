from z3 import *
import random
from structure_Node import Node

def generate_min_heap_condition(node):
    conditions=[]
    if node.left:
        conditions.append(node.left.value > node.value)
        conditions.extend(generate_min_heap_condition(node.left))
    if node.right:
        conditions.append(node.right.value > node.value)
        conditions.extend(generate_min_heap_condition(node.right))
    return conditions

def collect_all_nodes(node):    
    nodes = [node]
    if node.left:
        nodes.extend(collect_all_nodes(node.left))
    if node.right:
        nodes.extend(collect_all_nodes(node.right))
    return nodes


class MinHeap:
    def __init__(self):
        self.a = Node(Int('a'))
        self.b = Node(Int('b'))
        self.c = Node(Int('c'))
        self.d = Node(Int('d'))
        self.e = Node(Int('e'))
        self.f = Node(Int('f'))
        self.g = Node(Int('g'))
        self.h = Node(Int('h'))
        self.i = Node(Int('i'))

        self.a.left = self.b
        self.a.right = self.c
        self.b.left = self.d
        self.b.right = self.e
        self.c.left= self.f
        self.c.right=self.g
        self.d.left=self.h
        self.d.right=self.i

         #모든 노드가 고유한 값 가짐
        all_nodes = collect_all_nodes(self.a)
        unique_conditions = Distinct(*[node.value for node in all_nodes])

        # Min-Heap의 조건
        minHeap_conditions = And(generate_min_heap_condition(self.a))

        s = Solver()

        minHeap_models = []

        # 아래 모델을 여러개 뽑는 이유는, z3가 같은 해를 출력하는 경향이 있기 때문. 10개의 해를 뽑아놓고 거기서 랜덤하게 선택하도록 함으로써 해결.
        # 이진 탐색 트리 조건 확인
        s.push()
        s.add(And(minHeap_conditions, unique_conditions))
        for _ in range(10):  # 10개의 서로 다른 모델 뽑아냄
            if s.check() == sat:
                m = s.model()
                minHeap_models.append(m)
                # 이미 찾은 모델을 제외하고 다시 뽑아냄
                s.add(Or([var != m[var] for var in [self.a.value, self.b.value, self.c.value, self.d.value, self.e.value, self.f.value, self.g.value, self.h.value, self.i.value]]))
        s.pop()


        # 가능한 해 중 하나를 무작위로 선택
        selected_model = random.choice(minHeap_models)

        self.a=selected_model[self.a.value].as_long()
        self.b=selected_model[self.b.value].as_long()
        self.c=selected_model[self.c.value].as_long()
        self.d=selected_model[self.d.value].as_long()
        self.e=selected_model[self.e.value].as_long()
        self.f=selected_model[self.f.value].as_long()
        self.g=selected_model[self.g.value].as_long()
        self.h=selected_model[self.h.value].as_long()
        self.i=selected_model[self.i.value].as_long()
