#%%
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
# %%
df = pd.read_csv('C:\\Users\\plape\\OneDrive\\Escritorio\\Python-Finance\\Python-Finance\\Notebooks\\05-Pandas-with-Time-Series\\time_data\\walmart_stock.csv')
# %%
df.head()
#Quiero cambiar el index a que sean las fechas, hay dos formas de hacerlo:
# %%
#Forma mas larga pero con mas control
df.info() #veo q date es object entonces hay q convertirlo en datetime object:
# %%
df['Date'] = pd.to_datetime(df['Date'],format='%Y-%m-%d') #format me tengo q fijar en la documentation o notebook para ver q significa cada uno
# %%
df.info() #aunque con df.head() se ve igual, usando esto puedo ver que cambio a datetime64(ns) osea a un objeto datetime
# %%
df.set_index('Date',inplace=True)
# %%
df
# %%
#Forma mas corta
df = pd.read_csv('C:\\Users\\plape\\OneDrive\\Escritorio\\Python-Finance\\Python-Finance\\Notebooks\\05-Pandas-with-Time-Series\\time_data\\walmart_stock.csv',index_col='Date',parse_dates=True) #Esto me mantiene las fechas como strings, voy a tener q cambiarle la estructura despues, parse dates intenta de pasar el index a datetime object
# %%
df.index
# %%
#Time Resampling 
df.resample(rule='A') #Rule esta en el notebook con todo lo q puedo poner
# %%
df.resample(rule='A').mean() #te devuelve el mean q tuvo cada ano 
# %%
df.resample(rule='A').max()
# %%
def first_day(entry):
    return entry[0]
# %%
df.resample('A').apply(first_day)
# %%
#yearly end mean
df['Close'].resample('M').mean().plot(kind='bar',figsize=(16,6))
# %%
