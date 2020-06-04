import datetime as dt 
import matplotlib.pyplot as plt 
from matplotlib import style
import pandas as pd 
import pandas_datareader.data as web 

style.use('ggplot')

# start = dt.datetime(2020, 1, 1)
# end = dt.datetime(2020, 4, 20)

# df = web.DataReader('TSLA', 'yahoo', start, end) 
# df.to_csv('tsla.csv') #taking the data and converting it to a CSV file named 'tsla.csv'

# With Pandas, can read csv, json, excel, sql tables, all kinds of input/output

# df = pd.read_csv('tsla.csv') #If you already had a CSV file, this allows you to read it in
df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0) #Sets datetime as the index instead of adding an additional column of numbers as the index
# print(df.head(10))

# df.plot() #plots the dataframe onto a graph against the datetime as the index
df['Adj Close'].plot() #plots the Adj Close column of the graph 
plt.show() #Display the graph
# print(df['Adj Close'].head(10)) #Print just the adjusted close for the first 10 rows
# print(df[['Open', 'High']].head(10)) #Print multiple properties




