import json
import tensorflow as tf
import requests
from keras.models import Sequential
from keras.layers import Activation, Dense, Dropout, LSTM
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.metrics import mean_absolute_error
from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler
plt.switch_backend('Agg')
plt.style.use("ggplot")

from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout

def tanner_btc():
    endpoint = 'https://min-api.cryptocompare.com/data/histoday'
    res = requests.get(endpoint + '?fsym=BTC&tsym=USD&limit=2000')
    df = pd.DataFrame(json.loads(res.content)['Data'])
    df.drop(['conversionType'], 1, inplace=True)
    df.drop(['conversionSymbol'], 1, inplace=True)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df = df.set_index("time")[['close']].tail(1000)
    df = df.set_index(pd.to_datetime(df.index))

    scaler = MinMaxScaler()
    df = pd.DataFrame(scaler.fit_transform(df), columns=df.columns, index=df.index)


    def split_sequence(seq, n_steps_in, n_steps_out):
        """
        Splits the univariate time sequence
        """
        X, y = [], []

        for i in range(len(seq)):
            end = i + n_steps_in
            out_end = end + n_steps_out

            if out_end > len(seq):
                break

            seq_x, seq_y = seq[i:end], seq[end:out_end]

            X.append(seq_x)
            y.append(seq_y)

        return np.array(X), np.array(y)
    # How many periods looking back to train
    n_per_in  = 30

    # How many periods ahead to predict
    n_per_out = 10

    # Features (in this case it's 1 because there is only one feature: price)
    n_features = 1

    # Splitting the data into appropriate sequences
    X, y = split_sequence(list(df.close), n_per_in, n_per_out)

    # Reshaping the X variable from 2D to 3D
    X = X.reshape((X.shape[0], X.shape[1], n_features))

    #calling the pre-trained model
    model = keras.models.load_model('static/models/btc_model.h5')

    # Predicting off of y because it contains the most recent dates
    yhat = model.predict(np.array(df.tail(n_per_in)).reshape(1, n_per_in, n_features)).tolist()[0]

    # Transforming the predicted values back to their original prices
    yhat = scaler.inverse_transform(np.array(yhat).reshape(-1,1)).tolist()

    # Creating a DF of the predicted prices
    preds = pd.DataFrame(yhat, index=pd.date_range(start=df.index[-1], periods=len(yhat), freq="D"), columns=df.columns)

    # Printing the predicted prices
    print(preds)

    # Number of periods back to visualize the actual values
    pers = 10

    # Transforming the actual values to their original price
    actual = pd.DataFrame(scaler.inverse_transform(df[["close"]].tail(pers)), index=df.close.tail(pers).index, columns=df.columns).append(preds.head(1))

    # Plotting
    plt.figure(figsize=(16,6))
    plt.plot(actual, label="Actual Prices")
    plt.plot(preds, label="Predicted Prices")
    plt.ylabel("Price")
    plt.xlabel("Dates")
    plt.title(f"Forecasting the next {len(yhat)} days")
    plt.legend()
    plt.savefig("static/images/btc_predictions.png")

    return preds


