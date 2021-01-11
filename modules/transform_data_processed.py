import pandas as pd, numpy as np

def crossjoin(column_1,column_2):
    column_1 = pd.DataFrame(column_1.unique())
    column_2 = pd.DataFrame(column_2.unique())
    column_1['key'], column_2['key'] = 0,0
    return column_1.merge(column_2,on='key').drop(columns = 'key')

def by_code(df,station_code):
    df_station = df[df['station_code'] == station_code]
    df_station.columns = list(map(lambda x: station_code+' - '+x,df_station.columns))
    return df_station