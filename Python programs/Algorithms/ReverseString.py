Name = input("Enter your name : ")

print(Name[::-1])

for x in range(len(Name) - 1, -1, -1):
    print(f"{Name[x]}", end='')

# LMC Bubble Sort of 4 numbers
"""	LDA ARR1
	OUT
	LDA ARR2
	OUT
	LDA ARR3
	OUT
	LDA ARR4
	OUT
	LDA ARR5
	OUT

OLoop   LDA OLCurr
	ADD ONE
	OUT
	STA OLCurr
	LDA OLCurr
	SUB OLMax
	BRZ END
	BRA Comp1

Comp1	LDA ARR2
	SUB ARR1
	BRP Comp2
	LDA ARR1
	STA Temp
	LDA ARR2
	STA ARR1
	LDA Temp
	STA ARR2
Comp2   LDA ARR3
	SUB ARR2
	BRP Comp3
	LDA ARR2
	STA Temp
	LDA ARR3
	STA ARR2
	LDA Temp
	STA ARR3
Comp3   LDA ARR4
	SUB ARR3
	BRP Comp4
	LDA ARR3
	STA Temp
	LDA ARR4
	STA ARR3
	LDA Temp
	STA ARR4
Comp4   LDA ARR5
	SUB ARR4
	BRP OLoop
	LDA ARR4
	STA Temp
	LDA ARR5
	STA ARR4
	LDA Temp
	STA ARR5
	BRA OLoop

End     LDA ARR1
	OUT
	LDA ARR2
	OUT
	LDA ARR3
	OUT
	LDA ARR4
	OUT
	LDA ARR5
	OUT
	HLT



OLCurr  DAT 0
OLMax 	DAT 5
ONE	DAT 1

Temp    DAT 0
ARR1 	DAT 10
ARR2 	DAT 24
ARR3 	DAT 14
ARR4 	DAT 2
ARR5 	DAT 4

ARR6 	DAT 0
ARR7 	DAT 99
ARR8 	DAT 48
ARR9 	DAT 16
ARR10 	DAT 4"""