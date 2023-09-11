# 문제 예시: 아래 자료구조는 (트리, BST, Heap, Red-Black 트리) 중 하나이다. 해당되는 자료구조를 선택하시오.


from z3 import *
import random

class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

s = Solver()

# 트리의 노드에 해당하는 변수를 생성 (Z3의 Int 객체 사용)
a = Node(Int('a'))
b = Node(Int('b'))
c = Node(Int('c'))
d = Node(Int('d'))
e = Node(Int('e'))
f = Node(Int('f'))
g = Node(Int('g'))
h = Node(Int('h'))
i = Node(Int('i'))

# 트리 구조 설정
a.left = b
a.right = c
b.left = d
b.right = e
c.left= f
c.right=g
d.left=h
d.right=i


# 모든 노드가 고유한 값을 가져야 함
unique_conditions = And(
    Distinct(a.value, b.value, c.value, d.value, e.value, f.value, g.value, h.value, i.value)
)

# bst 위반
not_bst_conditions = Or(
    And(a.value < b.value, a.value > c.value), # a의 BST 위배 (거짓 거짓)
    And(a.value > b.value, a.value > c.value), # a의 BST 위배 (참 거짓)
    And(a.value < b.value, a.value < c.value), # a의 BST 위배 (거짓 참)
    And(b.value < d.value, b.value > e.value), # b의 BST 위배 (거짓 거짓)
    And(b.value > d.value, b.value > e.value), # b의 BST 위배 (참 거짓)
    And(b.value < d.value, b.value < e.value), # b의 BST 위배 (거짓 참)
    And(c.value < f.value, c.value > g.value), # c의 BST 위배 (거짓 거짓)
    And(c.value > f.value, c.value > g.value), # c의 BST 위배 (참 거짓)
    And(c.value < f.value, c.value < g.value), # c의 BST 위배 (거짓 참)
    And(d.value < h.value, d.value > i.value), # d의 BST 위배 (거짓 거짓)
    And(d.value > h.value, d.value > i.value), # d의 BST 위배 (참 거짓)
    And(d.value < h.value, d.value < i.value), # d의 BST 위배 (거짓 참)
)
not_heap_conditions =Or(
    And(a.value > b.value), # a의 Min Heap 위배
    And(a.value > c.value),
    And(a.value > d.value),
    And(a.value > e.value),
    And(a.value > f.value),
    And(a.value > g.value),
    And(a.value > h.value),
    And(a.value > i.value), # a의 Min Heap 위배
    And(b.value > d.value), # b의 Min Heap 위배
    And(b.value > e.value),
    And(b.value > h.value),
    And(b.value > i.value), # b의 Min Heap 위배
    And(c.value > f.value), # c의 Min Heap 위배
    And(c.value > g.value), # c의 Min Heap 위배
    And(d.value > h.value), # d의 Min Heap 위배
    And(d.value > i.value), # d의 Min Heap 위배
)



# 이진 탐색 트리의 조건
bst_conditions = And(
    b.value < a.value, d.value < a.value, e.value < a.value,
    c.value > a.value,
    d.value < b.value, h.value < b.value, e.value > b.value,
    f.value < c.value, g.value > c.value,
    h.value < d.value, i.value > d.value
)

# Min-Heap의 조건
heap_conditions = And(
    a.value <= b.value, a.value <= c.value,
    b.value <= d.value, b.value <= e.value,
    c.value <= f.value, c.value <= g.value,
    d.value <= h.value, d.value <= i.value
)

solutions = {
    'BST': None,
    'Normal Tree': None,
    'Min-Heap': None
}
bst_models = []
normal_tree_models = []
heap_models = []

# 아래 모델을 여러개 뽑는 이유는, z3가 같은 해를 출력하는 경향이 있기 때문. 10개의 해를 뽑아놓고 거기서 랜덤하게 선택하도록 함으로써 해결.
# 이진 탐색 트리 조건 확인
s.push()
s.add(And(bst_conditions, unique_conditions))
for _ in range(10):  # 10개의 서로 다른 모델 뽑아냄
    if s.check() == sat:
        m = s.model()
        bst_models.append(m)
        # 이미 찾은 모델을 제외하고 다시 뽑아냄
        s.add(Or([var != m[var] for var in [a.value, b.value, c.value, d.value, e.value, f.value, g.value, h.value, i.value]]))
s.pop()

# 일반 트리 조건 확인 (bst도 아니면서 Min heap도 아닌)
s.push()
s.add(unique_conditions,not_bst_conditions,not_heap_conditions)
for _ in range(10):  # 10개의 서로 다른 모델 뽑아냄
    if s.check() == sat:
        m = s.model()
        normal_tree_models.append(m)
        # 이미 찾은 모델을 제외하고 다시 뽑아냄
        s.add(Or([var != m[var] for var in [a.value, b.value, c.value, d.value, e.value, f.value, g.value, h.value, i.value]]))
s.pop()

# Min-Heap 조건 확인
s.push()
s.add(And(heap_conditions, unique_conditions))
for _ in range(10):  # 10개의 서로 다른 모델 뽑아냄
    if s.check() == sat:
        m = s.model()
        heap_models.append(m)
        # 이미 찾은 모델을 제외하고 다시 뽑아냄
        s.add(Or([var != m[var] for var in [a.value, b.value, c.value, d.value, e.value, f.value, g.value, h.value, i.value]]))
s.pop()

if bst_models:
    solutions['BST'] = bst_models
if normal_tree_models:
    solutions['Normal Tree'] = normal_tree_models
if heap_models:
    solutions['Min-Heap'] = heap_models

# 가능한 해 중 하나를 무작위로 선택
selected_tree_type = random.choice([k for k, v in solutions.items() if v is not None])
selected_model = random.choice(solutions[selected_tree_type])

print(f"Found a model for {selected_tree_type}:")
for var in [a.value, b.value, c.value, d.value, e.value, f.value, g.value, h.value, i.value]:
    print(f"{var}: {selected_model[var]}")

