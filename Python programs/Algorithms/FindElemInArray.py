x# Algorithm which figures out how many green sweets in an array of sweets

# Main Program
SweetsArray = ["Green", "Red", "Indigo", "Green", "Aquamarine", "Ruby", "Prismarine", "Green", "Green", "Lavender", "Green", "Green"]
TotalGreenSweets = 0
for items in SweetsArray:
    if items == "Green":
        TotalGreenSweets += 1
print(TotalGreenSweets)