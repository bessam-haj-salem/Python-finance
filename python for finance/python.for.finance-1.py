import datetime as dt
import matplotlib.pyplot as plt  # create graphs
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web  # grab data from an api

style.use('ggplot')
# start = dt.datetime(2000,1,1)
# end= dt.datetime(2016,12,31)

# df = web.DataReader('TSLA','yahoo', start, end)  # DATA FRAME ,  TSLA: ticker symbol of a company TESLA
# print(df.head(6)) # give us the number of raws of the table
# df.to_csv('tsla.csv')#take this data frame and export in csv file

# convert csv to a readble frame
df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)
# print(df.head())
# df.plot() # give you the graph
# df['Adj Close'].plot()  # Choose the column "adj close"
# print(df['Adj Close'])  # print the choosed column
# print(df[['Open', 'High']].head())  # select OPen and High column
# plt.show()
df['100ma'] = df['Adj Close'].rolling(
    window=100, min_periods=0).mean()  # moving average
# df.dropna(inplace=True) # == : df = df.dropna, this the way the have the first 100 days populated

print(df.head())

# number of 6 rows and 1 column , start on row:0 column:0 top corner,
ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)  # first graph
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1,
                       colspan=1, sharex=ax1)  # second graph, sharex will share only the zoom

ax1.plot(df.index, df['Adj Close'])  # here two superpose chartss
ax1.plot(df.index, df['100ma'])
ax2.plot(df.index, df['Volume'])  # another chart alone

plt.show()
