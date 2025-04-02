import random as r

Unsorted = [ x for x in range(10, 0, -1)]
print(Unsorted)

def Insertion(Unsorted):
    Sorted = Unsorted
    for x in range(1, len(Sorted)):
        CurrentItem = Sorted[x]
        y = x
        while (Unsorted[y - 1] > CurrentItem) and (y > 0): # While not sorted and not reached end of
            Sorted[y - 1], Sorted[y] = Sorted[y], Sorted[y - 1]
            y -= 1
    print(Sorted)

Insertion(Unsorted)