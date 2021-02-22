#%%
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
# %%
import statsmodels.api as sm
# %%
df = sm.datasets.macrodata.load_pandas().data
# %%
df
# %%
#Para q me tire toda la data
print(sm.datasets.macrodata.NOTE)
# %%
df.head()
# %%
#pasar q la fecha sea el index con statsmodels
index = pd.Index(sm.tsa.datetools.dates_from_range('1959Q1','2009Q3')) #1959Q1 significa q quiero q el start date sea el first quarter de 1959
df.index = index
# %%
df.head()
# %%
df['realgdp'].plot()
# %%
#get the trend using statsmodels 
result = sm.tsa.filters.hpfilter(df['realgdp']) #me devuelve tuple
# %%
result[0] #me devuelve series
# %%
#buscando el trend de lo q hace el realgdp
gdp_cycle, gdp_trend = sm.tsa.filters.hpfilter(df['realgdp'])
# %%
df['trend'] = gdp_trend
# %%
df[['realgdp','trend']].plot()
# %%
#para hacerle zoom a una parte del grafico
df[['realgdp','trend']]['2000-03-31':].plot()
# %%
