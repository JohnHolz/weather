import pandas as pd
from sklearn.model_selection import cross_validate, train_test_split
from jh_utils.data.sql.object import create_object_DB_by_envfile
from statsmodels.regression.linear_model import OLS
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from sklearn.model_selection import train_test_split


def ols_model(x, y, codename=None):
    if codename == None:
        codename = f'{x.shape[1]}_{y.name.split("_")[1]}'
        
    x_train, x_test = x[df_model.date_time<'01-01-2018'], x[df_model.date_time>='01-01-2018']
    y_train, y_test = y[df_model.date_time<'01-01-2018'], y[df_model.date_time>='01-01-2018']
    
    model = OLS(y_train,x_train)
    fit = model.fit()
    y_pred = fit.predict(x_test)
    
    metrics = evaluate(y_test,y_pred)
    return {'y_pred': y_pred, 'fit': fit, 'model':model, 'metrics':metrics, 'codename': codename}


db = create_object_DB_by_envfile('.env')

query = 'select * from datasets."ES_0"'


df = pd.read_sql(query,con=db.engine)

## adding covariables
df.date_time = pd.to_datetime(df.date_time)
df['hour'] = df.date_time.dt.hour
df['month'] = df.date_time.dt.month
df['year'] = df.date_time.dt.year
df['day_of_year'] = df.date_time.dt.day_of_year
df['weekofyear'] = df.date_time.dt.weekofyear

## transforming start hour in 9, to use hour**3, some models are hierarchical so is necessary to keep hour**2 
df['hour_9'] = df['hour'].apply(lambda x: (x-9)%24)
df['hour_9**2'] = df['hour_9']**2
df['hour_9**3'] = df['hour_9']**3

df_model = df[['month','hour_9','hour_9**2','hour_9**3']]

break_date = '2020-01-01'
train = df_model[df_model.datetime < break_date]
test = df_model[df_model.datetime > break_date]

model = ols_model(x,_y_.iloc[:,1])
from .evaluate import evaluate
