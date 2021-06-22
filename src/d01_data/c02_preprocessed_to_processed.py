
# * importing libs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

## * adding modules path
import sys
sys.path.insert(1, '../')

## * from m01 preprocessed_to_processed
from modules.preprocessed_to_processed import crossjoin, by_code

def process_data():
    """
    ! read preprocessed 
    ! create the final dataset -> crossjoin between hour and date
    ! combine hour and date columns -> transform to datetime this column
    ! rename the columns
    ! drop_duplicates just to be shure 
    ! append columns data from all stations to keep the data granularity
    ! remove not useful columns
    ! remove first lines with empty values
    ! write table 
    """

    ## ? get preprocessed data
    df = pd.read_csv('../../data/02_preprocessed/preprocessed.csv')

    ## ? creating the dataset with all combinations of dates and hours
    df_models = crossjoin(df['Data'],df['Hora'])
    df_models.columns = ['data','hora']

    ## ? change type to datetime
    df_models.iloc[:,0] = pd.to_datetime(df_models.iloc[:,0])

    # ? renamming columns to lowercase without special characters 
    df.columns = ['precipitacao total, horario (mm)',
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
    'latitude',
    'longitude',
    'height',
    'radiacao global (kj/m²)',
    'region',
    'state',
    'station',
    'station_code',
    'data',
    'hora']

    ## ! keep just date and hour to concatenate other informations
    df_models = df[['data', 'hora']]
    df_models = df_models.drop_duplicates()

    ## ! desnormalizing dataset by stations
    for i in df.station_code.unique():
        df_temp = by_code(df,i)
        df_models = df_models.merge(df_temp, 
                      how='left', 
                      right_on  = df_temp.iloc[:,-2:].columns.to_list(),
                      left_on = df.iloc[:,-2:].columns.to_list())

    ## ! remove not useful columns
    df_models = df_models[df_models.columns.drop(list(df_models.filter(regex='- data')))]
    df_models = df_models[df_models.columns.drop(list(df_models.filter(regex='- hora')))]
    df_models = df_models[df_models.columns.drop(list(df_models.filter(regex='- station_code')))]
    df_models = df_models[df_models.columns.drop(list(df_models.filter(regex='- station')))]
    df_models = df_models[df_models.columns.drop(list(df_models.filter(regex='- state')))]
    df_models = df_models[df_models.columns.drop(list(df_models.filter(regex='- region')))]
    df_models = df_models[df_models.columns.drop(list(df_models.filter(regex='- radiacao global')))]
    df_models = df_models[df_models.columns.drop(list(df_models.filter(regex='- latitude')))]
    df_models = df_models[df_models.columns.drop(list(df_models.filter(regex='- longitude')))]
    df_models = df_models[df_models.columns.drop(list(df_models.filter(regex='- height')))]

    ## ! removing first lines with empty values 
    df_models = df_models.iloc[16:,:]

    ## ! write to csv
    df_models.to_csv('../../data/03_processed/processed.csv',encoding='utf-8',index=False)