from readfile import *
def ReadChipsData():
    chipsData = {}
    file = open("chipsdata.txt")
    for s in file:
        chipName, chipIn, chipOut, chipTime, nandCount = s.split()
        chipsData[chipName] = list(chipIn.split(",")), list(chipOut.split(",")), int(chipTime), int(nandCount)
    file.close()
    return chipsData

def main():
    chipsData = ReadChipsData()
    ReadChip(chipsData)

if __name__ == "__main__":
    main()