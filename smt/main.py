from domain.quiz.quiz_bsort import *
from domain.quiz.quiz_BstHeapNormalTree import *

one=quiz_bsort()
two=quiz_BstHeapNormalTree()
quiz=[one,two]

for i in range(len(quiz)):
    quiz[i].setQuiz()
    print('문제:')
    print(quiz[i].quiz.problem)
    print('선지:')
    print('1: '+quiz[i].quiz.select[0])
    print('2: '+quiz[i].quiz.select[1])
    print('3: '+quiz[i].quiz.select[2])
    print('4: '+quiz[i].quiz.select[3])
    print('답: ')
    print(quiz[i].quiz.select[0])

