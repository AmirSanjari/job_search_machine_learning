import pandas as pd 

def loadData():
    dataset = pd.read_csv("../Dataset/data.csv")
    dataFrame = pd.DataFrame(dataset)
    return dataFrame
