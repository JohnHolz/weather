import os 
from os.path import isfile, join
import pandas as pd

def files_in_year(year, contains = 'INMET_SE_ES_'):
    folder = './{folder}'.format(folder = year)
    return list(filter(lambda k: str(contains) in k, os.listdir(folder)))

def read_inmet_csv(file):
    ## read data
    dados = pd.read_csv(file, encoding='ISO-8859-1', sep=';', skiprows=8).iloc[:,:-1]
    ## about the data
    about = pd.read_csv(file, encoding='ISO-8859-1', sep=';', nrows=8, header=None)
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
    return dados

def transform_hr(string):
    string = string.split(' ')[0]
    string = string[:2]+':'+string[2:]
    return string