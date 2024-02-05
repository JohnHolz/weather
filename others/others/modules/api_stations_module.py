from jh_utils.data.sql.object import create_object_DB_by_envfile
import pandas as pd
from jh_utils.data.pandas.sql import write_sql_table, get_sql_table


def base_station_table(path='../../../api/lab/stations.csv'):
    df = pd.read_csv(path)
    df.rename(columns={'first date':'first'}, inplace=True)
    df = df.drop_duplicates('station_code')
    df['collect'] = False
    return df

def write_stations_table(engine):
    df = base_station_table()
    ## setting one state to collect
    df.loc[df['state'] == 'ES','collect'] = True
    write_sql_table(df,
                table_name='stations',
                schema='public',
                engine=engine, 
                if_exists='replace') ## reset replacing
    return 'ok'

def update_state_to_collect(state, engine):
    df = pd.read_sql_table('stations',schema='public',con=engine)
    df.loc[df['state'] == state,'collect'] = True
    write_sql_table(df,
                table_name='stations',
                schema='public',
                engine=engine, 
                if_exists='replace') ## reset replacing
    return 'updated to: True'
    
def update_state_to_not_collect(state, engine):
    df = pd.read_sql_table('stations',schema='public',con=engine)
    df.loc[df['state'] == state,'collect'] = False
    write_sql_table(df,
                table_name='stations',
                schema='public',
                engine=engine, 
                if_exists='replace') ## reset replacing
    return 'updated to: False'

def get_list_of_stations_to_collect(engine):
    sql_query = f'''
    select s.station_code 
    from public.stations s
    where s.collect=TRUE
    '''
    return list(pd.read_sql(sql_query,con=engine).station_code)