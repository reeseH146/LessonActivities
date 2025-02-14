def toBinary(val):
    temp = val
    bin = ""
    while temp > 0:
        if temp % 2 == 0:
            bin = "0" + bin
        elif temp % 2 == 1:
            bin = "1" + bin
        temp = temp // 2
    return bin
            
valid = False
while not valid:
    userInput = int(input("Enter a num to convert to a binary value : "))
    if 1 <= userInput <= 255:
        valid = True
        print(toBinary(userInput))