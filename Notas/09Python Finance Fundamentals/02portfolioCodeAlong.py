#%%
import pandas as pd
from pandas.core.indexes.interval import SetopCheck
import quandl
# %%
start = pd.to_datetime('2012-01-01')
end = pd.to_datetime('2017-01-01')
# %%
aapl = quandl.get('WIKI/AAPL.11',start_date = start, end_date = end)
cisco = quandl.get('WIKI/CSCO.11',start_date = start, end_date = end)
ibm = quandl.get('WIKI/IBM.11',start_date = start, end_date = end)
amzn = quandl.get('WIKI/AMZN.11',start_date = start, end_date = end)
# %%
aapl
# %%
aapl.iloc[0]['Adj. Close']
# %%
#Cumulative Return or Normalizing a price
for stock_df in (aapl,cisco,ibm,amzn):
    stock_df['Normed Return'] = stock_df['Adj. Close'] / stock_df.iloc[0]['Adj. Close']
# %%
aapl.head()
# %%
aapl.tail()
# %%
#Have some allocations in portfolio
#30% in aapl
#20% in csco
#40% in amzn
#10% in ibm
# %%
for stock_df, allo in zip((aapl,cisco,ibm,amzn),[.3,.2,.4,.1]):
    stock_df['Allocation'] = stock_df['Normed Return'] * allo
# %%
aapl.head()
# %%
#supongamos q puse x cantidad de plata en un stock, multiplico lo q inverti por allocation y me da la ganancia 
for stock_df in (aapl,cisco,ibm,amzn):
    stock_df['Position Values'] = stock_df['Allocation'] * 1000000
# %%
aapl.head()
# %%
all_pos_vals = [aapl['Position Values'],cisco['Position Values'],ibm['Position Values'],amzn['Position Values']]
portfolio_val = pd.concat(all_pos_vals,axis=1)
# %%
portfolio_val.head()
# %%
portfolio_val.columns = ['AAPL Position','CSCO Position','IBM Position','AMZN Position']
# %%
portfolio_val['Total Position'] = portfolio_val.sum(axis=1)
# %%
portfolio_val.head()
# %%
import matplotlib.pyplot as plt
# %%
portfolio_val['Total Position'].plot(figsize=(12,10))
plt.title('Total Portfolio Value')
# %%
portfolio_val.drop('Total Position',axis=1).plot(figsize=(12,10))
# %%
#Portfolio Allocation Part 2
#Portfolio Statistics
# %%
#Daily Returns
portfolio_val['Daily Return'] = portfolio_val['Total Position'].pct_change(1)
# %%
#Average Daily Return
portfolio_val['Daily Return'].mean()
# %%
#Daily Return Standard Deviation
portfolio_val['Daily Return'].std()
# %%
portfolio_val['Daily Return'].plot(kind='hist',figsize=(4,5),bins=100)
# %%
portfolio_val['Daily Return'].plot(kind='kde',figsize=(4,5))
# %%
#Overall % on return or cumulative return
cumulative_return = 100* (portfolio_val['Total Position'][-1]/portfolio_val['Total Position'][0] - 1)
# %%
cumulative_return
# %%
#Sharpe Ratio
SR = portfolio_val['Daily Return'].mean() / portfolio_val['Daily Return'].std()
# %%
SR
# %%
#Si quiero daily voy a tener q multiplicar SR por un K-value, como es daily tengo q agarrar la square root de la cantidad de business days en el year como k-value
ANUALIZED_SR = (252 ** 0.5) * SR
# %%
ANUALIZED_SR
# %%
# SR > 1 se considera aceptable 
# SR > 2 Very Good
# SR > 3 Excellent