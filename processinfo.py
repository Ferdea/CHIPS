

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