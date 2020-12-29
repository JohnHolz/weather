import pandas as pd, numpy as np, os
from os.path import isfile, join
from transform_data_raw import files_in_year, read_inmet_csv, transform_hr

os.chdir('../data/raw/inmet-hist')
os.getcwd()

final_data = pd.DataFrame()
for i in sorted(os.listdir('.')):
    year = i
    for j in files_in_year(year):
        final_data = final_data.append(read_inmet_csv(year + '/' + j))

x1 = pd.to_datetime(final_data['DATA (YYYY-MM-DD)']).dropna()
x2 = pd.to_datetime(final_data['Data']).dropna()
datas = x1.append(x2)
final_data['Data'] = datas

x1 = final_data['HORA (UTC)'].dropna()
x2 = final_data['Hora UTC'].dropna().apply(transform_hr)
final_data['Hora'] = x1.append(x2)
final_data = final_data.drop(columns=['HORA (UTC)','Hora UTC'])

os.chdir('../..')
final_data.to_csv('preprocessed.csv',index=False)