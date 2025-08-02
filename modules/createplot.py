# module 1

import pandas as pd

def readingData():
    df1_source = pd.read_csv(r"data/Alphavantage/daily_iex.ams.csv")
    df2_source = pd.read_csv(r"data/Alphavantage/daily_TSCO.LON.csv")

    return [df1_source, df2_source]

def mergingData():
    dfList = readingData()

    dfList[0]['timestamp'] = pd.to_datetime(dfList[0]['timestamp'])
    dfList[1]['timestamp'] = pd.to_datetime(dfList[1]['timestamp'])

    filtered_df1 = dfList[0][dfList[0]['timestamp'] >= '2025-01-15']
    filtered_df2 = dfList[1][dfList[1]['timestamp'] >= '2025-01-15']

    df1_close = filtered_df1[['timestamp', 'close']]
    df2_close = filtered_df2[['timestamp', 'close']]

    df1_close['close'] = df1_close['close'] * 200

    df_total = pd.merge(df1_close, df2_close, how='outer', on='timestamp')

    return df_total