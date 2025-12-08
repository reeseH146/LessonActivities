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
        if SearchSet[MPoint] == SearchObj:
            return MPoint
        elif SearchSet[MPoint] < SearchObj:
            LPoint = MPoint + 1
        elif SearchObj < SearchSet[MPoint]:
            RPoint = MPoint - 1
        MPoint = (LPoint + RPoint) // 2
    return -1

# ಥ_ಥ
def InsertionSort(SortList):
    for x in range(1, len(SortList)):
        SwapItem = SortList[x]
        CompareMarketDotComIndex = x
        Swap = False
        while (SwapItem < SortList[CompareMarketDotComIndex - 1]) and (0 < CompareMarketDotComIndex): # Moves new position down each iteration if it is smaller then the item before it
            CompareMarketDotComIndex -= 1
            Swap = True
        if Swap:
            SortList.pop(x) # Removes from position
            SortList.insert(CompareMarketDotComIndex, SwapItem) # Replaces in new space
            Swap = False
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

"""
def MergeSort

class Stack

class Queue
"""

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