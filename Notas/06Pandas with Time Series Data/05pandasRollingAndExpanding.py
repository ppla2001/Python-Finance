#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %%
df = pd.read_csv('C:\\Users\\plape\\OneDrive\\Escritorio\\Python-Finance\\Python-Finance\\Notebooks\\05-Pandas-with-Time-Series\\time_data\\walmart_stock.csv',index_col='Date',parse_dates=True)
# %%
df.head()
# %%
df['Open'].plot(figsize=(16,6))
# %%
df.rolling(window=7).mean().head(14) #los primeros 6 dias estan con NaN porq especifique q queria 7 dias, no hay suficiente informacion para rellenar los primeros 6 dias, el valor del dia 2012-01-10 es el promedio de los primeros 7 dias, la data se hace mas reflective del trend de la data  
# %%
df['Open'].plot()
df.rolling(window=30).mean()['Close'].plot(figsize=(16,6))
# %%
#add legend
df['Close 30 Day Moving Average'] = df['Close'].rolling(window=30).mean()
df[['Close 30 Day Moving Average','Close']].plot(figsize=(16,6))
# %%
df['Close'].expanding().mean().plot(figsize=(16,6)) #este grafico representa at each particular time stamp on the x axis what is shown in the y axis is the actual value of everything that came before it averaged out, el ultimo point es el average de todo lo q vino antes 
# %%
#BOOLINGER BANDS FINANCIAL GRAPHS
#Que es? Son volatility bands placed above and below a moving average, donde la volatility is based on standard deviation, bands will widen when volatility increases and narrow when volatility decreases, prices are said to be relatively high when price is above the upper band
#Como se hace?
#Primero se hace la band de Close 20 Moving Average
df['Close: 20 Day Mean'] = df['Close'].rolling(window=20).mean()
#Despues haces la Upper baand = 20MA + 2*standard deviation over 20 days 
df['Upper'] = df['Close: 20 Day Mean'] + 2*(df['Close'].rolling(window=20).std())
#Despues lower band = 20MA - 2*std(20)
df['Lower'] = df['Close: 20 Day Mean'] - 2*(df['Close'].rolling(window=20).std())
#Por ultimo Close
df[['Close','Close: 20 Day Mean','Upper','Lower']].plot(figsize=(50,30))
# %%
