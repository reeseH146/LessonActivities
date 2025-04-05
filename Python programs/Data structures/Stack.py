class Queue:
    def __init__(self, Length):
        self.Queue = [None for x in range(Length)]
        self.LPointer = -1
        self.HPointer = -1
        self.MaxPointer = len(self.Stack) - 1
    
    #...
    def Peak(self):
        if self.Stack[self.HPointer]:
            print(f"{self.Stack[self.HPointer]} at index {self.HPointer}")
        else:
            print("ERROR : Stack empty")

    #...
    def Pop(self):
        if 0 < self.HPointer:
            self.Stack[self.HPointer] = None
            self.HPointer -= 1
        else:
            print("ERROR : Reached EOS") # End Of Stack
    #...
    def Push(self, PushItem):
        if self.HPointer < self.MaxPointer:
            self.HPointer += 1
            self.Stack[self.HPointer] = PushItem
        else:
            print("ERROR : Stack full")

End = False
QueueExample = Queue(5)
while not End:
    print("\n", QueueExample.Queue)
    Method = input("What method to do to the stack? : ")
    if Method == "Peak":
        QueueExample #...
    elif Method == "Pop":
        QueueExample #...
    elif Method == "Push":
        PushItem = input("Push Item : ")
        QueueExample #...
    else:
        print("ERROR : Not valid command")