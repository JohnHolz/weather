from jh_utils.sql.connection import create_connection 
from dotenv import dotenv_values

def create_stations_table(engine):
    sql_file = open('sql/stations_metadata.sql','r')
    query = sql_file.read()
    engine.execute(query)

#############################################
from jh_utils.pandas.sql import write_table
import pandas as pd

def create_datasets_table(engine):
    datasets = [{
        "name": "ES_0",
        "stations":["A612"],
        "start_date":"2006-10-31"
    },{
        "name": "ES_1",
        "stations":["A612","A634","A613","A614"],
        "start_date":"2017-02-15"
    }]

    datasets_metadata_table = pd.DataFrame(datasets)
    write_table(datasets_metadata_table,'datasets',schema='metadata',engine=engine,if_exists='replace')

if __name__=='__main__':
    env = dotenv_values('../../.env')
    engine = create_connection(database=env['db'],user=env['user'],password=env['pass'],host='localhost',port=env['port'])
    create_stations_table(engine)
    create_datasets_table(engine)