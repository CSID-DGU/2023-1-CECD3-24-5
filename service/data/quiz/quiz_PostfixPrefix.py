from z3 import *
from service.data.quiz.quiz import *
from service.data.quiz.structure.structure_PostfixPrefix import *
import sys
import os
import random



class quiz_PostfixPrefix:
    def __init__(self):
        self.quiz=None
     
    def setQuiz(self,num): 
        # max_trees 10으로 지정하지 않으면 가능한 나무들 많아서 시간이 너무 오래 걸림..
        max_trees = 10
        while s.check() == sat and len(possible_trees) < max_trees:
            m = s.model()
            possible_trees.append(m)
            s.add(Or([node.value != m[node.value] for node in all_nodes]))

        if possible_trees:
            selected_model = random.choice(possible_trees)
    
            # 노드 출력 순서를 a,b,c.. 로 고정
            #for node in [a, b, c, d, e, f, g]:
                #print(f"{node.value}: {selected_model[node.value]}")
    
    
            # 필요 시 전위 혹은 후위 둘 중 하나로 결정해서 출력 가능
            preorder_expr = to_preorder(a, selected_model)
            postorder_expr = to_postorder(a, selected_model)
    
            # 오답 선지 만들기 위헤
            wrong_expr1 = generate_mixed_expression(preorder_expr.copy(), postorder_expr.copy())
            wrong_expr2 = generate_mixed_expression(preorder_expr.copy(), postorder_expr.copy())

    
            number = num
            problem = "다음 중 위 트리 구조를 (전위순회)한 결과로 올바른 것은?"
            select = ["", "", "", ""]
            answer = 0
            select = [
                " ".join(preorder_expr),
                " ".join(postorder_expr),
                " ".join(wrong_expr1),
                " ".join(wrong_expr2)
            ]

        self.quiz=quiz(number,problem,select,answer)
        self.quiz.setType(1)

