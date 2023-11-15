from z3 import *
import random
from service.data.quiz.quiz import *

class quiz_circularQueueE:
    def __init__(self):
        self.quiz=None
    def setQuiz(self,num):
        number=num
        problem="다음 순환 큐가 Empty가 되기 위해 필요한 dequeue 연산의 횟수를 구하시오."
        select=[""]
        answer=0

        queue_size = random.randrange(5,8) 
        queue= [0]*queue_size
        front = random.randrange(0,queue_size)
        rear = random.randrange(0,queue_size)
        #current_elements는 front와 rear를 통해 구한 현재 순환큐에 들어있는 원소의 개수
        current_elements = (rear - front + queue_size) % queue_size

        for i in range(current_elements):
            queue[(front+i)%queue_size] = random.randrange(0,21) #queue의 front부터 rear-1까지 0~21까지의 숫자 중 임의로 넣기

        problem+=f"\n{queue}\tfront index: {front}\trear index: {rear}"

        s = Solver()

        num_dequeues = Int('num_dequeues') #dequeue 연산 횟수

        s.add((front - num_dequeues) % queue_size == (rear) % queue_size) #queue가 비는 조건

        s.add(num_dequeues > 0) #enqueue 연산 횟수는 0 이상

        

        if s.check() == sat:
            m = s.model()
            select[0] = (str(m[num_dequeues]))
            select.append(int(str(m[num_dequeues]))+1)
            select.append(int(str(m[num_dequeues]))-1)
            select.append(int(str(m[num_dequeues]))+2)
            self.quiz=quiz(number,problem,select,answer)
        else:
            print("해를 찾을 수 없습니다.")
