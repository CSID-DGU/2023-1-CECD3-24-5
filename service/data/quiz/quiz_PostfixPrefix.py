from z3 import *
from service.data.quiz.quiz import *
from service.data.quiz.structure.structure_PostfixPrefix import *
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
            problem = f"다음 트리 구조를 (전위순회)한 결과로 올바른 것은? \n a={selected_model[a.value]}, b={selected_model[b.value]}, c={selected_model[c.value]}, d={selected_model[d.value]}, e={selected_model[e.value]}, f={selected_model[f.value]}, g={selected_model[g.value]}"
            problem += "\n 단, 수직 레이아웃에서 위쪽 노드는 왼쪽 자식 노드임을 가정한다."
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
