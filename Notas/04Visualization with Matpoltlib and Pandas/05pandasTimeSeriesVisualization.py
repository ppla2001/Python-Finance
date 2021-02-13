#%%
import pandas as pd
import matplotlib.pyplot as plt

# %%
mcdon = pd.read_csv('C:\\Users\\plape\\OneDrive\\Escritorio\\Python-Finance\\Python-Finance\\Notebooks\\04-Visualization-Matplotlib-Pandas\\04-02-Pandas Visualization\\mcdonalds.csv',index_col='Date',parse_dates=True)
mcdon.head()
# %%
mcdon['Adj. Close'].plot()
# %%
mcdon['Adj. Volume'].plot(figsize=(12,4))
# %%
mcdon['Adj. Close'].plot(xlim=['2007-01-01','2009-01-01'],ylim=(20,50)) #Agarrando una parte de datos de dataframe y me intereso una parte en especifico entonces me centro en eso
# %%
mcdon['Adj. Close'].plot(xlim=['2007-01-01','2009-01-01'],ylim=(20,50),ls='--',c='red') #ls = linestyle
# %%
import matplotlib.dates as dates 
# %%
#quiero mostrar x ticks 
mcdon['Adj. Close'].plot(xlim=['2007-01-01','2009-01-01'],ylim=(0,50))
# %%
idx = mcdon.loc['2007-01-01':'2007-05-01'].index #si estoy usando todo el dataframe usaria mcdon.index
idx
# %%
stock = mcdon.loc['2007-01-01':'2007-05-01']['Adj. Close']
stock
# %%
fig,ax = plt.subplots()
ax.plot_date(idx, stock,'-')
#grid lines
ax.yaxis.grid(True)
ax.xaxis.grid(True)
fig.autofmt_xdate() #me arregla el formato del x axis
#plt.tight_layout() #deberia arreglarme el formato, pero a veces no me lo arregla y hay q usar el de arriba
plt.show()
# %%
#hacer q haya menos informacion en el x axis, solo quiero q haya meses
fig,ax = plt.subplots()
ax.plot_date(idx, stock,'-')
#Formateando X axis con
#LOCATING method
ax.xaxis.set_major_locator(dates.MonthLocator())
#Formateando el Locating method
ax.xaxis.set_major_formatter(dates.DateFormatter('%b-%y')) #%b etc puedo ver en resource codes

fig.autofmt_xdate() 
#HICE SOLO LOS MAJOR X AXIS
# %%
#AHORA MAJOR Y MINOR X AXIS
fig,ax = plt.subplots()
ax.plot_date(idx, stock,'-')
#LOCATING method
ax.xaxis.set_major_locator(dates.MonthLocator())
#Formateando el Locating method
ax.xaxis.set_major_formatter(dates.DateFormatter('\n\n\n\n%b-%y'))

ax.xaxis.set_minor_locator(dates.WeekdayLocator(byweekday=0)) #byweekday, lunes=0, martes=1 etc.
ax.xaxis.set_minor_formatter(dates.DateFormatter('%a')) #el by weekday afecta aca, solo se van a ver el dia que pedi

fig.autofmt_xdate() 
plt.tight_layout()
# %%
