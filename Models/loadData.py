import pandas as pd 

def loadData():
    """
    Load data from a CSV file into a pandas DataFrame.

    This function reads data from a CSV file located at '../Dataset/data.csv' 
    and returns it as a pandas DataFrame.

    Returns:
        pd.DataFrame: A DataFrame containing the data from the CSV file.
    """
    
    dataset = pd.read_csv("../Dataset/data.csv")
    dataFrame = pd.DataFrame(dataset)
    return dataFrame
