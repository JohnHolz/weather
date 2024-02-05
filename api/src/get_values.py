import pandas as pd
def raw_temperature_data(station,engine):
    sql_query = f'''
        SELECT station,"data",hora,"temperatura maxima na hora ant. (aut) (°c)","temperatura minima na hora ant. (aut) (°c)"
        FROM collected
        WHERE station = '{station}' AND TO_TIMESTAMP("data" || ' ' || hora, 'DD/MM/YYYY HH24:MI') >= (CURRENT_TIMESTAMP - INTERVAL '96 hours')
    '''
    df = pd.read_sql(sql_query,con=engine)
    df = df.loc[:,['data',
        'hora',
        'temperatura maxima na hora ant. (aut) (°c)',
        'temperatura minima na hora ant. (aut) (°c)']]
    df.columns = ['data',
        'hora',
        'temp_max',
        'temp_min']
    return df.to_dict(orient='records')
