import random

UnsortedList = [random.randint(0, 10) for x in range(10)]

def LinearSearch(Lst, Target):
    CounterFound = 0
    ListOfIndexes = []
    for x in range(0, len(Lst) - 1):
        if Lst[x] == Target:
            CounterFound += 1
            ListOfIndexes.append(x)
            print(f"Found {Target} at {x} index.")
    print(f"Found {Target} {CounterFound} times at locations : {ListOfIndexes}")

print(UnsortedList)
LinearSearch(UnsortedList, 10)