# Create a stack program
# Static class object
class Stack:
    def __init__(self, Size):
        self.TPointer = -1
        self.Stack = []
        self.MSize = Size
        for x in range (0, Size):
            self.Stack.append("Empty")

    # Returns value at top of the stack
    def Peak(self):
        # If there is anything in the stack then display
        if self.TPointer >= 0:
            print(self.Stack[self.TPointer])
        # Otherwise return nothing
        else:
            print("Stack empty")

    # Checks if there is anything to remove and does so if so
    def Pop(self):
        # Clears current position of any data and decrements pointer
        if self.TPointer >= 0:
            self.Stack[self.TPointer] = "Empty"
            self.TPointer -= 1
        else:
            print("Stack empty")

    # Checks if the stack is not full and inserts new data if so
    def Push(self, NItem):
        # Checks if there is space
        if self.TPointer + 1 < self.MSize: # Len returns amount of items, decrement offsets it to match 0 index. There still has to be 1 item left
            self.TPointer += 1
            self.Stack[self.TPointer] = NItem
        else:
            print("Stack full")

# Dynamic class object with linked list
#class LinkedList:
    


# Main program
Example = Stack(5)
Example.Peak()
Example.Pop()
Example.Push(5)
Example.Push(8)
Example.Push(1)
Example.Push(5)
Example.Push(2)
Example.Push(2)
Example.Peak()
Example.Pop()
Example.Peak()
Example.Pop()
Example.Peak()
Example.Pop()
Example.Peak()
Example.Pop()
Example.Peak()
Example.Pop()
Example.Peak()
Example.Pop()
Example.Peak()
Example.Pop()

