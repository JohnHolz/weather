
from flask import request, Blueprint, make_response, jsonify
from sqlalchemy import func
import pandas as pd
from selenium import webdriver
from jh_utils.data.pandas.sql import write_sql_table, get_sql_table
import time
# from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.chromium.options import Options
from jh_utils.data.sql.object import create_object_DB_by_envfile
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.core.os_manager import ChromeType


def get_station_data2(station:str):
    site = f'https://tempo.inmet.gov.br/TabelaEstacoes/{station}'
    chrome_driver_path = '/usr/lib/chromium-browser/chromedriver'

    # webdriver_manager = ChromeDriverManager()
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    # wb = webdriver.Chrome(webdriver_manager, options)

    service = webdriver.FirefoxService(executable_path='/usr/local/bin/geckodriver')
    wb = webdriver.Firefox(service=service)

    # wb = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    wb.get(site)
    time.sleep(5)
    df = pd.read_html(wb.page_source, decimal=',', thousands='.')[0]
    wb.close()
    return clean_data(df,station)


def write_station_data(station:str, engine):
    df = get_station_data2(station)
    write_sql_table(df,table_name='collected',schema='public',engine=engine, if_exists='append')



##### # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # 

columns_names = ['data',
        'hora',
        # temperatura
        'temperatura do ar - bulbo seco, horaria (°c)',
        'temperatura maxima na hora ant. (aut) (°c)',
        'temperatura minima na hora ant. (aut) (°c)',
        # umidade
        'umidade relativa do ar, horaria (%)',
        'umidade rel. max. na hora ant. (aut) (%)',
        'umidade rel. min. na hora ant. (aut) (%)',
        # orvalho
        'temperatura do ponto de orvalho (°c)',
        'temperatura orvalho max. na hora ant. (aut) (°c)',
        'temperatura orvalho min. na hora ant. (aut) (°c)',
        # pressao 
        'pressao atmosferica ao nivel da estacao, horaria (mb)',
        'pressao atmosferica max. na hora ant. (aut) (mb)',
        'pressao atmosferica min. na hora ant. (aut) (mb)',
        # VENTO
        'vento direcao horaria (gr) (° (gr))',
        'vento rajada maxima (m/s)',
        'vento velocidade horaria (m/s)',
        ## radiaçao, chuva e station
        'radiacao global (kj/m2)',
        'precipitacao total, horario (mm)',
        'station']

def transform_hr(hour):
    value = hour/100
    if value<10:
        return f'0{int(value)}:00'
    else:
        return f'{int(value)}:00'

def clean_data(df, station:str):
    df['station'] = station
    df.columns = columns_names
    df['hora'] = df['hora'].apply(transform_hr)
    df.dropna(axis=0,thresh=10, inplace=True)
    return df


def get_station_data(station:str):
    site = f'https://tempo.inmet.gov.br/TabelaEstacoes/{station}'
    chrome_driver_path = '/usr/lib/chromium-browser/chromedriver'

    webdriver_manager = GeckoDriverManager()
    options = webdriver.Fire()

    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    # wb = webdriver.Chrome(webdriver_manager, options)
    wb = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install())

    # wb = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    wb.get(site)
    time.sleep(5)
    df = pd.read_html(wb.page_source, decimal=',', thousands='.')[0]
    return clean_data(df,station)

#### rota

collector_blueprint = Blueprint('collector_blueprint', __name__, template_folder='model')

@collector_blueprint.route('/collect_station', methods =['POST'])
def try_collect_station():
    try:
        data = request.get_json()
        db_object = create_object_DB_by_envfile()
        write_station_data(data['station_code'], engine=db_object.engine())
        return make_response(jsonify({"message": "Success"}), 200)
    except Exception as e:
        return make_response(jsonify({"message": "Error"}), 500)
