import io

def Read(FileName):
    Temp = []
    # Opens the file
    TXTFile = open(FileName, "r")
    RawData = TXTFile.read()
    TXTFile.close()

    Temp = RawData.split(", ")
    for x in range(0, len(Temp)):
        Temp[x] = int(Temp[x])

    return Temp

def Average(DataSet):
    Overall = 0
    Count = 0

    while Count < len(DataSet):
        Overall += DataSet[Count]
        Count +=1

    return Overall/Count

FileDataSet = Read(r"C:\Users\Hi-bu\Reese\3 - Cloned projects\LessonActivities\Python programs\File\Example1.txt")
AverageSteps = Average(FileDataSet)
print(AverageSteps)