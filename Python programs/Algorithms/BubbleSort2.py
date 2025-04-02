import random

JumbledList = [random.randint(0, 10) for x in range(10)]

def BubbleSort(ToSortList):
    SortedList = ToSortList
    Swapped = True
    Index = len(ToSortList)

    while (0 < Index) and (Swapped):
        Swapped = False
        Index -= 1
        for x in range(0, Index):
            if SortedList[x] > SortedList[x + 1]:
                SortedList[x], SortedList[x + 1] = SortedList[x + 1], SortedList[x]
                Swapped = True
    return SortedList

print(JumbledList)
print(BubbleSort(JumbledList))