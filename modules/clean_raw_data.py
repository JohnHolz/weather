import os 
from os.path import isfile, join

def es_data(ano,get_in_hist_folder = 'inmet-hist', file_name_contains = 'INMET_SE_ES_'):
    folder = './{folder_1}/{folder_2}'.format(folder_1 = get_in_hist_folder,folder_2 = ano)
    return list(filter(lambda k: str(file_name_contains) in k, os.listdir(folder)))

