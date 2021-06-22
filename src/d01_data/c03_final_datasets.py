
## * importing libs
import pandas as pd, numpy as np
import json, os

## * adding modules path
import sys
sys.path.insert(1, '../')

## * from m00 processed_to_datasets
from d00_modules.m00_general.cleaning import make_dummies

## * from m01 processed_to_datasets
from d00_modules.m01_data.processed_to_datasets import make_model_dataframe

def make_datasets():
    """
    ! read processed data 
    ! create dummies
    ! filter some hours
    ! drop columns that created the dummies 
    ! read the dataset info
    ! write the datasets

    """


    df = pd.read_csv('../../data/03_processed/processed.csv')

    ## ? Na from dataset
    na_value = -9999

    ## ? organize index and drop hour and dates
    df['date_time'] = df['data']+' '+df['hora']
    df['date_time'] = pd.to_datetime(df['date_time'])

    ## ? adding week, month and year variables
    df['weekday'] = df['date_time'].dt.weekday
    df['month'] = df['date_time'].dt.month
    # df['year'] = df['date_time'].dt.year

    df = pd.concat((df,make_dummies(df['weekday'])),axis=1)
    df = pd.concat((df,make_dummies(df['month'])),axis=1)

    df = df.rename(columns={'hora': 'hour'})
    df.hour = df.hour.apply(lambda x: x.split(':')[0])
    
    ## ! selected_hours to make dataframe small
    selected_hours = ['00','03','06','09','12','15','18','21','24']
    
    df = df[df.hour.isin(selected_hours)]
    df = pd.concat((df,make_dummies(df['hour'])),axis=1)
    
    ## ? set an index
    df.index = df['date_time']
    df = df.drop(columns=['data','date_time','hour','weekday','month'])
    df = df.replace(to_replace=na_value,value=np.NaN)
    
    ## ! fill na with previous values
    df = df.fillna(method='ffill')
    
    ## ! variables to be used
    rows    = df.shape[0]
    columns = df.shape[1]
    
    datasets = 'datasets.json'
    with open(datasets) as data:
        datasets = json.load(data)
    
    dataset_keys = list(datasets.keys())
    
    for i in dataset_keys:
        make_model_dataframe(df,i,datasets_info = datasets).to_csv('../../data/04_datasets/{dataset}.csv'.format(dataset = i))