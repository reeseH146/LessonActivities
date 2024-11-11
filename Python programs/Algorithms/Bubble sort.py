# This is a bubble sort
import random as r

UnsortedList = [r.randint(0, 10) for x in range(19)]

def BubbleSort(List):
    # Loops through the list multiple times
    for x in range(len(List) - 1):
        # Bubbles up the list again
        for y in range(len(List) - 1):
            # Swaps the element and the next element if not sorted
            if List[y] > List[y + 1]:
                Temp = List[y]
                List[y] = List[y + 1]
                List[y+1] = Temp
    return List



print(BubbleSort(UnsortedList))