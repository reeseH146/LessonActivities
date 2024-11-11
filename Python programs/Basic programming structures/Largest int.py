# Takes 2 integers and outputs the larget
Num1 = int(input("Enter first integer : "))
Num2 = int(input("Enter second integer : "))

if Num1 > Num2:
    print(f"Num1 : {Num1}, is bigger.")
elif Num2 > Num1:
    print(f"Num2 : {Num2}, is bigger.")
else:
    print("Both num are the same size")
