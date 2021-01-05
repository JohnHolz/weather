import pandas as pd, numpy as np, os
from os.path import isfile, join
from transform_data_raw import files_in_year, read_inmet_csv, transform_hr

## change directory to historical data
os.chdir('../data/raw/inmet-hist')

## declare the output dataframe
final_data = pd.DataFrame()

## go year folder by year folder concatenating the dataframes 
for i in sorted(os.listdir('.')):
    year = i
    for j in files_in_year(year):
        final_data = final_data.append(read_inmet_csv(year + '/' + j))


# historical problemns
## during the years the inmet changed the name of date and hour column 
## so now when we append we have 2 date and 2 hours columnns, 
## we need to remove the NAN data and append the columns to create a unique column

## creating date column
date_1 = pd.to_datetime(final_data['DATA (YYYY-MM-DD)']).dropna()
date_2 = pd.to_datetime(final_data['Data']).dropna()
datas = date_1.append(date_2)
final_data['Data'] = datas

## create hour column
hour_1 = final_data['HORA (UTC)'].dropna()
hour_2 = final_data['Hora UTC'].dropna().apply(transform_hr)
final_data['Hora'] = hour_1.append(hour_2)
final_data = final_data.drop(columns=['DATA (YYYY-MM-DD)','HORA (UTC)','Hora UTC'])

## change directory to wright the final data
os.chdir('../..')

## write the final data
final_data.to_csv('preprocessed.csv',index=False)