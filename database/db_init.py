import dask.dataframe as dd
## importing my lib functions to work with databases with fewer lines 
from jh_utils.data.sql.connection import create_string_connection, create_connection
from jh_utils.data.sql.object import create_object_DB_by_envfile
from jh_utils.utils.mensages import attention
from jh_utils.data.sql.manipulate_db import create_table_structure, create_schema, delete_table
import pandas as pd
import sqlalchemy as sa
## importing env variables
from dotenv import dotenv_values
env = dotenv_values('../../.env')

db_object = create_object_DB_by_envfile('../../.env')

engine = db_object.engine()
engine_string = db_object.uri()
# engine_string = create_string_connection(database=env['db'],host='localhost',password=env['pass'],user=env['user'],port=env['port'])

regions = ['northeast','southeast','south','central_west','north']

## Creating schemas
def create_schemas(db_object):
    db_object.create_schema('raw')
    db_object.create_schema('datasets')
    db_object.create_schema('metadata')
    db_object.create_schema('models')

def create_structure():
    for i in regions:
        pandas_df = pd.read_csv(f'02_preprocessed/{i}/2020.csv')
        create_table_structure(pandas_df,i,engine,schema='raw')

from jh_utils.utils.timer import Timer
def upload_historical_data(region):
    for i in range(2000,2022):
        time = Timer(True)
        df = dd.read_csv(f'02_preprocessed/{region}/{i}.csv')
        dd.to_sql(df,uri=engine_string, name=region,schema='raw',parallel=True, method='multi',chunksize=15_000,if_exists='append',index=False)
        time.stop()
        print(i,'-',time.duration)

if __name__ == '__main__':
    create_schemas()
    print('SCHEMAS CREATED')
    create_structure()
    print('RAW HISTORICAL TABLE CREATED')
    upload_historical_data(region='southeast')
    print(attention('southeast'))
    upload_historical_data(region='south')
    print(attention('south'))
    # upload_historical_data(region='central_west')
    # print(attention('central_west'))
    # upload_historical_data(region='north')
    # print(attention('north'))
    # upload_historical_data(region='northeast')
    # print(attention('northeast'))
    print('RAW HISTORICAL UPLOADED')
