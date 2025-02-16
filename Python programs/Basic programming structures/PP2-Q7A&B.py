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

userInput = -1
while (1 > userInput) or (userInput > 255):
    userInput = int(input("Enter a num to convert to a binary value : "))
print(toBinary(userInput))

"""for i in range(1, 256):
    print(toBinary(i))"""