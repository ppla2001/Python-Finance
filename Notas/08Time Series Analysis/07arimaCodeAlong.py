#%% 
#PRIMER PASO
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import model
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
#ACF & PACF
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
# %%
fig_first = plot_acf(df['First Difference'].dropna())
# %%
fig_seasonal_first = plot_acf(df['Seasonal First Difference'].dropna())
# %%
from pandas.plotting import autocorrelation_plot
# %%
autocorrelation_plot(df['Seasonal First Difference'].dropna())
# %%
#Partial Correlation Plot
result = plot_pacf(df['Seasonal First Difference'].dropna())
# %%
#FINAL ACF PACF plots 
plot_acf(df['Seasonal First Difference'].dropna())
plot_pacf(df['Seasonal First Difference'].dropna())
# %%
#Como la data es seasonal, vamos a usar seasonal arima model
from statsmodels.tsa.arima_model import ARIMA
# %%
model = sm.tsa.statespace.SARIMAX(df['Milk in Pounds per Cow'],order=(0,1,0),seasonal_order=(1,1,1,12)) #order, seasonal order
# %%
results = model.fit()
# %%
print(results.summary())
# %%
#residual errors
results.resid
# %%
results.resid.plot()
# %%
results.resid.plot(kind='kde')
# %%
#No puedo hacer forecast mas alla de la cantidad de puntos de data q hay en el df, para eso le tengo q agregar tiempo al df usando pandas
df['forecast'] = results.predict(start=150,end=168)
df[['Milk in Pounds per Cow','forecast']].plot(figsize=(12,8))
# %%
#agrego tiempo
from pandas.tseries.offsets import DateOffset
# %%
future_dates = [df.index[-1] + DateOffset(months=x) for x in range(1,24)]
# %%
future_dates
# %%
future_df = pd.DataFrame(index=future_dates,columns=df.columns)
# %%
future_df
# %%
final_df = pd.concat([df,future_df])
# %%
final_df['forecast'] = results.predict(start=168,end=192)
# %%
final_df.tail()
# %%
final_df['Milk in Pounds per Cow'].plot()
final_df['forecast'].plot()
# %%
final_df[['Milk in Pounds per Cow','forecast']].plot(figsize=(12,8))
# %%
