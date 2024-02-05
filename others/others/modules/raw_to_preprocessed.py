import pandas as pd, numpy as np, os
from os.path import isfile, join
from jh_utils.utils.mensages import attention

## * adding modules path
## importing my modules
from modules.raw_to_preprocessed import files_in_year, read_inmet_csv, transform_hr, comma_to_dot, change_comma

## importing my lib functions to work with databases with fewer lines 
from jh_utils.data.sql.connection import create_string_connection
from jh_utils.pandas.sql import write_table

## importing env variables
from dotenv import dotenv_values
env = dotenv_values('../../.env')

def fill_region_raw(contains = 'INMET_',region='southeast'):
    """
    ! get data
    ! run through folders to append data
    ! unite hour and date columns from diferent formats
    ! delete non informational data
    ! write preprocessed dataframe 
    """

    data_folder = '../../data/01_raw/inmet-hist/'
    # engine = create_string_connection(database=env['db'], user=env['user'],password=env['pass'], host=env['host'],port=env['port'])
    for i in sorted(os.listdir(data_folder)):
        df = pd.DataFrame()
        for j in files_in_year(data_folder+i, contains = contains):
            df = df.append(read_inmet_csv(data_folder + i + '/' + j))
            print(j)
        
        if 'RADIACAO GLOBAL (KJ/m²)' in df.columns:
            df.rename(columns={'RADIACAO GLOBAL (KJ/m²)': 'RADIACAO GLOBAL (Kj/m²)'},inplace=True)
        df['latitude'], df['longitude'], df['height'] = pd.to_numeric(df.latitude.apply(comma_to_dot)), pd.to_numeric(df.longitude.apply(comma_to_dot)), pd.to_numeric(df.height.apply(comma_to_dot))
        df.fillna(-9999,inplace=True)
        df.to_csv(f'../../data/02_preprocessed/{region}/{i}.csv',index=False)
        print(i)

if __name__ == "__main__":
    print(attention('HERE'))
    fill_region_raw(contains = 'INMET_N_', region='north')
    print(attention('north'))
    fill_region_raw(contains = 'INMET_CO', region='central_west')
    print(attention('central_west'))
    fill_region_raw(contains = 'INMET_S_', region='south')
    print(attention('south'))
    fill_region_raw(contains = 'INMET_NE', region='northeast')
    print(attention('northeast'))
    fill_region_raw(contains = 'INMET_SE', region='southeast')
    print(attention('southeast'))
