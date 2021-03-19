#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %%
aapl = pd.read_csv('C:\\Users\\plape\\OneDrive\\Escritorio\\Python-Finance\\Python-Finance-1\\Notebooks\\09-Python-Finance-Fundamentals\\AAPL_CLOSE',index_col='Date',parse_dates=True)
csco = pd.read_csv('C:\\Users\\plape\\OneDrive\\Escritorio\\Python-Finance\\Python-Finance-1\\Notebooks\\09-Python-Finance-Fundamentals\\CISCO_CLOSE',index_col='Date',parse_dates=True)
ibm = pd.read_csv('C:\\Users\\plape\\OneDrive\\Escritorio\\Python-Finance\\Python-Finance-1\\Notebooks\\09-Python-Finance-Fundamentals\\IBM_CLOSE',index_col='Date',parse_dates=True)
amzn = pd.read_csv('C:\\Users\\plape\\OneDrive\\Escritorio\\Python-Finance\\Python-Finance-1\\Notebooks\\09-Python-Finance-Fundamentals\\AMZN_CLOSE',index_col='Date',parse_dates=True)
# %%
stocks = pd.concat([aapl,csco,ibm,amzn],axis=1)
stocks.columns=['aapl','cisco','ibm','amzn']
# %%
stocks.head()
# %%
#Mean daily return
stocks.pct_change(1).mean()
# %%
#Pearson Correlation coefficient between all time series
stocks.pct_change(1).corr()
# %%
stocks.pct_change(1).head()
#VS
# %%
#Logarithmic returns
log_ret = np.log(stocks/stocks.shift(1))
log_ret.head()
# %%
log_ret.hist(bins=100,figsize=(12,8))
plt.tight_layout()
# %%
log_ret.mean()
# %%
#Covariance of columns
log_ret.cov()
# %%
#Covariance multiplied by number of business days 
log_ret.cov() * 252
# %%
#Some random allocation
np.random.seed(101)
print(stocks.columns)

weights = np.array(np.random.random(4))
print('Random Weights')
print(weights)

print('Rebalance')
weights = weights / np.sum(weights)
print(weights)

#Expected return
print('Expected Portfolio Return')
exp_ret = np.sum( (log_ret.mean() * weights) * 252)
print(exp_ret)

#Expected Volatility 
print('Expected Volatility')
exp_vol = np.sqrt(np.dot(weights.T,np.dot(log_ret.cov()*252,weights)))
print(exp_vol)

#Sharpe Ratio
print('Sharpe Ratio')
SR = exp_ret / exp_vol
print(SR)
# %%
#Thousands of Allocations
np.random.seed(101)

num_port = 5000
all_weights = np.zeros((num_port,len(stocks.columns)))
ret_arr = np.zeros(num_port)
vol_arr = np.zeros(num_port)
sharpe_arr = np.zeros(num_port)

for ind in range(num_port):

    #Weights
    weights = np.array(np.random.random(4))
    weights = weights / np.sum(weights)

    #Save Weights
    all_weights[ind,:] = weights
    
    #Expected return
    ret_arr[ind] = np.sum( (log_ret.mean() * weights) * 252)

    #Expected Volatility 
    vol_arr[ind] = np.sqrt(np.dot(weights.T,np.dot(log_ret.cov()*252,weights)))

    #Sharpe Ratio
    sharpe_arr[ind] = ret_arr[ind] / vol_arr[ind]

# %%
sharpe_arr.max()
# %%
sharpe_arr.argmax()
# %%
all_weights[1420,:]
# %%
max_sr_ret = ret_arr[1420]
max_sr_vol = vol_arr[1420]
# %%
plt.figure(figsize=(12,8))
plt.scatter(vol_arr,ret_arr,c=sharpe_arr,cmap='plasma')
plt.colorbar(label='Sharpe Ratio')
plt.xlabel('Volatility')
plt.ylabel('Return')

plt.scatter(max_sr_vol,max_sr_ret,c='red',s=50,edgecolors='black')

# %%
