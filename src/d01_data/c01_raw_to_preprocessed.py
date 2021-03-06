
## * importing libs
import pandas as pd, numpy as np, os
from os.path import isfile, join

## * from m01 raw_to_preprocessed
from modules.raw_to_preprocessed import files_in_year
from modules.raw_to_preprocessed import read_inmet_csv

## * adding modules path
import sys
sys.path.insert(1, '../')

## * from m00 cleaning
from d00_modules.cleaning import transform_hr
from d00_modules.cleaning import comma_to_dot

def clean_raw_data():
    """
    ! get data
    ! run through folders to append data
    ! unite hour and date columns from diferent formats
    ! delete non informational data
    ! write preprocessed dataframe 
    """

    ## * change directory to historical data
    os.chdir('../../data/01_raw/inmet-hist')

    ## * declare the output dataframe
    final_data = pd.DataFrame()

    ## * go year folder by year folder concatenating the dataframes 
    for i in sorted(os.listdir('.')):
        year = i
        for j in files_in_year(year):
            final_data = final_data.append(read_inmet_csv(year + '/' + j))

    #  !  historical problemns
    ## ?  during the years the inmet changed the name of date and hour column 
    ## ?  so now when we append we have 2 date and 2 hours columnns, 
    ## ?  we need to remove the NAN data and append the columns to create a unique column

    ## ? creating date column
    date_1 = pd.to_datetime(final_data['DATA (YYYY-MM-DD)']).dropna()
    date_2 = pd.to_datetime(final_data['Data']).dropna()
    datas = date_1.append(date_2)
    final_data['Data'] = datas

    ## ? create hour column
    hour_1 = final_data['HORA (UTC)'].dropna()
    hour_2 = final_data['Hora UTC'].dropna().apply(transform_hr)
    final_data['Hora'] = hour_1.append(hour_2)
    final_data = final_data.drop(columns=['DATA (YYYY-MM-DD)','HORA (UTC)','Hora UTC'])

    ## ! remove the commas and transform all values in floats
    df_transformed = final_data.drop(columns=["region", "state", "station", "station_code", "Data", "Hora"]).applymap(comma_to_dot)
    df_transformed[["region", "state", "station", "station_code", "Data", "Hora"]] = final_data[["region", "state", "station", "station_code", "Data", "Hora"]]

    ## ! change directory to wright the final data
    os.chdir('../..')

    ## ! write the final data
    df_transformed.to_csv('02_preprocessed/preprocessed.csv',index=False)

    ## ! change directory back
    os.chdir('../src/d01_data')