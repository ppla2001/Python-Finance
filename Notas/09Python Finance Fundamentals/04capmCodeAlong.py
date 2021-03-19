#%%
from scipy import stats
# %%
import pandas as pd
import pandas_datareader as web
# %%
start = pd.to_datetime('2010-01-04')
end = pd.to_datetime('2017-07-25')
# %%
spy_etf = web.DataReader('SPY','yahoo',start,end)
# %%
spy_etf.info()
# %%
spy_etf.head()
# %%
aapl = web.DataReader('AAPL','yahoo',start,end)
# %%
aapl.head()
# %%
aapl.tail()
# %%
#CAPM says aapl stock performance has to have some relationship with overall market performance (spy_etf) 
# %%
import matplotlib.pyplot as plt
# %%
aapl['Close'].plot(label='AAPL',figsize=(10,8))
spy_etf['Close'].plot(label='SPY Index')
plt.legend()
# %%
#Compare Cumulative Return
aapl['Cumulative'] = aapl['Close'] / aapl['Close'].iloc[0]
spy_etf['Cumulative'] = spy_etf['Close'] / spy_etf['Close'].iloc[0]
# %%
aapl['Cumulative'].plot(label='AAPL',figsize=(10,8))
spy_etf['Cumulative'].plot(label='SPY')
plt.legend()
# %%
#Daily Return
aapl['Daily Return'] = aapl['Close'].pct_change(1)
spy_etf['Daily Return'] = spy_etf['Close'].pct_change(1)
# %%
plt.scatter(aapl['Daily Return'],spy_etf['Daily Return'],alpha=0.25)
# %%
beta,alpha,r_value,p_value,std_error = stats.linregress(aapl['Daily Return'].iloc[1:],spy_etf['Daily Return'].iloc[1:])
# %%
beta
# %%
alpha
# %%
r_value
# %%
spy_etf['Daily Return'].head()
# %%
import numpy as np
# %%
noise = np.random.normal(0,0.001,len(spy_etf['Daily Return'].iloc[1:]))
# %%
noise
# %%
fake_stock = spy_etf['Daily Return'].iloc[1:] + noise
# %%
plt.scatter(fake_stock,spy_etf['Daily Return'].iloc[1:],alpha=0.25)
# %%
beta,alpha,r_value,p_value,std_error = stats.linregress(fake_stock,spy_etf['Daily Return'].iloc[1:])
# %%
beta
# %%
alpha
# %%
