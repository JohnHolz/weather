import pandas as pd

def transform_hr(string):
    """
    Hours came in 2 formats: "HH:MM" and "HHMM UTC" 
    so this function transform the second in the first
    """
    string = string.split(' ')[0]
    string = string[:2]+':'+string[2:]
    return string


def comma_to_dot(value):
    """
    brazil uses comma, so we need to transform comma to dots and retransform to float
    This function transforms a value in string, remove dots and then replace commas to dots
    """
    value = str(value).replace('.','').replace(',','.')
    return float(value)


def make_dummies(series):
    """
    
    """

    df = pd.get_dummies(series,drop_first=True)
    df.columns = list(map(lambda x: '{}_'.format(series.name) + str(x),list(df.columns)))
    return df