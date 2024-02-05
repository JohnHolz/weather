from dotenv import dotenv_values
#from jh_utils.data.sql.utils import create_string_connection
from jh_utils.data.sql.connection import create_string_connection
from jh_utils.data.sql.object import create_object_DB_by_envfile

def get_connection_string():
    obj = create_object_DB_by_envfile()
    return obj.uri()

def get_secret_key():
    config = dotenv_values(".env")
    secret_key = config['secret_key']
    return secret_key
