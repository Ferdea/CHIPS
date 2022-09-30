

def CalculatePrice(chipsInfo):
    price = 0
    for i in range(len(chipsInfo)):
        price += chipsInfo[i][3]
    return price


def CalculateTime(inputInfo, chipsInfo):
    timeData = {x: 0 for x in inputInfo}
    for i in range(len(chipsInfo)):
        inputTime = []
        for j in range(len(chipsInfo[i][0])):
            inputTime.append(timeData[chipsInfo[i][0][j]])
        deltaTime = max(inputTime) + chipsInfo[i][2]
        for j in range(len(chipsInfo[i][1])):
            timeData[chipsInfo[i][1][j]] = deltaTime
    return max(timeData.values())