# selectdata module

import pandas as pd

def readingData():
    df1_source = pd.read_csv(r"data/Alphavantage/daily_iex.ams.csv")
    df2_source = pd.read_csv(r"data/Alphavantage/daily_TSCO.LON.csv")

    return [df1_source, df2_source]

def fetchData(stock, date):
    dfList = readingData()

    # make pandas handle the date time more effectively
    dfList[0]['timestamp'] = pd.to_datetime(dfList[0]['timestamp'])
    dfList[1]['timestamp'] = pd.to_datetime(dfList[1]['timestamp'])

    # ensure the searched date is a Timestamp
    date_ts = pd.to_datetime(date)

    if stock == "AEX":
        series = dfList[0].loc[dfList[0]['timestamp'] == date_ts, 'close']
    elif stock == "London_Exchange":
        series = dfList[1].loc[dfList[1]['timestamp'] == date_ts, 'close']
    else:
        return None

    if series.empty:
        return None  # no match
    return series.iloc[0]  # return the close value (scalar)


