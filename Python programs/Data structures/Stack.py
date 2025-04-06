class Stack:
    def __init__(self, Length):
        self.Stack = [None for x in range(Length)]
        self.HPointer = -1
        self.MaxPointer = len(self.Stack) - 1
    
    def Peak(self):
        if self.Stack[self.HPointer]:
            print(f"{self.Stack[self.HPointer]} at index {self.HPointer}")
        else:
            print("ERROR : Stack empty")

    def Pop(self):
        if 0 <= self.HPointer:
            self.Stack[self.HPointer] = None
            self.HPointer -= 1
        else:
            print("ERROR : Reached EOS") # End Of Stack

    def Push(self, PushItem):
        if self.HPointer < self.MaxPointer:
            self.HPointer += 1
            self.Stack[self.HPointer] = PushItem
        else:
            print("ERROR : Stack full")

End = False
StackExample = Stack(5)
while not End:
    print(StackExample.Stack)
    Method = input("What method to do to the stack? : ")
    if Method == "Peak":
        StackExample.Peak()
    elif Method == "Pop":
        StackExample.Pop()
    elif Method == "Push":
        PushItem = input("Push Item : ")
        StackExample.Push(PushItem)
    elif Method == "Quit":
        raise SystemExit
    else:
        print("ERROR : Not valid command")