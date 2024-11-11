# Generates the sorted list for a binary search and takes input of item to find
LVal = 0
HVal = 10
SortedList = [x for x in range(LVal, HVal)]
print(SortedList)

# Sets parameters for binary search
LBound = 0
HBound = 10

# Binary search
def BinarySearch(ItemFind, LB, HB):
    MP = 0
    Found = False
    while (not Found) and (LB <= HB):
        # Assigns the MP
        MP = LB + (HB - LB) // 2
        # Checks if the MP is the item
        if ItemFind == SortedList[MP]:
            Found = True
        # If Item is larger than the MP then Lower is MP + 1
        elif ItemFind > SortedList[MP]:
            LB = MP + 1
        # If Item is larger than the MP then Lower is MP - 1
        elif ItemFind < SortedList[MP]:
            HB = MP - 1
    return MP

# Tests all items in the array works with the binary search
for x in range(LBound, HBound):
    Midpoint = BinarySearch(x, LBound, HBound)
    print(f"We found {x} in SortedList at index {Midpoint} which is {SortedList[Midpoint]}")