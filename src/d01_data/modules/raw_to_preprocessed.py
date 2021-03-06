import os
import pandas as pd
from os.path import isfile, join

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

