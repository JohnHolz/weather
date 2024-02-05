
from jh_utils.data.pandas.sql import write_sql_table, get_sql_table
from jh_utils.data.sql.object import create_object_DB_by_envfile
import pandas as pd


def base_station_table(path='lab/stations.csv'):
    df = pd.read_csv(path)
    df.rename(columns={'first date':'first'}, inplace=True)
    df = df.drop_duplicates('station_code')
    df['collect'] = False
    return df

def write_stations_table(engine):
    df = base_station_table()
    df.loc[df['state'] == 'ES','collect'] = True
    ## setting one state to collect
    write_sql_table(df,
                table_name='stations',
                schema='public',
                engine=engine, 
                if_exists='replace') ## reset replacing
    return 'ok'

def update_state_to_collect(state):
    ob = create_object_DB_by_envfile('.env')
    engine = ob.engine()
    df = pd.read_sql_table('stations',con=engine)
    df.loc[df['state'] == state,'collect'] = True
    write_sql_table(df,
                table_name='stations',
                schema='public',
                engine=engine, 
                if_exists='replace') ## reset replacing
    return 'updated to: True'

def update_state_to_not_collect(state):
    ob = create_object_DB_by_envfile('.env')
    engine = ob.engine()
    df = pd.read_sql_table('stations',con=engine)
    df.loc[df['state'] == state,'collect'] = False
    write_sql_table(df,
                table_name='stations',
                schema='public',
                engine=engine, 
                if_exists='replace') ## reset replacing
    return 'updated to: False'


def get_last_hours_query(station, hours=16):
    return f'''SELECT c.station,
       c."data",
       c.hora,
       c."temperatura maxima na hora ant. (aut) (°c)",
       c."temperatura minima na hora ant. (aut) (°c)"
    FROM public.collected c
    WHERE c.station = {station} AND TO_TIMESTAMP(c."data" || ' ' || c.hora, 'DD/MM/YYYY HH24:MI') >= (CURRENT_TIMESTAMP - INTERVAL '{hours} hours')'''

def get_temperature_message(station):
    ob = create_object_DB_by_envfile('.env')
    engine = ob.engine()
    df = pd.read_sql(get_last_hours_query(station,16),con=engine)
    return df.to_string()
