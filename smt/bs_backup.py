from z3 import *
import random

#----------5회전해야 정렬이 끝나는 크기가 6인 배열 랜덤하게 생성--------#

def checkFivePass(): 
    swapCnt = 0
    arr = [0]*6

    for i in range(6): #중복 없는 랜덤한 숫자 배열 뽑기
        num = random.randrange(1, 21)
        while num in arr:
            num = random.randrange(1, 21)
        arr[i] = num

    initArr = arr.copy()
    allArr = [[0 for j in range(6)] for i in range(5)]

    for round in range(5): #숫자 배열 버블정렬 5회전
        swapCnt = 0
        for j in range(len(arr) - 1 - round):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapCnt += 1

        if swapCnt == 0: #5회전 전에 정렬이 끝났다면
            return False

        allArr[round] = arr.copy()
    
    return initArr, allArr #5회전에 맞추어 정렬이 끝나는 배열 리턴

def makeNum() :
    while True:
        result = checkFivePass() #반환값이 False가 아닌 튜플인지 확인
        if result and isinstance(result, tuple) and len(result) == 2:
            arr, allArr = result
            return arr, allArr


#------------ 여기부터 솔버 ----------------#

#2회전을 확인하는 함수
def check_two_pass(s, arr):
    s.push()
    #배열의 마지막 원소가 배열의 나머지 원소보다 커야 함
    for i in range(len(arr) - 2):
        s.add(arr[len(arr)-1] > arr[i])
    
    #배열의 마지막에서 두번째인 원소가 마지막 원소를 제외한 나머지 원소보다 커야 함
    for i in range(len(arr) - 3):
        s.add(arr[len(arr)-2] > arr[i])
    
    #배열의 마지막에서 세번째인 원소가 마지막 원소, 그 이전 원소를 제외한 나머지 원소보다 모두 크지 않아야 함.
    conditions = [arr[len(arr)-3] < arr[i] for i in range(len(arr) - 4)]
    s.add(Or(*conditions))

    #결과가 sat면 result에 해당 회전 결과 들어감
    result = s.check() == sat
    #solver 상태 복구
    s.pop()

    return result



# solver 초기화
s = Solver()

init_value, all_value = makeNum()
a, b, c, d, e, f = Ints('a b c d e f')
init = [a, b, c, d, e, f]

# init의 각 원소, 즉 solver 변수들에 초기값 할당하기
for var, value in zip(init, init_value): 
    s.add(var == value)

#버블정렬을 적용한 전체 결과를 check_two_pass에 넣고, sat한 결과(2회전결과)를 도출하기
answer = []
random.shuffle(all_value)

for arr in all_value:
    if check_two_pass(s, arr):
        answer.append(arr)

if answer:
    print(f"다음과 같은 숫자 배열이 주어졌을 때 : {init_value}, \n버블 정렬(Bubble Sort) 알고리즘을 사용하여 정렬한다고 가정하면 두 번째 통과 후의 배열 상태는 어떻게 되는가?")

    #젼체 리스트에서 정답을 제외한 나머지 랜덤한 요소 하나를 없애기
    choice = [[0 for j in range(6)] for i in range(4)]
    choice = [item for item in all_value if item not in answer]
    not_choice = random.choice(choice)
    all_value.remove(not_choice)

    #문제 출력
    cnt = 1
    for row in all_value:
        print(f"{cnt} : {row}")
        cnt += 1

    #답 출력
    print(f"답: {answer[0]}")
else:
    print("답을 찾을 수 없습니다.")
