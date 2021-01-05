import pandas as pd, numpy as np

def crossjoin(column_1,column_2):
    column_1 = pd.DataFrame(column_1.unique())
    column_2 = pd.DataFrame(column_2.unique())
    column_1['key'], column_2['key'] = 0,0
    return column_1.merge(column_2,on='key').drop(columns = 'key')