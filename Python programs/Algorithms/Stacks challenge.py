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

class Stack:
    def __init__(self, MaxStack):
        self.Stack = [None for x in range(MaxStack)]
        self.Max = 0

    def Peak(self):
        print(self.Stack[self.Max])
    
    def Pop(self):
        if self.Max > 0:
            self.Stack[self.Max] = None
            self.Max -= 1
        else:
            raise OverflowError
    
    def Push(self, PushItem):
        if self.Max < len(self.Stack) - 2:
            self.Stack[self.Max] = PushItem
            self.Max += 1
        else:
            raise OverflowError

TheStack = Stack(100)

def PushToStack(Message):
    for Characters in Message:
        TheStack.Push(Characters)
    
    print(TheStack.Stack)

PushToStack("IPlayPokemonGoEveryday")