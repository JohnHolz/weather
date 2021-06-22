import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

def get_today_data(station = 'A612'):
    
    # ! getting station`s new data from today 
    # ? link https://tempo.inmet.gov.br/TabelaEstacoes/{station}
    # * 
    
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    site = f'https://tempo.inmet.gov.br/TabelaEstacoes/{station}'

    wb = webdriver.Chrome('chromedriver',options = options)
    wb.get(site)

    html = wb.page_source
    df = pd.read_html(html)[0]
    return df