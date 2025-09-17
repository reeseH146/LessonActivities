class Dog:
    def __init__(self, Name, Breed, Age, DoB):
        self.Name = Name
        self.Breed = Breed
        self.Age = Age
        self.DOB = DoB

    def GetName(self):
        return self.Name

    def GetBreed(self):
        return self.Breed

    def GetAge(self):
        return self.Age
    
    def GetDOB(self):
        return self.DOB
    
    def Bark(Type):
        if Type == 0:
            print("Bark")
        elif Type == 1:
            print("Bark!!")
        
Pet = Dog("Morty", "Chuwawa", 3, "11/7/2001")


# Do we have to submit this to Sir? This OOP seems pointless