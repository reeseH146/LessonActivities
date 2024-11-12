# This is a bubble sort
import random as r

UnsortedList = [x for x in range(0, 250000)]

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
    n = len(List) - 1
    while Sorted and n > 0:
        # Bubbles up the list again
        for y in range(n):
            n -= 1
            # Swaps the element and the next element if not sorted
            if List[y] > List[y + 1]:
                Temp = List[y]
                List[y] = List[y + 1]
                List[y+1] = Temp
                Sorted = True
    return List

print(UnsortedList)
print(BubbleSort(UnsortedList))
#print(EfficBubbleSort(UnsortedList))