def tanner_doge():
    endpoint = 'https://min-api.cryptocompare.com/data/histoday'
    res = requests.get(endpoint + '?fsym=DOGE&tsym=USD&limit=2000')
    df = pd.DataFrame(json.loads(res.content)['Data'])
    df.drop(['conversionType'], 1, inplace=True)
    df.drop(['conversionSymbol'], 1, inplace=True)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df = df.set_index("time")[['close']].tail(1000)
    df = df.set_index(pd.to_datetime(df.index))

    scaler = MinMaxScaler()
    df = pd.DataFrame(scaler.fit_transform(df), columns=df.columns, index=df.index)


    def split_sequence(seq, n_steps_in, n_steps_out):
        """
        Splits the univariate time sequence
        """
        X, y = [], []

        for i in range(len(seq)):
            end = i + n_steps_in
            out_end = end + n_steps_out

            if out_end > len(seq):
                break

            seq_x, seq_y = seq[i:end], seq[end:out_end]

            X.append(seq_x)
            y.append(seq_y)

        return np.array(X), np.array(y)
    # How many periods looking back to train
    n_per_in  = 30

    # How many periods ahead to predict
    n_per_out = 10

    # Features (in this case it's 1 because there is only one feature: price)
    n_features = 1

    # Splitting the data into appropriate sequences
    X, y = split_sequence(list(df.close), n_per_in, n_per_out)

    # Reshaping the X variable from 2D to 3D
    X = X.reshape((X.shape[0], X.shape[1], n_features))

    #calling the pre-trained model
    model = keras.models.load_model('static/models/doge_model.h5')

    # Predicting off of y because it contains the most recent dates
    yhat = model.predict(np.array(df.tail(n_per_in)).reshape(1, n_per_in, n_features)).tolist()[0]

    # Transforming the predicted values back to their original prices
    yhat = scaler.inverse_transform(np.array(yhat).reshape(-1,1)).tolist()

    # Creating a DF of the predicted prices
    preds = pd.DataFrame(yhat, index=pd.date_range(start=df.index[-1], periods=len(yhat), freq="D"), columns=df.columns)

    # Printing the predicted prices
    print(preds)

    # Number of periods back to visualize the actual values
    pers = 10

    # Transforming the actual values to their original price
    actual = pd.DataFrame(scaler.inverse_transform(df[["close"]].tail(pers)), index=df.close.tail(pers).index, columns=df.columns).append(preds.head(1))

    # Plotting
    plt.figure(figsize=(16,6))
    plt.plot(actual, label="Actual Prices")
    plt.plot(preds, label="Predicted Prices")
    plt.ylabel("Price")
    plt.xlabel("Dates")
    plt.title(f"Forecasting the next {len(yhat)} days")
    plt.legend()
    plt.savefig("static/images/doge_predictions.png")

    return preds


def tanner_eth():
    endpoint = 'https://min-api.cryptocompare.com/data/histoday'
    res = requests.get(endpoint + '?fsym=ETH&tsym=USD&limit=2000')
    df = pd.DataFrame(json.loads(res.content)['Data'])
    df.drop(['conversionType'], 1, inplace=True)
    df.drop(['conversionSymbol'], 1, inplace=True)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df = df.set_index("time")[['close']].tail(1000)
    df = df.set_index(pd.to_datetime(df.index))

    scaler = MinMaxScaler()
    df = pd.DataFrame(scaler.fit_transform(df), columns=df.columns, index=df.index)


    def split_sequence(seq, n_steps_in, n_steps_out):
        """
        Splits the univariate time sequence
        """
        X, y = [], []

        for i in range(len(seq)):
            end = i + n_steps_in
            out_end = end + n_steps_out

            if out_end > len(seq):
                break

            seq_x, seq_y = seq[i:end], seq[end:out_end]

            X.append(seq_x)
            y.append(seq_y)

        return np.array(X), np.array(y)
    # How many periods looking back to train
    n_per_in  = 30

    # How many periods ahead to predict
    n_per_out = 10

    # Features (in this case it's 1 because there is only one feature: price)
    n_features = 1

    # Splitting the data into appropriate sequences
    X, y = split_sequence(list(df.close), n_per_in, n_per_out)

    # Reshaping the X variable from 2D to 3D
    X = X.reshape((X.shape[0], X.shape[1], n_features))

    #calling the pre-trained model
    model = keras.models.load_model('static/models/eth_model.h5')

    # Predicting off of y because it contains the most recent dates
    yhat = model.predict(np.array(df.tail(n_per_in)).reshape(1, n_per_in, n_features)).tolist()[0]

    # Transforming the predicted values back to their original prices
    yhat = scaler.inverse_transform(np.array(yhat).reshape(-1,1)).tolist()

    # Creating a DF of the predicted prices
    preds = pd.DataFrame(yhat, index=pd.date_range(start=df.index[-1], periods=len(yhat), freq="D"), columns=df.columns)

    # Printing the predicted prices
    print(preds)

    # Number of periods back to visualize the actual values
    pers = 10

    # Transforming the actual values to their original price
    actual = pd.DataFrame(scaler.inverse_transform(df[["close"]].tail(pers)), index=df.close.tail(pers).index, columns=df.columns).append(preds.head(1))

    # Plotting
    plt.figure(figsize=(16,6))
    plt.plot(actual, label="Actual Prices")
    plt.plot(preds, label="Predicted Prices")
    plt.ylabel("Price")
    plt.xlabel("Dates")
    plt.title(f"Forecasting the next {len(yhat)} days")
    plt.legend()
    plt.savefig("static/images/eth_predictions.png")

    return preds
