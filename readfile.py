

def GetChipName():
    return input("Введите название чипа: ")

def RemovePreffixBeforeChar(s, char):
    if char in s:
        s = s[s.find(char) + 1::]
    return s

def RemoveSuffixAfterChar(s, char):
    if char in s:
        s = s[:s.find(char):]
    return s

def ImproveString(s):
    while "[" in s and "]" in s:
        s = s[:s.find("["):] + s[s.find("]") + 1::]
    s = RemoveSuffixAfterChar(s, "/")
    s = RemoveSuffixAfterChar(s, "*")
    s = RemoveSuffixAfterChar(s, ";")
    s = RemoveSuffixAfterChar(s, "\n")
    s = RemoveSuffixAfterChar(s, ")")
    s = s.replace("(", "|")
    s = s.replace(" ", "")
    if s.isspace() or "{" in s or "}" in s:
        return [""]
    if "IN" in s:
        return ["IN:"] + ImproveString(RemovePreffixBeforeChar(s, "N"))
    if "OUT" in s:
        return ["OUT:"] + ImproveString(RemovePreffixBeforeChar(s, "T"))
    return [s]

def GetSimplifiedFile(fileName):
    file = open(fileName)
    stringArray = []
    for s in file:
        improveString = ImproveString(s)
        if improveString != [""]:
            stringArray += improveString
    file.close()
    return stringArray

def SplitChip(s):
    chipName, ioPut = s.split("|")
    ioPut = ioPut.split(",")
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

def GetInfoAboutChip(s, chipsData):
    chipName, ioPut = SplitChip(s)
    if chipName not in chipsData.keys():
        exit(chipName)
    inputData = GetInput(chipName, ioPut, chipsData)
    outputData = GetOutput(chipName, ioPut, chipsData)
    elapsedTime = chipsData[chipName][2]
    chipUsed = chipsData[chipName][3]
    return inputData, outputData, elapsedTime, chipUsed

def SplitSimpleFile(file, chipsData):
    result = [[], [], []] # 0 - IN, 1 - OUT, 2 - PARTS
    state = -1
    for s in file:
        if s in ("IN:", "OUT:", "PARTS:"):
            state += 1
        else:
            if state == 2:
                result[state].append(GetInfoAboutChip(s, chipsData))
            else:
                for substring in s.split(","):
                    if substring != "":
                        result[state].append(substring)
    return result

def CalculatePrice(data):
    price = 0
    for i in range(len(data[2])):
        price += data[2][i][3]
    return price

def CalculateTime(data):
    timeData = {x: 0 for x in data[0]}
    for i in range(len(data[2])):
        inputTime = []
        for j in range(len(data[2][i][0])):
            inputTime.append(timeData[data[2][i][0][j]])
        deltaTime = max(inputTime) + data[2][i][2]
        for j in range(len(data[2][i][1])):
            timeData[data[2][i][1][j]] = deltaTime
    return max(timeData.values())

def ReadChip(chipsData):
    fileName = f'chipFiles/{GetChipName()}.hdl'
    file = GetSimplifiedFile(fileName)
    readResult = SplitSimpleFile(file, chipsData)

    print("Время чипа в нандах: ", CalculateTime(readResult))
    print("Кол-во нандов: ", CalculatePrice(readResult))