import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time
from scipy.stats import linregress
from config import akey
from alpha_vantage.cryptocurrencies import CryptoCurrencies
import sqlite3
import csv
from sqlalchemy import create_engine
from flask import make_response

def updateBTC():
    conn = sqlite3.connect("data/crypto.db")
    cur = conn.cursor()
    cur.execute("select max(Date) from btc")
    results = cur.fetchone()
    # print(results[0])
    cc = CryptoCurrencies(key=akey, output_format='pandas')
    data, meta_data = cc.get_digital_currency_daily(symbol='BTC', market='EUR')
    data['Currency'] = 'BTC'
    data.reset_index(inplace=True)
    data.drop(['1a. open (EUR)', '2a. high (EUR)', '3a. low (EUR)','4a. close (EUR)'], axis=1, inplace=True)
    # print(data.columns.values.tolist())
    data.columns = ['Date','Open','High','Low','Close','Volume','MarketCap','Coin']
    data['Date']= pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)
    data['200_MA'] = data['Close'].rolling('200D').mean()
    data['150_MA'] = data['Close'].rolling('150D').mean()
    data['50_MA'] = data['Close'].rolling('50D').mean()
    data['52W_High'] = data['Close'].rolling('365D').max()
    data['52W_Low'] = data['Close'].rolling('365D').min()
    data['Volatility']=(data['High']-data['Low'])/data['Open']
    # print(data.head())
    selected = data.loc[:results[0]]
    selected.reset_index(inplace=True)
    # print(selected.head())
    selected.to_sql('btc', conn, if_exists='append', index=False)

def updateDOGE():
    conn = sqlite3.connect("data/crypto.db")
    cur = conn.cursor()
    cur.execute("select max(Date) from doge")
    results = cur.fetchone()
    print(results[0])
    cc = CryptoCurrencies(key=akey, output_format='pandas')
    data, meta_data = cc.get_digital_currency_daily(symbol='DOGE', market='EUR')
    data['Currency'] = 'DOGE'
    data.reset_index(inplace=True)
    data.drop(['1a. open (EUR)', '2a. high (EUR)', '3a. low (EUR)','4a. close (EUR)'], axis=1, inplace=True)
    print(data.columns.values.tolist())
    data.columns = ['Date','Open','High','Low','Close','Volume','MarketCap','Coin']
    data['Date']= pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)
    data['200_MA'] = data['Close'].rolling('200D').mean()
    data['150_MA'] = data['Close'].rolling('150D').mean()
    data['50_MA'] = data['Close'].rolling('50D').mean()
    data['52W_High'] = data['Close'].rolling('365D').max()
    data['52W_Low'] = data['Close'].rolling('365D').min()
    data['Volatility']=(data['High']-data['Low'])/data['Open']
    doge_csv = data[['Open','High','Low','Close','Volume', 'Volatility']]
    doge_csv.reset_index(inplace=True)
    doge_csv.to_csv('static/updated_csv/doge_current.csv')
    print(data.head())
    selected = data.loc[:results[0]]
    selected.reset_index(inplace=True)
    print(selected.head())
    selected.to_sql('doge', conn, if_exists='append', index=False)

def updateETH():
    conn = sqlite3.connect("data/crypto.db")
    cur = conn.cursor()
    cur.execute("select max(Date) from eth")
    results = cur.fetchone()
    # print(results[0])
    cc = CryptoCurrencies(key=akey, output_format='pandas')
    data, meta_data = cc.get_digital_currency_daily(symbol='ETH', market='EUR')
    data['Currency'] = 'ETH'
    data.reset_index(inplace=True)
    data.drop(['1a. open (EUR)', '2a. high (EUR)', '3a. low (EUR)','4a. close (EUR)'], axis=1, inplace=True)
    # print(data.columns.values.tolist())
    data.columns = ['Date','Open','High','Low','Close','Volume','MarketCap','Coin']
    data['Date']= pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)
    data['200_MA'] = data['Close'].rolling('200D').mean()
    data['150_MA'] = data['Close'].rolling('150D').mean()
    data['50_MA'] = data['Close'].rolling('50D').mean()
    data['52W_High'] = data['Close'].rolling('365D').max()
    data['52W_Low'] = data['Close'].rolling('365D').min()
    data['Volatility']=(data['High']-data['Low'])/data['Open']
    # print(data.head())
    selected = data.loc[:results[0]]
    selected.reset_index(inplace=True)
    # print(selected.head())
    selected.to_sql('eth', conn, if_exists='append', index=False)