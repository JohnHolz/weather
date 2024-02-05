import pandas as pd
import sys
import numpy as np
from jh_utils.data.pandas.sql import get_sql_table

def sql_string_vector(ls):
    return '( '+ ','.join(list(map(lambda x: "'"+x+"'",ls))) + ')'

def get_raw_data(stations, start_date, engine, region = 'southeast'):
    query = f'select * from raw.{region} r where r.station_code in {sql_string_vector(stations)} and r."Data" >' + f"'{start_date}';"
    df = get_sql_table(query,engine)
    return df

def crossjoin(column_1,column_2,same_column = True):
    """
    Create a crossjoin dataframe based on 2 columns
    """
    column_1 = pd.DataFrame(column_1.unique())
    column_2 = pd.DataFrame(column_2.unique())
    column_1['key'], column_2['key'] = 0,0
    date_time = column_1.merge(column_2,on='key').drop(columns = 'key')
    date_time.columns = ['data','hora']
    date_time.sort_values(['data','hora'],inplace=True)
    date_time.reset_index(inplace=True,drop=True)
    if same_column:
        return pd.DataFrame(pd.to_datetime(date_time['data'] + ' ' +  date_time['hora']), columns=['date_time'])
    
    date_time['data'] = pd.to_datetime(date_time['data'])
    return date_time

def by_code(df,station_code):
    """
        Create a dataframe filtered by station_code and rename the columns by the status code
    """
    df_station = df[df['station_code'] == station_code]
    df_station.columns = list(map(lambda x: station_code+' - '+x,df_station.columns))
    return df_station

def process_raw(df):
    """
    ! create the final dataset -> crossjoin between hour and date
    ! rename the columns
    ! combine hour and date columns -> transform to date_time
    ! append columns data from all stations to keep the data granularity
    ! remove not useful columns
    ! return table 
    """

    df.columns = renamed_columns
    df['date_time'] = pd.to_datetime(df['data'] + ' ' +  df['hora'])
    df_models = crossjoin(df['data'],df['hora'])
    df = df.drop(['data','hora'],axis=1)
    for i in df.station_code.unique():
        df_temp = by_code(df,i)    
        df_models = df_models.merge(df_temp, 
                    how='left', 
                    right_on  = df_temp.iloc[:,-1].name,
                    left_on = 'date_time')
    
    ## ! remove not useful columns
    df_models = df_models[df_models.columns.drop(list(df_models.filter(regex='- date_time')))]
    df_models = df_models[df_models.columns.drop(list(df_models.filter(regex='- station_code')))]
    df_models = df_models[df_models.columns.drop(list(df_models.filter(regex='- station')))]
    df_models = df_models[df_models.columns.drop(list(df_models.filter(regex='- state')))]
    df_models = df_models[df_models.columns.drop(list(df_models.filter(regex='- region')))]
    df_models = df_models[df_models.columns.drop(list(df_models.filter(regex='- radiacao global')))]
    df_models = df_models[df_models.columns.drop(list(df_models.filter(regex='- latitude')))]
    df_models = df_models[df_models.columns.drop(list(df_models.filter(regex='- longitude')))]
    df_models = df_models[df_models.columns.drop(list(df_models.filter(regex='- height')))]
    return df_models

def clean_na(df):
    ## Na from dataset
    na_value = -9999

    df.index = df['date_time']
    df = df.drop(columns=['date_time'])

    df = df.replace(to_replace=na_value,value=np.NaN)
    df = df[df.iloc[:,1].first_valid_index():]
    df = df.fillna(method='ffill')
    return df

def make_dataset(stations, start_date, engine):
    df = get_raw_data(stations, start_date, engine)
    df = process_raw(df)
    df = clean_na(df)
    return df

renamed_columns = ['data','hora','precipitacao total, horario (mm)',
    'pressao atmosferica ao nivel da estacao, horaria (mb)',
    'pressao atmosferica max. na hora ant. (aut) (mb)',
    'pressao atmosferica min. na hora ant. (aut) (mb)',
    'radiacao global (kj/m2)',
    'temperatura do ar - bulbo seco, horaria (°c)',
    'temperatura do ponto de orvalho (°c)',
    'temperatura maxima na hora ant. (aut) (°c)',
    'temperatura minima na hora ant. (aut) (°c)',
    'temperatura orvalho max. na hora ant. (aut) (°c)',
    'temperatura orvalho min. na hora ant. (aut) (°c)',
    'umidade rel. max. na hora ant. (aut) (%)',
    'umidade rel. min. na hora ant. (aut) (%)',
    'umidade relativa do ar, horaria (%)',
    'vento direcao horaria (gr) (° (gr))',
    'vento rajada maxima (m/s)',
    'vento velocidade horaria (m/s)',
    'region',
    'state',
    'station',
    'station_code',
    'latitude',
    'longitude',
    'height']