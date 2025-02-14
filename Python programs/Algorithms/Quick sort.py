# Quick sort program
import random as r

UnsortedList = [r.randint(0, 1000000) for x in range(999999)]
#284713965
#248713965
#241783965
#241387965
#241357968

#2143 5 7968
#1243 5 7968
def Partit(SortList, Start, End):
    Pivot = SortList[End]
    j = Start - 1
    # Continues sorting until it reaches the pivot
    for i in range(Start, End):
        # Swaps smaller item with larger item and continues
        if SortList[i] <= Pivot:
            j += 1
            SortList[i], SortList[j] = SortList[j], SortList[i]
            print(SortList, 1)
    # Swaps pivot and last larger item
    j += 1
    SortList[j], SortList[End] = SortList[End], SortList[j]
    print(SortList, 2)
    return j

def QuickSort(SortList, Start = 0, End = None):
    # Allows for
    if End is None:
        End = len(SortList) - 1
    if Start < End:
        Pivot = Partit(SortList, Start, End)
        # Recurses left/right half
        QuickSort(SortList, Start, Pivot - 1)
        print("Left recurse end")
        QuickSort(SortList, Pivot + 1, End)
        print("Right recurse end")

print(UnsortedList)
QuickSort(UnsortedList, 0, None)
print(UnsortedList)
