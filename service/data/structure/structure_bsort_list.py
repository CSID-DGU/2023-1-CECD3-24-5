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