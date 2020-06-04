import datetime as dt 
import matplotlib.pyplot as plt 
from matplotlib import style
import pandas as pd 
import pandas_datareader.data as web 

style.use('ggplot')

df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0) #Sets datetime as the index instead of adding an additional column of numbers as the index

#DataFrame.rolling provides rolling window calculations

#'windows=100' uses 100 rows, 'min_periods=0' means the calculations will start even if not 100 entries, for example
#   second entry will be avg of first 2 rows, 3rd will be avg of first 3 rows, 101st will be avg of last 100 because that is what the 
#   window is set to
df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean() #Making a new column '100 moving avg'
# df.dropna(inplace=True) # Remove missing values in place so no need to reassign df
print(df.head())

#Generally, each matplotlib thing has a figure and the figure contains all your subplots, most of the time you have 1 subplot (graph)
#   But if you have multiple sub plots (graphs) these are referred to as axis?

#6 rows, 1 column
#starting point = 0,0
#spans 5 rows
#spans 1 column
#On ax2 - 'sharex=ax1' means share the axis with ax1 so whenever we zoom in on ax1, ax2 zooms in as well.
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1) 

#plots a simple line, and lines take x's and y's, x data = date (in our case the date is the index), y data = Adjusted close
ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['Volume'])

plt.show()

