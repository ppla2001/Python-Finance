#%% 
import quandl
# %%
mydata = quandl.get('EIA/PET_RWTC_D') #se puede usar como argumento returns='numpy', a lo que despues puedo llamar mydata y me devuelve arrays con la info
# %%
import matplotlib.pyplot as plt
# %%
mydata.plot()
# %%
#Otro ejemplo
real_estate = quandl.get('ZILLOW/C9_ZRIFAH')
# %%
real_estate
# %%
#para agarrar el codigo sin ir a la pagina 
data = quandl.get('WIKI/AAPL')
# %%
data.head()
# %%
#Para pedir menos informacion
data = quandl.get('WIKI/AAPL.1')
data
# %%
