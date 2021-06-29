
## * importing libs
import pandas as pd, numpy as np
import json, os

## * adding modules path
import sys
sys.path.insert(1, '../')

## * from m00 processed_to_datasets
from d00_modules.cleaning import make_dummies

## * from m01 processed_to_datasets
from modules.processed_to_datasets import make_model_dataframe

## frin jh_utils
from jh_utils.time_series.time_dataframe import time_series_dataframe

def make_datasets():
    """
    ! read processed data 
    ! create dummies
    ! filter some hours
    ! drop columns that created the dummies 
    ! read the dataset info
    ! write the datasets

    """
    ## read dataset
    df = pd.read_csv('../../data/03_processed/processed.csv')

    ## Na from dataset
    na_value = -9999

    ## organize index and drop hour and dates
    df['date_time'] = df['data']+' '+df['hora']
    df['date_time'] = pd.to_datetime(df['date_time'])
    df = df.rename(columns={'hora': 'hour'})
    df.hour = df.hour.apply(lambda x: x.split(':')[0])
    ## set an index
    df.index = df['date_time']
    df = df.drop(columns=['data','date_time','hour'])
    df = df.replace(to_replace=na_value,value=np.NaN)

    ## fill na with previous values
    df = df.fillna(method='ffill')
    df = df.reset_index()
    df = df[df.date_time>'2006-11-01']
    df.reset_index(drop=True, inplace=True)
    df.index = df.date_time

    ## ! concatenate 
    time_df = time_series_dataframe('2006-11-01','2021-01-01').iloc[1:]
    df = pd.concat([df,time_df],axis=1).iloc[:,1:]

    datasets = 'datasets.json'
    with open(datasets) as data:
        datasets = json.load(data)

    dataset_keys = list(datasets.keys()) 

    for i in dataset_keys:
        make_model_dataframe(df,datasets[i]).to_csv('../../data/04_datasets/{dataset}.csv'.format(dataset = i),index = False)