import numpy as np
import pandas as pd

# split a univariate sequence into samples
def split_sequence(sequence, n_steps_in, n_steps_out):
    X, y = list(), list()
    for i in range(len(sequence)):
        # find the end of this pattern
        end_ix = i + n_steps_in
        out_end_ix = end_ix + n_steps_out
        # check if we are beyond the sequence
        if out_end_ix > len(sequence):
            break
        # gather input and output parts of the pattern
        seq_x, seq_y = sequence[i:end_ix], sequence[end_ix:out_end_ix]
        X.append(seq_x)
        y.append(seq_y)
    return np.array(X), np.array(y)


#from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.layers import LSTM, Dropout, Dense
from tensorflow.keras.models import Sequential

def lstm_model(first_layer = 16,
            hidden_layers = [32], 
            n_features = 1, 
            n_steps_in = 12, 
            n_steps_out = 12,
            optimizer = 'RMsprop', 
            loss = 'mse'):
    # reshape from [samples, timesteps] into [samples, timesteps, features]
    # define model
    model = Sequential()
    model.add(LSTM(first_layer, 
                    activation='relu', 
                    return_sequences=True, 
                    input_shape=(n_steps_in, n_features)))
    model.add(Dropout(0.35))
    for i in hidden_layers:
        model.add(LSTM(i, activation='relu'))
        model.add(Dropout(0.35))
    model.add(Dense(n_steps_out))
    model.compile(optimizer=optimizer, loss=loss)
    return model


def transform_data(raw_data, data_agregation, first_date):
    df = raw_data.groupby('sk_data').sum()
    df.index = pd.to_datetime(df.index,format = '%Y%m%d')
    df = df.resample(data_agregation).sum()
    df = df[df.index>first_date]
    df = df.total.values
    df = df.astype('float32')
    return df