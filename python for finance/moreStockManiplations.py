import datetime as dt
import matplotlib.pyplot as plt  # create graphs
from matplotlib import style

import mplfinance as mpf
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc
import pandas as pd
import pandas_datareader.data as web  # grab data from an api

style.use('ggplot')

df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)

# 10days, mean : the average value, ohlc: open high low close
df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()

df_ohlc.reset_index(inplace=True)  # convert to date

df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)  # convert date to mdate
# print(df_ohlc.head())


ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)  # first graph
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)
ax1.xaxis_date()  # take mdate and display it as a date

candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)
plt.show()





