from readfile import *
from processinfo import *
from calculate import *


def main():
    chipsData = ReadChipsData()
    fileName = f'chipFiles/{GetChipName()}.hdl'
    file = GetSimplifiedFile(fileName)

    inputInfo, outputInfo, chipsInfo = SplitSimpleFile(file, chipsData)

    print("Время чипа в нандах: ", CalculateTime(inputInfo, chipsInfo))
    print("Кол-во нандов: ", CalculatePrice(chipsInfo))


if __name__ == "__main__":
    main()