from z3 import *
import random
from smt.structure_Node import Node

def generate_bst_conditions(node):
        conditions = []
        if node.left:
            conditions.append(node.left.value < node.value)
            conditions.extend(generate_bst_conditions(node.left))
        if node.right:
            conditions.append(node.right.value > node.value)
            conditions.extend(generate_bst_conditions(node.right))
        return conditions

def collect_all_nodes(node):    
    nodes = [node]
    if node.left:
        nodes.extend(collect_all_nodes(node.left))
    if node.right:
        nodes.extend(collect_all_nodes(node.right))
    return nodes
        

class BST:


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


        #BST 조건
        bst_conditions = And(generate_bst_conditions(self.a))
        s = Solver()

        bst_models = []

        # 아래 모델을 여러개 뽑는 이유는, z3가 같은 해를 출력하는 경향이 있기 때문. 10개의 해를 뽑아놓고 거기서 랜덤하게 선택하도록 함으로써 해결.
        # 이진 탐색 트리 조건 확인
        s.push()
        s.add(And(bst_conditions, unique_conditions))
        for _ in range(10):  # 10개의 서로 다른 모델 뽑아냄
            if s.check() == sat:
                m = s.model()
                bst_models.append(m)
                # 이미 찾은 모델을 제외하고 다시 뽑아냄
                s.add(Or([var != m[var] for var in [self.a.value, self.b.value, self.c.value, self.d.value, self.e.value, self.f.value, self.g.value, self.h.value, self.i.value]]))
        s.pop()


        # 가능한 해 중 하나를 무작위로 선택
        selected_model = random.choice(bst_models)

        self.a=selected_model[self.a.value]
        self.b=selected_model[self.b.value]
        self.c=selected_model[self.c.value]
        self.d=selected_model[self.d.value]
        self.e=selected_model[self.e.value]
        self.f=selected_model[self.f.value]
        self.g=selected_model[self.g.value]
        self.h=selected_model[self.h.value]
        self.i=selected_model[self.i.value]
