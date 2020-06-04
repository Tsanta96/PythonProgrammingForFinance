import datetime as dt #The datetime module supplies classes for manipulating dates and times
import matplotlib.pyplot as plt #Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.
from matplotlib import style
import pandas as pd #pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.
import pandas_datareader.data as web #Provides up to date remote data access for pandas, works for multiple versions of pandas.

style.use('ggplot')

start = dt.datetime(2000, 1, 1)
end = dt.datetime(2020, 4, 20)

df = web.DataReader('TSLA', 'yahoo', start, end) #Creating a dataframe with data coming from the yahoo API

# print(df.head(10)) #Prints first 10 rows of data
print(df.tail(10)) #Prints last 10 rows of data