import pandas as pd
import matplotlib.pyplot as plt

# source file is inside data folder and named "aex.csv"
def readingData():
    df1_source = pd.read_csv(r"data/aex.csv")
    df2_source = pd.read_csv(r"data/nasdaq.csv")

    return [df1_source, df2_source]

def mergingData():
    dfList = readingData()

    df1_close = dfList[0][['Date', 'Close']]
    df2_close = dfList[1][['Date', 'Close']]

    df1_close['Close'] = df1_close['Close'] * 7.50

    df_total = pd.merge(df1_close, df2_close, how='outer', on='Date')

    return df_total