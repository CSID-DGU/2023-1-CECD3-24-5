# 문제: 다음은, 어떤 자료구조에 대한 삽입 연산이 진행되는 코드이다. 해당 자료구조는 무엇인가?

# 1. 우선 '스택', '균형이진트리', '최대 힙', '이진 탐색 트리' 에 대한 삽입 연산을 메소드 형태로 모두 정의
# 2. 그리고, random 라이브러리를 이용해서, 위의 네 자료구조 중에 하나를 랜덤하게 선택
# 3. z3를 이용해 선택된 자료구조의 제약조건을 만족하는 해를 구해서, 해당 해를 이용해 자료구조 안에 값들을 채워넣음
# 4. 그 다음엔, 위에서 선택받은 자료구조에 대한 삽입연산 메소드를 불러와서, 해당 삽입연산을 내가 만든 자료구조에 진행
# 5. 삽입연산을 진행한 후에도, 자료구조에 대한 제약조건을 여전히 만족하는지 검증함으로써, 해당 자료구조에 대한 삽입연산 메소드라는 것을 검증

from z3 import Solver, Int, And
import random
from smt.structure_Node import Node
from smt.structure_BST import BST


# 정의된 삽입 메소드 (이 경우, 이진 탐색 트리 삽입)
def bst_insert(root, value):
    if root is None:
        root=Node(value)
        root.left=None
        root.right=None
        return root
    if root.value == value:
        return root
    elif root.value > value:
        root.left = bst_insert(root.left, value)
    else:
        root.right = bst_insert(root.right, value)
    return root

# 이진 탐색 트리 제약 조건을 z3로 검증
def validate_bst(root, s):
    if not root:
        return True
    x = Int('x')
    y = Int('y')
    if root['left']:
        s.add(x < root['value'])
        validate_bst(root['left'], s)
    if root['right']:
        s.add(y > root['value'])
        validate_bst(root['right'], s)

# 각 자료구조의 초기 상태를 생성 (랜덤하게 자료구조를 선택)
data_structures = ['Stack', 'BalancedBinaryTree', 'MaxHeap', 'BinarySearchTree']
chosen_structure = random.choice(data_structures)

# z3 solver 초기화
s = Solver()

# 선택된 자료구조에 따라 초기 상태와 제약 조건을 설정
if chosen_structure == 'BinarySearchTree':
    root = {'value': 50, 'left': None, 'right': None}
    s.add(Int('root') == 50)

    # z3를 사용하여 제약 조건을 만족하는 해를 찾고 값을 삽입
    if s.check() == 'sat':
        m = s.model()
        root_value = m.evaluate(Int('root')).as_long()
        bst_insert(root, root_value)
        
    # z3를 사용하여 삽입 연산 후에도 제약 조건을 만족하는지 확인
    if validate_bst(root, s):
        print(f"The generated question is: The following code performs an insert operation on a data structure. What is the data structure?")
        print(f"Chosen data structure: {chosen_structure}")
