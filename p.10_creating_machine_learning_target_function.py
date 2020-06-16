from collections import Counter
import numpy as np
import pandas as pd 
import pickle 

#Generating whether each stock is a buy/sell/hold

def process_data_for_labels(ticker):
    hm_days = 7 #Amount of days in the future
    df = pd.read_csv('sp500_joined_closes.csv', index_col=0)
    tickers = df.columns.values.tolist()
    df.fillna(0, inplace=True)
    
    for i in range(1, hm_days+1):
        df['{}_{}d'.format(ticker, i)] = (df[ticker].shift(-i) - df[ticker]) / df[ticker]

    df.fillna(0, inplace=True)

    return tickers, df 

#*args lets us pass any number of parameters
def buy_sell_hold(*args):
    cols = [c for c in args]
    requirement = 0.02 # 2%
    for col in cols:
        if col > requirement: #Buy
            return 1 
        if col < -requirement: #Sell
            return -1
    return 0 #Hold

