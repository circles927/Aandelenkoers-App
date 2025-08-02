# createplot module

import pandas as pd

def readingData():
    df1_source = pd.read_csv(r"data/Alphavantage/daily_iex.ams.csv")
    df2_source = pd.read_csv(r"data/Alphavantage/daily_TSCO.LON.csv")

    return [df1_source, df2_source]

def mergingData():
    dfList = readingData()

    # make pandas handle the date time more effectively
    dfList[0]['timestamp'] = pd.to_datetime(dfList[0]['timestamp'])
    dfList[1]['timestamp'] = pd.to_datetime(dfList[1]['timestamp'])

    # filter the dataframes to only include rows after a certain date
    filtered_df1 = dfList[0].loc[(dfList[0]['timestamp'] >= '2025-01-20')]
    filtered_df2 = dfList[1].loc[(dfList[1]['timestamp'] >= '2025-01-20')]

    # select only the timestamp and close columns from each dataframe
    df1_close = filtered_df1[['timestamp', 'close']].copy()
    df2_close = filtered_df2[['timestamp', 'close']].copy()

    # bring up the first graph next to the second graph
    df1_close['close'] = df1_close['close'] * 200

    # merge the two dataframes on the timestamp column into one dataframe
    df_total = pd.merge(df1_close, df2_close, how='outer', on='timestamp')

    return df_total