# Function to convert denary number to binary number with unpadded 0
def toBinary(val):
    bin = "" # Stores the result of binary value converison
    while val > 0: # Loops through until denary number is greater than 0
        if val % 2 == 0: # If MOD 2 returns no remainders then adds 0 to the start of bin string since the output is given in reverse order
            bin = "0" + bin
        elif val % 2 == 1: # If MOD 2 returns remainder of 1 then adds 1
            bin = "1" + bin
        val = val // 2 # Halves the number rounded down, each place value in a binary number is double the previous
    return bin

# User input and validation for denary numbers to convert to binary
userInput = -1 # Default case to promote loop to run
while (1 > userInput) or (userInput > 255): # Denary number has to be integer between 1 and 255, otherwise continue asking for user input
    userInput = int(input("Enter a num to convert to a binary value : ")) # Asks for a integer denary number
# Prints result of converting denary number input to binary number from "toBinary" function
print(toBinary(userInput))

# Commented out code which tested the toBinary function with numbers ranging from 1 to 255
"""for i in range(1, 256):
    print(toBinary(i))"""