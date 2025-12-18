# A bunch of searching/sorting algorithms implemented in Python
import random as r

def LinearSearch(SearchObj, SearchSet):
    Found = False
    Indexes = []
    for x in range(0, len(SearchSet)):
        if SearchSet[x] == SearchObj:
            Indexes.append(x)
            Found = True
    if Found:
        return Indexes
    else:
        return -1
    
# 你好我很爱你
def BinarySearch(SearchObj, SearchSet):
    LPoint = 0
    RPoint = len(SearchSet) - 1
    MPoint = (LPoint + RPoint) // 2
    while (LPoint <= MPoint):
        if SearchSet[MPoint] == SearchObj: # Checks bounds
            return MPoint
        elif SearchSet[MPoint] < SearchObj:
            LPoint = MPoint + 1
        elif SearchObj < SearchSet[MPoint]:
            RPoint = MPoint - 1
        MPoint = (LPoint + RPoint) // 2 # Recalculates pointer
    return -1

# ಥ_ಥ
def InsertionSort(SortList):
    for x in range(1, len(SortList)):
        SwapItem = SortList[x]
        CompareMarketDotComIndex = x
        while (SwapItem < SortList[CompareMarketDotComIndex - 1]) and (0 < CompareMarketDotComIndex): # Moves new position down each iteration if it is smaller then the item before it
            SortList[CompareMarketDotComIndex] = SortList[CompareMarketDotComIndex - 1] # Swaps
            CompareMarketDotComIndex -= 1
        SortList[CompareMarketDotComIndex] = SwapItem # If indexes moves then item placed in sorted place, otherwise replaces same space
    return SortList

#☆*: .｡. o(≧▽≦)o .｡.:*☆
def BubbleSort(SortList):
    Sorted = True
    for x in range(len(SortList) - 1, 1, -1): # Defines inner loop ranges
        for y in range(0, x): # Loops up to before sorted parts
            if SortList[y] > SortList[y + 1]: # Sorts
                Sorted = False
                SortList[y], SortList[y + 1] = SortList[y + 1], SortList[y]
        if Sorted: # Early quit if already sorted
            break
    return SortList

def MergeSortMerge(SortList, LPoint, RBound, LBound):
    RPoint = LBound + 1

    while (LPoint <= LBound) or (RPoint <= RBound): # While not reached end of both sections of each lists to merge
        if SortList[LPoint] < SortList[RPoint]: # Selects the smallest value from the front of both list and inserts them
            SortList[LPoint], SortList[RPoint] = SortList[RPoint], SortList[LPoint]
            LPoint += 1
        elif SortList[LPoint] >= SortList[RPoint]:
            SortList[LPoint], SortList[RPoint] = SortList[RPoint], SortList[LPoint]
            RPoint += 1

    # if not (LPoint <= LBound) and (RPoint <= RBound): # If RSide incomplete, move it to the back
    # Don't think need this, if RSide incomplete then 

# MPoint counts as left partition
def MergeSort(SortList, LPoint, RPoint):
    if LPoint >= RPoint:
        return
    else:
        MPoint = (LPoint + RPoint) // 2 # Provides the splitter index
        print(SortList[LPoint:MPoint])
        MergeSort(SortList, LPoint, MPoint) # Splits list in LHalf

        print(SortList[MPoint + 1:RPoint])
        MergeSort(SortList, MPoint + 1, RPoint) # Splits list in RHalf

        print(SortList[LPoint:RPoint])
        MergeSortMerge(SortList, LPoint, RPoint, MPoint) # Merges List together

# 5, 3, 1, 9
# 1, 3, 5, 9
# 1, 

def MergeSortRuntime(SortList):
    print(SortList)
    return MergeSort(SortList, 0, len(SortList))

"""
Calculate a pivot point
Sort items
Recurse
"""
def QuickSort(SortList, LRange, RRange):
    if LRange == RRange:
        pass
    else:
        Pivot = (LRange + RRange) // 2
        #i quit


class Stack:
    def __init__(self, Length):
        self.多大 = Length - 1
        self.Stack = [None for x in range(0, Length)]
        self.高 = 0

    def Peak(self):
        if self.Stack[self.高] != None:
            return self.Stack[self.高]

    def Push(self, PushItem):
        if self.高 < self.多大:
            self.高 += 1
            self.Stack[self.高] = PushItem
            return f"Pushed {PushItem}"
        else:
            return f"Stack overflow : {PushItem} lost"

    def Pop(self):
        if self.Stack[self.高] == None: # Implies that 高 already points to bottom
            return "Stack underflow : Unfortunately no infinite dupe glitch"
        else:
            self.Stack[self.高] = None
            if 0 < self.Stack:
                self.高 -= 1

class CircularQueue:
    def __init__(self, Length):
        self.MAXLENGTH = Length - 1
        self.Queue = [None for x in range(0, Length)]
        self.FPointer = 0
        self.BPointer = 0

    
    def Peak(self):
        if self.Queue[self.FPointer] != None:
            return self.Queue[self.FPointer]
        
    def Enqueue(self, EnqueueItem): 
        # If BPointer before LPointer and does not cross (even after enqueue), then enqueue
        # Assumes BPointer is after FPointer
        if (self.BPointer < (self.FPointer - 1)) or (self.BPointer < self.MAXLENGTH): 
            self.Queue[self.BPointer] = EnqueueItem
            self.BPointer += 1
        # Checks for 
        elif (self.BPointer == self.MAXLENGTH) and (0 < self.FPointer):
            self.BPointer = 0
            self.Queue[self.BPointer] = EnqueueItem

        if self.BPointer < self.MAXLENGTH:
            self.Queue[self.BPointer]
        elif self.BPointer == self.MAXLENGTH:
            self.BPointer

    def Dequeue(self):
        if self.Queue[self.FPointer] == None:
            return "Queue empty"
        else:
            self.Queue[self.FPointer] = None
            if self.FPointer < self.BPointer: # If equal to BP then does not increment to illegally cross
                self.FPointer += 1
            return "Dequeued successfully"

RandList = [r.randint(0, 10) for x in range(0, 10)]
NRandList = [x for x in range(0, 10)]
"""
for x in range(-1, 12):
    print(LinearSearch(x, RandList), RandList)
"""
"""
print(NRandList)
for x in range(-3, 15):
    print(x, BinarySearch(x, NRandList))
"""
"""
print(BubbleSort(RandList))
"""
"""
print(InsertionSort(RandList))
"""

#MergeSortRuntime(RandList)
QuickSort(RandList, 0, len(RandList) - 1)

# TODO : Create PowerPoint on DSA
# TODO : Test stack and queue
# TODO : Learn MergeSort implementation and implement it
# TODO : Relearn QuickSort