#%%
#Parte 0 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
# %%
#Parte 1
#FIJARME EN SOLUTIONS COMO SE HACIA PARA SACAR INFO SIN TENER CSV
tesla = pd.read_csv('C:\\Users\\plape\\OneDrive\\Escritorio\\Python-Finance\\Python-Finance\\Notebooks\\07-Stock-Market-Analysis-Capstone-Project\\Tesla_Stock.csv',index_col='Date',parse_dates=True)

ford = pd.read_csv('C:\\Users\\plape\\OneDrive\\Escritorio\\Python-Finance\\Python-Finance\\Notebooks\\07-Stock-Market-Analysis-Capstone-Project\\Ford_Stock.csv',index_col='Date',parse_dates=True)

general_m = pd.read_csv('C:\\Users\\plape\\OneDrive\\Escritorio\\Python-Finance\\Python-Finance\\Notebooks\\07-Stock-Market-Analysis-Capstone-Project\\GM_Stock.csv',index_col='Date',parse_dates=True)
# %%
tesla.head()
# %%
ford.head()
# %%
general_m.head()
# %%
#Parte 2 
tesla['Open'].plot(label='Tesla',figsize=(16,6),title='Open Price')
ford['Open'].plot(label='Ford')
general_m['Open'].plot(label='General Motors')
plt.legend()
# %%
tesla['Volume'].plot(label='Tesla',figsize=(16,6),title='Volume')
ford['Volume'].plot(label='Ford')
general_m['Volume'].plot(label='General Motors')
plt.legend()
# %%
#Bonus
ford['Volume'].argmax()
# What happened:
# http://money.cnn.com/2013/12/18/news/companies/ford-profit/
# https://www.usatoday.com/story/money/cars/2013/12/18/ford-2014-profit-warning/4110015/
# https://media.ford.com/content/dam/fordmedia/North%20America/US/2014/01/28/4QFinancials.pdf
# %%
tesla['Total Traded'] = tesla['Open'] * tesla['Volume']
tesla.head()
# %%
ford['Total Traded'] = ford['Open'] * ford['Volume']
ford.head()
# %%
general_m['Total Traded'] = general_m['Open'] * general_m['Volume']
general_m.head()
# %%
tesla['Total Traded'].plot(label='Tesla',figsize=(16,6))
ford['Total Traded'].plot(label='Ford')
general_m['Total Traded'].plot(label='General Motors')
plt.ylabel('Total Traded')
plt.legend()
# %%
tesla['Total Traded'].argmax()
# http://money.cnn.com/2014/02/25/investing/tesla-record-high/
# https://blogs.wsj.com/moneybeat/2014/02/25/tesla-shares-surge-on-morgan-stanley-report/
# https://www.washingtonpost.com/news/wonk/wp/2014/02/25/teslas-stock-is-up-644-why-it-may-not-last/
# http://www.cnbc.com/2014/02/25/tesla-soars-ford-falls-in-consumer-reports-study.html
# %%
#Moving Average for 50 and 200
general_m['MA50'] = general_m['Open'].rolling(50).mean()
general_m['MA200'] = general_m['Open'].rolling(200).mean()
general_m[['Open','MA50','MA200']].plot(figsize=(16,6),title='Moving Average General Motors')
# %%
from pandas.plotting import scatter_matrix
# %%
comparison = pd.concat([tesla['Open'],general_m['Open'],ford['Open']],axis=1)
# %%
comparison.columns = ['Tesla Open','GM Open','Ford Open']
# %%
scatter_matrix(comparison,figsize=(8,8),alpha=0.2,hist_kwds={'bins':50});
# %%
from mpl_finance import candlestick_ohlc
from matplotlib.dates import DateFormatter, date2num, WeekdayLocator, DayLocator, MONDAY

# Rest the index to get a column of January Dates
ford_reset = ford.loc['2012-01':'2012-01'].reset_index()

# Create a new column of numerical "date" values for matplotlib to use
ford_reset['date_ax'] = ford_reset['Date'].apply(lambda date: date2num(date))
ford_values = [tuple(vals) for vals in ford_reset[['date_ax', 'Open', 'High', 'Low', 'Close']].values]

mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
alldays = DayLocator()              # minor ticks on the days
weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
dayFormatter = DateFormatter('%d')      # e.g., 12

#Plot it
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)
ax.xaxis.set_major_locator(mondays)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(weekFormatter)

candlestick_ohlc(ax, ford_values, width=0.6, colorup='g',colordown='r');
# %%
#Parte 3 
#Esta es una forma
tesla['returns'] = (tesla['Close'] / tesla['Close'].shift(1)) - 1
tesla['returns']
# %%
#Esta es otra forma de hacer lo de arriba
tesla['returns'] = tesla['Close'].pct_change(1)
tesla['returns']
# %%
ford['returns'] = ford['Close'].pct_change(1)
general_m['returns'] = general_m['Close'].pct_change(1)
# %%
tesla.head()
# %%
ford['returns'].hist(bins=100)
# %%
general_m['returns'].hist(bins=100)
# %%
tesla['returns'].hist(bins=100)
# %%
#stacking histograms together
tesla['returns'].hist(bins=100,label='Tesla',figsize=(10,8),alpha=0.4)
ford['returns'].hist(bins=100,label='Ford',figsize=(10,8),alpha=0.4)
general_m['returns'].hist(bins=100,label='General Motors',figsize=(10,8),alpha=0.4)
plt.legend()
# %%
#Kernel Density Estimation Plot
tesla['returns'].plot(kind='kde',label='Tesla',figsize=(10,8))
ford['returns'].plot(kind='kde',label='Ford',figsize=(10,8))
general_m['returns'].plot(kind='kde',label='General Motors',figsize=(10,8))
plt.legend()
# %%
#Box Plots
box_df = pd.concat([tesla["returns"],ford['returns'],general_m['returns']],axis=1)
box_df.columns = ['Tesla Returns','Ford Returns','General Motors Returns']
box_df.plot(kind='box',figsize=(8,11))
# %%
#Comparing Daily Returns Between Stocks 
scatter_matrix(box_df,figsize=(8,8),alpha=0.2,hist_kwds={'bins':100});
# %%
box_df.plot(kind='scatter',x='Ford Returns',y='General Motors Returns',alpha=0.5,figsize=(8,8))
#Tend to be correlated, we can do a linear regression graph
# %%
