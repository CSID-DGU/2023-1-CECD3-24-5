from service.data.quiz.quiz_bsort import *
from service.data.quiz.quiz_BstHeapNormalTree import *
from service.data.quiz.quiz_PostfixPrefix import *
from service.data.quiz.quiz_WorstComplexity import *
from service.data.quiz.quiz_circularQueueF import *
from service.data.quiz.quiz_circularQueueE import *
from service.data.quiz.quiz_findElementInStack import *
from service.data.quiz.quiz_DataStructureComparison import *
from service.data.quiz.quiz_Features import *
from service.data.quiz.quiz_newFeatures import *
from service.data.quiz.quiz_RandomAccess import *
from service.data.quiz.quiz_Stability import *
from service.data.quiz.quiz_Unstability import *
from service.data.quiz.quiz_StableInPlace import *



class CreateQuizsService:

    def __init__(self):
        self.quizes=[]
        self.candidate=[]

        bsort=quiz_bsort()
        BSTHeapNormal=quiz_BstHeapNormalTree()
        PostfixPrefix=quiz_PostfixPrefix()
        WorstComplexity=quiz_WorstComplexity()
        circularQueueF=quiz_circularQueueF()
        circularQueueE=quiz_circularQueueE()
        findElementInStack=quiz_findElementInStack()
        DataStructureComparison=quiz_DataStructureComparison()
        Features=quiz_Features()
        newFeatures=quiz_newFeatures()
        RandomAccess=quiz_RandomAccess()
        Stability=quiz_Stability()
        Unstability=quiz_Unstability()
        #StableInPlace=quiz_StableInPlace()


        self.candidate.append(bsort)
        self.candidate.append(BSTHeapNormal)
        self.candidate.append(PostfixPrefix)
        self.candidate.append(WorstComplexity)
        self.candidate.append(circularQueueF)
        self.candidate.append(circularQueueE)
        self.candidate.append(findElementInStack)
        self.candidate.append(DataStructureComparison)
        self.candidate.append(Features)
        self.candidate.append(newFeatures)
        self.candidate.append(RandomAccess)
        self.candidate.append(Stability)
        self.candidate.append(Unstability)
        #self.candidate.append(StableInPlace)
    

    def createQuizs(self, number):
        for i in range(0, int(number)):
            self.candidate[i].setQuiz(i+1)
            quiz=self.candidate[i].quiz
            #여기까지 문제 생성
            quiz.mixAnswer()
            #직렬화
            self.quizes.append(quiz.changToDict())
        return self.quizes
    


