
def ReadChipsData():
    chipsData = {}
    file = open("chipsdata.txt")
    for s in file:
        chipName, chipIn, chipOut, chipTime, nandCount = s.split()
        chipsData[chipName] = list(chipIn.split(",")), list(chipOut.split(",")), int(chipTime), int(nandCount)
    file.close()
    return chipsData

def RemoveComments(s):
    return s.split("/")[0].split("*")[0]

def RemoveBrackets(s):
    while "[" in s and "]" in s:
        s = s[:s.find("["):] + s[s.find("]") + 1::]
    return s

def RemoveSpaces(s):
    return s.replace(" ", "")

def splitChip(s):
    s = RemoveBrackets(s)
    s = RemoveSpaces(s)
    chipName, ioPut = s.split("(")
    ioPut = ioPut.split(")")[0].split(",")
    return chipName, ioPut

def GetInput(chipName, ioPut, chipsData):
    inputData = []
    for i in chipsData[chipName][0]:
        for j in ioPut:
            if j.split("=")[0] == i:
                inputData.append(j.split("=")[1].split("[")[0])
    return inputData

def GetOutput(chipName, ioPut, chipsData):
    outputData = []
    for i in chipsData[chipName][1]:
        for j in ioPut:
            if j.split("=")[0] == i:
                outputData.append(j.split("=")[1])
    return outputData

def GetInfo(s, chipsData):
    chipName, ioPut = splitChip(s)
    if chipName not in chipsData.keys():
        exit(chipName)
    inputData = GetInput(chipName, ioPut, chipsData)
    outputData = GetOutput(chipName, ioPut, chipsData)
    elapsedTime = chipsData[chipName][2]
    chipUsed = chipsData[chipName][3]
    return inputData, outputData, elapsedTime, chipUsed


inputData = []
outputData = []
elapsedTime = []
chipUsed = 0

chipsData = ReadChipsData()
fileName = input("Введи название чипа: ")
with open("chipFiles/" + fileName + ".hdl") as file:
    # 0 - чтение комментариев, 1 - IN, 2 - OUT, 3 - PARTS
    state = 0
    IN = ["true", "false"]
    OUT = []
    for s in file:
        s = RemoveBrackets(RemoveComments(s))
        if state == 0:
            if "IN" in s:
                s = s.replace("IN", "")
                state = 1
        if state == 1:
            s = RemoveSpaces(s.replace(";", "").replace("\n", ""))
            IN += list(s.split(","))
            if "OUT" in s:
                state = 2
                s = s.replace("OUT", "")
        if state == 2:
            s = RemoveSpaces(s.replace(";", "").replace("\n", ""))
            OUT += list(s.split(","))
            if "PARTS" in s:
                state = 3
                continue
        if state == 3 and not s.isspace() and "}" not in s:
            data = GetInfo(s, chipsData)
            inputData.append(data[0])
            outputData.append(data[1])
            elapsedTime.append(data[2])
            chipUsed += data[3]

timeData = {x: 0 for x in IN}
for i in range(len(inputData)):
    inputTime = []
    for j in range(len(inputData[i])):
        inputTime.append(timeData[inputData[i][j]])
    deltaTime = max(inputTime) + elapsedTime[i]
    for j in range(len(outputData[i])):
        timeData[outputData[i][j]] = deltaTime

print("Время чипа в нандах: ", max(timeData.values()))
print("Кол-во нандов: ", chipUsed)