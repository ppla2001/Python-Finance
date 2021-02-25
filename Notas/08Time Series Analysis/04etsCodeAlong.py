#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %%
airlines = pd.read_csv('C:\\Users\\plape\\OneDrive\\Escritorio\\Python-Finance\\Python-Finance\\Notebooks\\08-Time-Series-Analysis\\airline_passengers.csv',index_col='Month')
# %%
airlines.head()
# %%
airlines.plot() #Parece haber una seasonality muy marcada, con trend a subir
# %%
airlines.dropna(inplace=True) #drop missing values 
# %%
airlines.index = pd.to_datetime(airlines.index)
# %%
airlines.index #lo pase a un datetime 
# %%
from statsmodels.tsa.seasonal import seasonal_decompose
# %%
result = seasonal_decompose(airlines['Thousands of Passengers'],model='multiplicative')
# %%
result.seasonal.plot()
# %%
result.trend.plot()
# %%
fig = result.plot()
# %%
