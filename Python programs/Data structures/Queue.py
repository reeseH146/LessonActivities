# Queue data structure implementation, not entirely sure if I know eveything about the queue though
class Queue:
    def __init__(self, Length):
        self.Queue = [None for x in range(Length)] # Actual queue object which stores the data
        self.LPointer = 0 # Stores pointer of the first item
        self.MaxPointer = -1 # Stores pointer of the last item
    
    def Peak(self):
        if self.Queue[self.LPointer]: # Checks there is something at LPoint/LItem
            print(f"{self.Queue[self.LPointer]} at index {self.LPointer}")
        else:
            print("ERROR : Queue empty")

    def Dequeue(self):
        if self.Queue[self.LPointer]: # Checks LPoint has something to remove
            self.Queue[self.LPointer] = None # Removes item
            self.LPointer += 1 # Moves LPointer up
            if self.LPointer == self.MaxPointer: # Resets queue if it is empty
                self.LPointer = -1
                self.MaxPointer = -1
        else:
            print("ERROR : Reached EOQ") # End Of Queue

    def Enqueue(self):
        EnqueueItem = input("Enque Item : ")
        if self.MaxPointer < len(self.Queue) - 1: # Checks there is available space in the queue
            self.MaxPointer += 1 # Increases pointer of highest position
            self.Queue[self.MaxPointer] = EnqueueItem # Adds item to queue
        else:
            print("ERROR : Queue full on top")

# ### --- ### --- ### --- ### --- ### --- ### --- ### #
# --- ### --- ### --- ### --- ### --- ### --- ### --- #
# ### --- ### --- ### --- ### --- ### --- ### --- ### #

class CircularQueue:
    def __init__(self, Length):
        self.Queue = [None for x in range(Length)] # Queue object
        self.LPointer = 0 # Tracks start of queue
        self.MaxPointer = -1 # Tracks end of queue
    
    def Peak(self):
        if self.Queue[self.LPointer]: # Checks there is something at start of queue
            print(f"{self.Queue[self.LPointer]} at index {self.LPointer}")
        else:
            print("ERROR : Queue empty")

    # Remove by ... : 
    # Must not cross with start
    # Next must not be full
    def Dequeue(self):
        if self.Queue[self.LPointer]: # Checks LPoint has something to remove
            self.Queue[self.LPointer] = None # Removes item
            if self.LPointer == (len(self.Queue) - 1): # Checks if at last index
                self.LPointer = 0
            else: # Not at last pointer
                self.LPointer += 1
        else:
            print("ERROR : Reached EOQ") # End Of Queue

    # Checks if pointer is last
        # Checks next space is not full (if full then last pointer will also be there so no need to check)
            # Moves item and pointer there
    # Pointer is not last
        # Checks next space is not full
            # Moves item and pointer there
    def Enqueue(self):
        EnqueueItem = input("Enque Item : ")
        if self.MaxPointer == (len(self.Queue) - 1):
            self.MaxPointer = 0
            self.Queue[self.MaxPointer] = EnqueueItem
        elif self.MaxPointer < (len(self.Queue) - 1):
            self.MaxPointer += 1
            self.Queue[self.MaxPointer] = EnqueueItem
        else:
            print("ERROR : Queue full on top")

# ### --- ### --- ### --- ### --- ### --- ### --- ### #
# --- ### --- ### --- ### --- ### --- ### --- ### --- #
# ### --- ### --- ### --- ### --- ### --- ### --- ### #

QueSize = 5
QueueType = input("Would you like to play with a normal queue or a circular queue? : ")
if QueueType == "Queue":
    QueueExample = Queue(QueSize) 
elif QueueType == "CircularQ":
    QueueExample = CircularQueue(QueSize)

# Simulates queue and circular queue operations
End = False
while not End:
    print("\n", QueueExample.Queue)
    Method = input("What method to do to the Queue? : ")
    if (Method == "Peak") or (Method == "P"):
        QueueExample.Peak()
    elif (Method == "Dequeue") or (Method == "D"):
        QueueExample.Dequeue()
    elif (Method == "Enqueue") or (Method == "E"):
        QueueExample.Enqueue()
    elif Method == "Quit":
        raise SystemExit
    else:
        print("ERROR : Not valid command")