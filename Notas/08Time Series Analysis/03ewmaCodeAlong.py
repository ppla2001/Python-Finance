#%%
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
# %%
airlines = pd.read_csv('C:\\Users\\plape\\OneDrive\\Escritorio\\Python-Finance\\Python-Finance\\Notebooks\\08-Time-Series-Analysis\\airline_passengers.csv',index_col='Month')
# %%
airlines.head()
# %%
airlines.dropna(inplace=True)
# %%
airlines.index = pd.to_datetime(airlines.index)
# %%
airlines.head()
# %%
#simple moving average 
airlines['6-Month-SMA'] = airlines['Thousands of Passengers'].rolling(window=6).mean()
# %%
airlines['12-Month-SMA'] = airlines['Thousands of Passengers'].rolling(window=12).mean()
# %%
airlines.plot()
# %%
#EXPONENTIALLY WEIGHTED MOVING AVERAGE
airlines['EWMA-12'] = airlines['Thousands of Passengers'].ewm(span=12).mean()
# %%
airlines[['Thousands of Passengers','EWMA-12']].plot()
# %%
#MIRAR DESDE MINUTO 8 DE EWMA CODE ALONG PARA VER DATOS IMPORTANTES 