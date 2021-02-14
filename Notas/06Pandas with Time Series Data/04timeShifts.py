#%%
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
# %%
df = pd.read_csv('C:\\Users\\plape\\OneDrive\\Escritorio\\Python-Finance\\Python-Finance\\Notebooks\\05-Pandas-with-Time-Series\\time_data\\walmart_stock.csv',index_col='Date',parse_dates=True)
# %%
df.head()
# %%
df.tail()
# %%
#mover la info a otro index position
df.shift(periods=1) #1 period = 1 index row
# %%
#shift backwards 
df.shift(periods=-1)
# %%
#tshift and frequency argument
df.tshift(freq='A') #Time string code q puedo ver en notebook o documentation, no pierdo info, se me mueve todo al time string code
# %%
