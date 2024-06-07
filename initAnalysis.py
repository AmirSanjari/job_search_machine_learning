def initAnalysis(dataFrame):
    placed = dataFrame[dataFrame["placed"] > 0]
    notPlaced = dataFrame[dataFrame["placed"] < 1]

    targetPlaced = placed.iloc[:,3]
    dataPlaced = placed.iloc[:,4:]

    targetNotPlaced = notPlaced.iloc[:,3]
    dataNotPlaced = notPlaced.iloc[:,4:]

    return targetPlaced, dataPlaced, targetNotPlaced, dataNotPlaced