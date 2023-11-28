from z3 import *
import random

class quiz_hashTableLocation:
    def __init__(self):
        self.quiz = None

    def hash_function(self, key, table_size):
        # 간단한 해시 함수: key를 table_size로 나눈 나머지를 반환
        return key % table_size

    def setQuiz(self, num):
        number = num
        table_size = random.randrange(5, 10)  # 해시 테이블 크기
        operations = random.randrange(5, 10)  # 수행할 연산의 수

        # 해시 테이블 초기화
        hash_table = [-1] * table_size

        # 삽입 및 삭제 연산 수행
        for _ in range(operations):
            operation_type = random.choice(['insert', 'delete'])
            key = random.randrange(0, 21)

            if operation_type == 'insert':
                index = self.hash_function(key, table_size)
                hash_table[index] = key
            elif operation_type == 'delete':
                index = self.hash_function(key, table_size)
                hash_table[index] = -1

        # 찾을 원소 선택
        target = random.choice(range(21))

        # 문제 생성
        problem = f"다음 해시 테이블에서 원소 {target}의 위치를 찾으시오.\n해시 테이블: {hash_table}\n해시 함수: key % {table_size}"

        s = Solver()

        # 위치 변수 정의
        location = Int('location')

        # 위치 조건 추가
        s.add(Or([location == self.hash_function(target, table_size) if hash_table[self.hash_function(target, table_size)] == target else location == -1]))

        if s.check() == sat:
            m = s.model()
            answer = m[location].as_long()
            select = [answer, answer + 1, answer - 1, answer + 2]  # 선택지 생성
            self.quiz = (number, problem, select, 0)
        else:
            print("해를 찾을 수 없습니다.")

