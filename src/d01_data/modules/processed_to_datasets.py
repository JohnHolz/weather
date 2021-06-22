import pandas as pd

################################################
## processed to datasets tranformations
#################################################

def make_model_dataframe(df, dataset, datasets_info, fixed_columns = ['hour', 'month', 'weekday']):
    ## filtering the date
    df = df[df.index > datasets_info[dataset]['start_date']]
    ## declaring the output-dataframe
    df_out = pd.DataFrame()
    ## filtering regex
    for i in datasets_info[dataset]['regex_columns'] + fixed_columns:
        df_out = pd.concat([df_out,df.filter(regex=i)],axis=1)
    return df_out
