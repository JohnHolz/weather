
import pandas as pd
import requests as rq
from time import sleep
import json

def post_collect_station_data(station_code):
    path = 'http://192.168.0.14:5018/collect_station'
    json_data = {'station_code':station_code}
    req = rq.post(f'{path}', json=json_data)
    return req


def get_list_of_stations_to_collect(engine):
    sql_query = f'''
    select s.station_code 
    from stations s
    where s.collect=TRUE
    '''
    return list(pd.read_sql(sql_query,con=engine).station_code)

def get_stations_as_json_new_data(engine):
    sql_query = f'''
    SELECT c.station, MAX(c.data) as recent_date
    FROM collected c
    GROUP BY c.station
    ORDER BY recent_date DESC
    '''
    df = pd.read_sql(sql_query, con=engine)
    data_dict = df.to_dict('records')
    return data_dict

def collect_all_stations(engine):
    rets = {}
    ls_stations = get_list_of_stations_to_collect(engine)
    for i in ls_stations:
        rets[i] = post_collect_station_data(i)
        print(i)
        sleep(4)
    return rets

def station_status_code(input_dict):
    return {k:v.status_code for k,v in input_dict.items()}
