import pandas as pd
import json

def readData():
    with open("data/raw/ABN.AS_marketstack.json") as f:
        rawABN = json.load(f)
    with open("data/raw/PHIA.AS_marketstack.json") as f:
        rawPHI = json.load(f)

    data_list1 = rawABN["data"]
    df1 = pd.DataFrame(data_list1)

    data_list2 = rawPHI["data"]
    df2 = pd.DataFrame(data_list2)  

    df_merged = manData(df1, df2)

    return df_merged

def manData(df1, df2):
    df_filtered = df1[df1['date'] >= '2025-04-01']
    df_filtered2 = df2[df2['date'] >= '2025-04-01']

    df_total = pd.merge(df_filtered, df_filtered2, how='outer', on='date')
    
    return df_total