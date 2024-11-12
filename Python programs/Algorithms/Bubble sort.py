# This is a bubble sort
import random as r

UnsortedList = [r.randint(0, 100) for x in range(250)]

def BubbleSort(List):
    # Loops through the list multiple times
    for x in range(len(List) - 1):
        # Bubbles up the list again
        for y in range((len(List) - 1)-x):
            # Swaps the element and the next element if not sorted
            if List[y] > List[y + 1]:
                Temp = List[y]
                List[y] = List[y + 1]
                List[y+1] = Temp
    return List

def EfficBubbleSort(List):
    # Loops through the list multiple times
    Sorted = True
    n = len(List)
    while Sorted and n > 0:
        n -= 1
        # Bubbles up the list again
        for y in range(n):
            # Swaps the element and the next element if not sorted
            if List[y] > List[y + 1]:
                Temp = List[y]
                List[y] = List[y + 1]
                List[y+1] = Temp
                Sorted = True
    return List

#print(UnsortedList)
#print(BubbleSort(UnsortedList))
CheckList = EfficBubbleSort(UnsortedList)
print(CheckList)
for x in range(len(CheckList) - 1):
    if CheckList[x] > CheckList[x + 1]:
        print("FAIL!!!", x, CheckList[x], CheckList[x + 1])
        break