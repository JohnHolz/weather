import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import modules.transform_data_processed as td

def process_data():
    df = pd.read_csv('data/preprocessed.csv')
    df_models = td.crossjoin(df['Data'],df['Hora'])
    df_models.columns = ['data','hora']
    df_models.iloc[:,0] = pd.to_datetime(df_models.iloc[:,0])

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

    df_models = df[['data', 'hora']]
    df_models = df_models.drop_duplicates()

    for i in df.station_code.unique():
        df_temp = td.by_code(df,i)
        df_models = df_models.merge(df_temp, 
                      how='left', 
                      right_on  = df_temp.iloc[:,-2:].columns.to_list(),
                      left_on = df.iloc[:,-2:].columns.to_list())

    df_models.to_csv('data/processed.csv',encoding='utf-8',index=False)