import os
import pandas as pd
from os.path import isfile, join

###################################
## raw to preprocessed
###################################

def files_in_year(year, contains = 'INMET_SE'):
    folder = './{folder}'.format(folder = year)
    return list(filter(lambda k: str(contains) in k, os.listdir(folder)))

def transform_hr(string:str):
    """
    Hours came in 2 formats: "HH:MM" and "HHMM UTC" 
    so this function transform the second in the first
    """
    string = string.split(' ')[0]
    string = string[:2]+':'+string[2:]
    return string

def comma_to_dot(value:str):
    """
    brazil uses comma, so we need to transform comma to dots and retransform to float
    This function transforms a value in string, remove dots and then replace commas to dots
    """
    value = str(value).replace('.','').replace(',','.')
    try:
        return float(value)
    except:
        return -9999

def change_comma(string):
    string = string.replace(',','.')
    if string.split('.')[0] == '':
        string = '0'+string
    return string

def read_inmet_csv(file):
    """
    In inmet csv data we have the data and the metadata (first 8 lines of csv). 
    The data is date, temp, wind...
    The metadata is city of station, latitude, height...
    Só in this func we want to read the file and transform 
    the metadata in columns to be used
    """

    ## read data
    data = pd.read_csv(file, encoding='ISO-8859-1', sep=';', skiprows=8, decimal=',').iloc[:,:-1]

    ## read metadata
    about = pd.read_csv(file, encoding='ISO-8859-1', sep=';', nrows=8, header=None, decimal=',')
    
    ## transforming metadata in columns
    about = about.transpose()
    about.columns = about.iloc[0,:]
    about = about.iloc[1]
    data['region']        = about[0]
    data['state']         = about[1]
    data['station']       = about[2]
    data['station_code']  = about[3]
    data['latitude']      = about[4]
    data['longitude']     = about[5]
    data['height']        = about[6]

    if 'DATA (YYYY-MM-DD)' in data.columns:
        data.rename(columns={'DATA (YYYY-MM-DD)': 'Data'}, inplace=True)
    
    data['Data'] = pd.to_datetime(data['Data'])

    if 'HORA (UTC)' in data.columns:
        data.rename(columns={'HORA (UTC)': 'Hora'}, inplace=True)

    if 'Hora UTC' in data.columns:
        data['Hora UTC'] = data['Hora UTC'].apply(transform_hr)
        data.rename(columns={'Hora UTC': 'Hora'}, inplace=True)

    # return data
    return data