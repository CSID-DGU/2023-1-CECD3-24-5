from z3 import *

# Z3에서 제공하는 열거형 생성. 사용 방식: '열거형의 타입이 담길 변수' , '(열거형의 값의 변수들, , ...)' = EnumSort('열거형 이름', ['값1','값2','값3'...])
# 이렇게하면 이후에 Const로 정의되는 z3 변수는 저 값들 중 하나의 값만 가질 수 있음.
Complexities, (On2, Onlogn, Onplusk, Owkn) = EnumSort('Complexities', [
    'On2',
    'Onlogn',
    'Onplusk',
    'Owkn'
])

print(Complexities)

# 각 알고리즘에 대한 변수 생성 및 시간복잡도 설정
algos = {
    "선택정렬": Const("선택정렬", Complexities),
    "힙정렬": Const("힙정렬", Complexities),
    "합병정렬": Const("합병정렬", Complexities),
    "퀵정렬": Const("퀵정렬", Complexities),
    "버블정렬": Const("버블정렬", Complexities),
    "삽입정렬": Const("삽입정렬", Complexities),
    "버킷정렬": Const("버킷정렬", Complexities),
    "계수정렬": Const("계수정렬", Complexities),
    "기수정렬": Const("기수정렬", Complexities),
    "쉘정렬": Const("쉘정렬", Complexities)
}

# z3 solver 초기화
s = Solver()

# 각 알고리즘의 시간복잡도 설정
s.add(algos["선택정렬"] == On2)
s.add(algos["힙정렬"] == Onlogn)
s.add(algos["합병정렬"] == Onlogn)
s.add(algos["퀵정렬"] == On2)
s.add(algos["버블정렬"] == On2)
s.add(algos["삽입정렬"] == On2)
s.add(algos["버킷정렬"] == On2)
s.add(algos["기수정렬"] == Owkn)
s.add(algos["쉘정렬"] == On2)

# 특정 알고리즘의 시간복잡도를 찾는 함수
def find_complexity_of_algo(algorithm_name):
    if s.check() == sat:
        model = s.model()
        complexity = model[algos[algorithm_name]]
        
        if complexity == On2: return "O(n^2)"
        if complexity == Onlogn: return "O(nlogn)"
        if complexity == Onplusk: return "O(n+k)"
        if complexity == Owkn: return "O(w*(k+n))"
    else:
        return None

# 테스트
print(find_complexity_of_algo("퀵정렬"))  # O(n^2)
print(find_complexity_of_algo("힙정렬"))  # O(nlogn)
