import datetime as dt 
import matplotlib.pyplot as plt 
from matplotlib import style
import mplfinance as mpf #New
from mplfinance.original_flavor import candlestick_ohlc #Allows users to use older syntax from the deprecated mpl_finance module
import matplotlib.dates as mdates #Matplot lib does not use datetime dates
import pandas as pd 
import pandas_datareader.data as web 

style.use('ggplot')

df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0) 
# df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean() 

#Resampling - Take some information and resample it to a specific time period such as one hour, I'm guessing sort of 
#   condesing that information?

#Generally when resampling, you're going to make a new dataframe

#'10Min', weekly biweekly, all types of periods you can choose from
#Takes an average EVERY 10 DAYS, unlike a 10 day rolling avg which is the avg of the last 10 days for each day
#.mean(), .sum(), .ohlc() - 'open high low close'
df_ohlc = df['Adj Close'].resample('10D').ohlc() 
df_volume = df['Volume'].resample('10D').sum() # This will provide the true total volume over the 10 day period

# print(df_ohlc.head())
#                   open        high         low       close
# Date                                                      
# 2019-01-02  310.119995  347.260010  300.359985  347.260010
# 2019-01-12  334.399994  347.309998  302.260010  302.260010
# 2019-01-22  298.920013  308.769989  287.589996  307.019989
# 2019-02-01  312.209991  321.350006  305.799988  305.799988
# 2019-02-11  312.839996  312.839996  302.559998  302.559998

# candlestick_ohlc takes 'date', 'open', 'high', 'low', 'close'
df_ohlc.reset_index(inplace=True) #resets the index in place. #Removes 'date' as the index
# print(df_ohlc.head())

df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num) #converts our date time object to an mdate number which is needed apparently
# print(df_ohlc.head())

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1) 
ax1.xaxis_date()

# mpf.plot(df, type='candlestick', mav=20, volume=True)
candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')

#setting 'df_volume.index.map(mdates.date2num)' to x axis, and 'df_volume.values' to y axis
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)
plt.show() #BOOM, cool graph
