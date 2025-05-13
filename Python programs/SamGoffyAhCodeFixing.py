# Linear search
def linear_search(target, data):
    iterations = 0
    found = False
    i = 0
    while found == False and i < len(data):
        iterations += 1
        if data[i] == target:
            found = True
        else:
            i += 1

    return i, iterations

# Binary search (REQUIRES SORTED LIST)
def binary_search(target, data):
    data.sort()  # Ensure data is sorted
    print(data)

    high = len(data)
    low = 0
    iterations = 0

    while True:
        iterations += 1
        mid = (high + low) // 2

        if data[mid] == target:
            return mid, iterations
        elif high == low:
            return -1, iterations
        elif data[mid] < target:
            low = mid + 1
        elif data[mid] > target:
            high = mid - 1

# Bubble sort
def bubble_sort(data):
    swaps = True
    m = len(data)
    iterations = 0
    while swaps:
        iterations += 1
        m -= 1
        swaps = False
        for i in range(m):
            if data[i] > data[i+1]:
                temp = data[i]
                data[i] = data[i+1]
                data[i+1] = temp
                swaps = True
   
    return data, iterations

# Insertion sort
def insertion_sort(data):
    iterations = 0
    for i in range(1, len(data)):
        temp = data[i]
        x = i
        while x > 0 and data[x-1] > temp:
            iterations += 1
            data[x] = data[x-1]
            x -= 1
        data[x] = temp
    return data, iterations









def take_input(accepted_values: list[int], msg: str) -> int:
    while True:
        i = int(input(msg))
        if i in accepted_values:
            return i
        else:
            print("This is not a valid input, please try again!")

### MAIN PROGRAM
running = True
magical_super_duper_list = [5, 1, 3, 9, 8, 2, 0, 9, 6]
while running:
    print(f"Currently using dataset: {", ".join(map(str, magical_super_duper_list))}")
    print(f"Please enter the algorithm you would like to use:\n1- Linear Search      2- Binary Search\n3- Bubble Sort        4- Insertion Sort\n5- Quit")
    inp = take_input([i for i in range(1, 6, 1)], "")
    copy = magical_super_duper_list.copy()

    match inp:
        case 1:
            t = int(input("Please enter the target to search for: "))
            index, effic = linear_search(t, copy)
            if index == -1: print(f"The item was not in the list, it took {effic} iterations to find this out.")
            else: print(f"Found item at index {index}, it took {effic} iterations to find.")
        case 2:
            t = int(input("Please enter the target to search for: "))
            index, effic = binary_search(t, copy)
            if index == -1: print(f"The item was not in the list, it took {effic} iterations to find this out.")
            else: print(f"Found item at index {index}, it took {effic} iterations to find.")
        case 3:
            res, effic = bubble_sort(copy)
            print(f"The array has been sorted! This took {effic} iterations.")
        case 4:
            res, effic = insertion_sort(copy)
            print(f"The array has been sorted! This took {effic} iterations.")
        case 5:
            print("Goodbye!")
            running = False
        case _:
            print("Eeerm, my input function doesnt work...")
    print(res)
    print(magical_super_duper_list)

    print("\n----------------------------\n")