import pandas as pd

################################################
## processed to datasets tranformations
#################################################

def make_model_dataframe(df, dataset, fixed_columns = ['hour', 'month', 'weekday', 'sin', 'cos']):
    ## filtering the date
    df = df[df.index > dataset['start_date']]
    ## declaring the output-dataframe
    df_out = pd.DataFrame()
    ## filtering regex
    for i in dataset['regex_columns'] + fixed_columns:
        df_out = pd.concat([df_out,df.filter(regex=i)],axis=1)
    return df_out