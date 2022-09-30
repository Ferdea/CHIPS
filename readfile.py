

def ReadChipsData():
    chipsData = {}
    file = open("chipsdata.txt")
    for s in file:
        chipName, chipIn, chipOut, chipTime, nandCount = s.split()
        chipsData[chipName] = list(chipIn.split(",")), list(chipOut.split(",")), int(chipTime), int(nandCount)
    file.close()
    return chipsData

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