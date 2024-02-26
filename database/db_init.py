import dask.dataframe as dd
## importing my lib functions to work with databases with fewer lines 
from jh_utils.data.sql.connection import create_string_connection, create_connection
from jh_utils.data.sql.object import create_object_DB_by_envfile
from jh_utils.utils.mensages import attention
from jh_utils.data.sql.manipulate_db import create_table_structure, create_schema, delete_table
import pandas as pd
import sqlalchemy as sa
from dotenv import dotenv_values
from sqlalchemy import create_engine, text
from time import sleep

db_object = create_object_DB_by_envfile('.env')
engine = db_object.engine()
engine_string = db_object.uri()
# engine_string = create_string_connection(database=env['db'],host='localhost',password=env['pass'],user=env['user'],port=env['port'])
regions = ['northeast','southeast','south','central_west','north']

def create_schema(schema_name, engine):
    ## remake,sqlalchemy broke
    with engine.connect() as conn:
        conn.execute(f'CREATE SCHEMA IF NOT EXISTS {schema_name};')


def create_schemas():
    create_schema('raw',engine)
    create_schema('datasets',engine)
    create_schema('metadata',engine)
    create_schema('models',engine)

def create_structure():
    pandas_df = pd.read_csv(f'data/02_preprocessed/southeast/2020.csv',nrows=100)
    for i in regions:
        create_table_structure(pandas_df,i,engine,schema='raw')

from jh_utils.utils.timer import Timer
def upload_historical_data(region):
    for i in range(2022,2024):
        time = Timer(True)
        df = dd.read_csv(f'data/02_preprocessed/{region}/{i}.csv')
        dd.to_sql(df,uri=engine_string, name=region, schema='raw',parallel=True, method='multi',chunksize=15_000,if_exists='append',index=False)
        time.stop()
        print(i,'-',time.duration, '- sleeping 10s')
        sleep(10)
        
if __name__ == '__main__':
    create_schemas()
    print('SCHEMAS CREATED')
    create_structure()
    print('RAW HISTORICAL TABLE CREATED')
    upload_historical_data(region='southeast')
    print(attention('southeast'))
    # upload_historical_data(region='south')
    # print(attention('south'))
    # upload_historical_data(region='central_west')
    # print(attention('central_west'))
    # upload_historical_data(region='north')
    # print(attention('north'))
    # upload_historical_data(region='northeast')
    # print(attention('northeast'))
    # print('RAW HISTORICAL UPLOADED')
