# Y12 Programming 2 doc
def ReadMessage(FileName):
    MessageFile = open(FileName)
    Message = MessageFile.readline()
    MessageFile.close()
    return Message

#######################################################################
# ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### #
# --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- #
# ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### #
#######################################################################

class Stack: # Stack class
    def __init__(self, MaxStack):
        self.Stack = [None for x in range(MaxStack)] # Tracks items in the stack, fixed size so len is defined by default
        self.Max = 0 # Tracks of the top item in the stack

    def Peak(self): # Looks at the start of the stack
        print(self.Stack[self.Max])
    
    def Pop(self): # Removes the top item in the stack if there is still anything to pop
        if self.Max > 0:
            self.Stack[self.Max] = None
            self.Max -= 1
        else:
            raise OverflowError
    
    def Push(self, PushItem): # Adds item onto the top of the stack if it doesn't exceed the stack
        if self.Max < len(self.Stack) - 2:
            self.Stack[self.Max] = PushItem
            self.Max += 1
        else:
            raise OverflowError

TheStack = Stack(50) # Creates the stack with a size of 50

def PushToStack(Message): # Function to push each character onto a stack
    for Characters in Message: # Loops through string
        TheStack.Push(Characters) # Pushes string char to stack
    
    print(TheStack.Stack)

#######################################################################
# ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### #
# --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- #
# ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### #
#######################################################################

"""
 - Read each character from the top of the stack
 - Convert character to corresponding ASCII value
 - Subtract 10 from the ASCII value
 - Convert new ASCII value into ASCII character
 - Store the new characters into a string until the stack is empty
 - Open a file to write the string into the file and close the file, this string is in reverse order by default since it has been reversed from reading
"""

"""
1000
59
2
13
22
20
"""

# Y12 Programming 3 doc
"""
Sequence - The program should go through different processes/functions to enter data to hire a function room in order since some of the data may be dependant on another such as the data before which room to book since some rooms may have been already booked on a specific date
Condition - The program will check through which rooms are available on which dates and then return it to the customer to select the room they want to book
"""
NumPlayers = ""
while (not NumPlayers.isnumeric()) and (0 <= NumPlayers <= 10):
    NumPlayers = input("Number of Players : ")
NumPlayers = int(NumPlayers)

Players = []
for x in range(0, NumPlayers):
    Players.append([input(f"Please enter player {x + 1} name : "), 0])

for x in range(1, 9):
    print(f"Round {x}")
    for y in range(0, len(Players)):
        Players[y][1] += input(f"Player {y + 1}")

Total = 0
for x in range(0, len(Players)):
    print(f"{Players[x][0]} scored {Players[x][1]}")
    Total += Players[x][1]
print(f"Average is {Total / 8}")

