#%% 
#PRIMER PASO
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
# %%
df = pd.read_csv('C:\\Users\\plape\\OneDrive\\Escritorio\\Python-Finance\\Python-Finance\\Notebooks\\08-Time-Series-Analysis\\monthly-milk-production-pounds-p.csv')
# %%
df.head()
# %%
df.columns = ['Month','Milk in Pounds per Cow']
# %%
df.drop(168,axis=0,inplace=True)
# %%
df['Month'] = pd.to_datetime(df['Month'])
# %%
df.set_index('Month',inplace=True)
# %%
df.index
# %%
df.describe().transpose()
# %%
#SEGUNDO PASO
df.plot()
# %%
time_series = df['Milk in Pounds per Cow']
# %%
time_series.rolling(12).mean().plot(label='12 Month Rolling Mean')
time_series.rolling(12).std().plot(label='12 Month Rolling Std')
time_series.plot()
plt.legend()
# %%
#ETS DECOMPOSITION PLOT
from statsmodels.tsa.seasonal import seasonal_decompose
# %%
decomp = seasonal_decompose(time_series)
# %%
fig = decomp.plot()
fig.set_size_inches(15,8)
# %%
#TEST DATA IF STATIONARY OR NOT
from statsmodels.tsa.stattools import adfuller
# %%
result = adfuller(df['Milk in Pounds per Cow'])
# %%
def adf_check(time_series):
    result = adfuller(time_series)
    print('Augmented Dicky-Fuller Test')
    labels = ['ADF Test Statistic','p-value','Num of lags','Num of Observations']
    
    for value,label in zip(result,labels):
        print(label + ' : '+str(value))
    
    if result[1] <= 0.05:
        print('Strong evidence against null hypotesis')
        print('Reject null hypotesis')
        print('Data has no unit root and is stationary')
    else:
        print('Weak evidence against null hypotesis')
        print('Fail to reject null hypotesis')
        print('Data has unit root, it is non stationary')
# %%
adf_check(df['Milk in Pounds per Cow'])
# %%
df['First Difference'] = df['Milk in Pounds per Cow'] - df['Milk in Pounds per Cow'].shift(1)
# %%
df['First Difference'].plot()
# %%
adf_check(df['First Difference'].dropna())
# %%
df['Milk Second Difference'] = df['First Difference'] - df['First Difference'].shift(1)
# %%
adf_check(df['Milk Second Difference'].dropna())
# %%
#seasonal difference
df['Seasonal Difference'] = df['Milk in Pounds per Cow'] - df['Milk in Pounds per Cow'].shift(12)
# %%
df['Seasonal Difference'].plot()
# %%
adf_check(df['Seasonal Difference'].dropna())
# %%
df['Seasonal First Difference'] = df['First Difference'] - df['First Difference'].shift(12)
# %%
df['Seasonal First Difference'].plot()
# %%
adf_check(df['Seasonal First Difference'].dropna())
# %%
