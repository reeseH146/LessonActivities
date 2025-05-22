def FizzBuzz(Number):
    if (Number % 3 == 0) and (Number % 5 == 0):
        print("FizzBuzz")
    elif (Number % 3 == 0):
        print("Fizz")
    elif (Number % 5 == 0):
        print("Buzz")
    else:
        print(f"{x}")

for x in range(1, 31):
    FizzBuzz(x)

"""OuterLoop LDA OLCurrent
BRZ Ending
SUB 1




OLCurrent DAT 5
ILCurrent DAT 0
ILMax DAT 

ARR1 DAT 10
ARR2 DAT 24
ARR3 DAT 14
ARR4 DAT 2
ARR5 DAT 4

ARR6 DAT 0
ARR7 DAT 99
ARR8 DAT 48
ARR9 DAT 16
ARR10 DAT 4"""