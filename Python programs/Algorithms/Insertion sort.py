import random as r

UnsortedList = [r.randint(0, 10) for x in range(0, 1000000)]

def InsertionSort(List):
    for x in range(1, len(List)):
        num = x
        while List[num - 1] > List[num]:
            Temp = List[num]
            List[num] = List[num - 1]
            List[num - 1] = Temp
            num -= 1
            if num == 0:
                break
    return List


print(UnsortedList)
print(InsertionSort(UnsortedList))