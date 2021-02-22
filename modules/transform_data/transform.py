import os 
from os.path import isfile, join
import pandas as pd, numpy as np

###################################
## raw to preprocessed
###################################

def files_in_year(year, contains = 'INMET_SE_ES_'):
    folder = './{folder}'.format(folder = year)
    return list(filter(lambda k: str(contains) in k, os.listdir(folder)))

def read_inmet_csv(file):
    """
    In inmet csv data we have the data and the metadata (first 8 lines of csv). 
    The data is date, temp, wind...
    The metadata is city of station, latitude, height...
    Só in this func we want to read the file and transform 
    the metadata in columns to be used
    """

    ## read data
    dados = pd.read_csv(file, encoding='ISO-8859-1', sep=';', skiprows=8).iloc[:,:-1]

    ## read metadata
    about = pd.read_csv(file, encoding='ISO-8859-1', sep=';', nrows=8, header=None)
    
    ## transforming metadata in columns
    about = about.transpose()
    about.columns = about.iloc[0,:]
    about = about.iloc[1]
    dados['region']        = about[0]
    dados['state']         = about[1]
    dados['station']       = about[2]
    dados['station_code']  = about[3]
    dados['latitude']      = about[4]
    dados['longitude']     = about[5]
    dados['height']        = about[6]

    # return data
    return dados

def transform_hr(string):
    """
    Hours came in 2 formats: "HH:MM" and "HHMM UTC" 
    so this function transform the second in the first
    """
    string = string.split(' ')[0]
    string = string[:2]+':'+string[2:]
    return string


def comma_to_dot(value):
    """
    brazil uses comma, so we need to transform comma to dots and retransform to float
    This function transforms a value in string, remove dots and then replace commas to dots
    """
    value = str(value).replace('.','').replace(',','.')
    return float(value)



################################################
## preprocessed to processed tranformations
#################################################

def crossjoin(column_1,column_2):
    """
    Create a crossjoin dataframe based on 2 columns
    """
    column_1 = pd.DataFrame(column_1.unique())
    column_2 = pd.DataFrame(column_2.unique())
    column_1['key'], column_2['key'] = 0,0
    return column_1.merge(column_2,on='key').drop(columns = 'key')

def by_code(df,station_code):
    """
    Create a dataframe filtered by station_code and rename the columns by the status code
    """
    df_station = df[df['station_code'] == station_code]
    df_station.columns = list(map(lambda x: station_code+' - '+x,df_station.columns))
    return df_station


