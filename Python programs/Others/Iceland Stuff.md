# Task 1

![Dice Roll score algorithm flow chart](DiceRoll-Fchart.svg)

# Task 2
Create secret code from :
 - First 4 char of favorite colour
 - Followed by ASCII code of first character of favourite animal

Answer : 
Colour = input("What is your favourite colour? : ")
Animal = input("What is your favourite animal? : ")
Code = Colour[0:3] + str(ord(Animal[0]))
print(Code)

Cursed 1 line : 
print(input("What is your favourite colour? : ")[0:4] + str(ord(input("What is your favourite colour? : ")[0])))

# Task 3
Calculate mean height across specified range of inputs.

Answer :
TotalPatients = int(input("Enter total patients to calculate mean from : "))
SumHeight = 0
for x in range(TotalPatients):
    SumHeight += float(input("Height of current patient : "))
print(SumHeight / TotalPatients)