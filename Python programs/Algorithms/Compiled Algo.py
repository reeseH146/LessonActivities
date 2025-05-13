import random as MimikyuVMAX

#######################################################################
# ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### #
# --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- #
# ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### #
#######################################################################

# LinearSearch
def LinearSearch(RefList):
    SearchList = RefList
    # Defines search parameters
    SearchItem = int(input(f"{SearchList}\nSearch item : "))
    SearchLocations = []

    # Actual search - Goes through the list from start to finish
    for x in range(0, len(SearchList)):
        if SearchList[x] == SearchItem:
            SearchLocations.append(x)
    
    # Returns the results
    if len(SearchLocations) == 0:
        print(f"{SearchItem} not found in array.")
    else:
        print(f"{SearchItem} found at indexes : {SearchLocations}")

#######################################################################
# ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### #
# --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- #
# ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### #
#######################################################################

# BinarySearch
def BinarySearch(RefList):
    SearchList = sorted(RefList)
    # Defines search parameters
    SearchItem = int(input(f"{SearchList}\nSearch item : "))
    Comparison = 0

    # Actual search
    LBound = 0
    UBound = len(SearchList)
    Found = False
    SearchIndex = -1
    while (LBound <= UBound):
        Mid = (LBound + UBound) // 2
        Comparison += 1
        if SearchList[Mid] == SearchItem:
            SearchIndex = Mid
            Found = True
            break
        elif SearchList[Mid] < SearchItem:
            LBound = Mid + 1
        elif SearchItem < SearchList[Mid]:
            UBound = Mid - 1

    # Returns the results
    if not Found:
        print(f"{SearchItem} not found in search list.")
    else:
        print(f"{SearchItem} found at index : {SearchIndex}")
    print(f"Compared {Comparison} times.")

#######################################################################
# ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### #
# --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- #
# ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### #
#######################################################################

# BubbleSort
def BubbleSort(RefList):
    SortList = RefList
    print(f"Bubble sorting : {SortList}")
    Sorted = False
    Swap = 0
    Comparison = 0

    # Actual sorting
    for x in range(len(SortList) - 1, 0, -1): # Loops through the list extra times, decrements used for inner loop limit
        if Sorted: # Quits if there was no swapping
            break
        for y in range(0, x): # Bubbles up to limit of outer loop
            if SortList[y] > SortList[y+1]:
                Swap += 1
                SortList[y], SortList[y+1] = SortList[y+1], SortList[y]
                Sorted = False
    
    # Result
    print(f"Bubble sorted : {SortList}")
    print(f"Swapped {Swap} times.")


#######################################################################
# ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### #
# --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- #
# ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### #
#######################################################################

# InsertionSort
def InsertionSort(RefList):
    SortList = RefList
    print(f"Insertion sorting : {SortList}")
    Swap = 0

    # Sorting
    for x in range(1, len(SortList)):
        y = x
        while (SortList[y - 1] > SortList[y]) and (y > 0):
            Swap += 1
            SortList[y], SortList[y - 1] = SortList[y - 1], SortList[y]
            y -= 1

    print(f"Insertion sorted : {SortList}")
    print(f"Swapped {Swap} times.")

#######################################################################
# ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### #
# --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- #
# ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### #
#######################################################################

# Preset datasets
UnsortedPokemon= [""]
CustomValues = [10, 0, 20] # N, LValue, HValue
def RandomNumGen(Values):
    Temp = [MimikyuVMAX.randint(Values[1], Values[2]) for x in range(Values[0])]
    return Temp

# Main program
Running = True
while Running:
    # User inputs menu navigation
    NavChoice = input("""Change data set ; Linear search ; Binary search ; Bubble sort ; Insertion sort :
Please enter 1 of the following options as first 3 char: """)
    ArrayExample = RandomNumGen(CustomValues)
    match NavChoice.lower():
        case "lin":
            LinearSearch(ArrayExample)
        case "bin":
            BinarySearch(ArrayExample)
        case "bub":
            BubbleSort(ArrayExample)
        case "ins":
            InsertionSort(ArrayExample)
        case "quit":
            Running = False
        case _:
            print("Not valid option")
        
    print("\n")