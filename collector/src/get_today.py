import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

def get_current_data(station_code = 'A612'):
    sleep_time = 4
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    site = 'https://tempo.inmet.gov.br/TabelaEstacoes/'+station_code
    wb = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    sleep(sleep_time)
    wb.get(site)
    sleep(sleep_time)
    html = wb.page_source
    df = pd.read_html(html)[0]
    return df