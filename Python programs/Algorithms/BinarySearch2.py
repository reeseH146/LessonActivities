SortedList = [x for x in range(10)]

def BinarySearch(Lst, Target):
    Lb = 0
    Ub = len(Lst) - 1
    Mp = (Lb + Ub) // 2
    Found = False
    while (not Found) or (Lb < Ub):
        if Lst[Mp] == Target:
            print(f"Found {Target} at {Mp}")
            Found = True
            break
        elif Lst[Mp] < Target:
            Lb = Mp + 1
            Mp = (Lb + Ub) // 2
        elif Target < Lst[Mp]:
            Ub = Mp - 1
            Mp = (Lb + Ub) // 2
    if not Found:
        print("Not in list")

print(SortedList)
for x in range(0, len(SortedList)):
    BinarySearch(SortedList, 100)