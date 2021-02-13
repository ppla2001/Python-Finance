#%%
import numpy as np
from numpy.random import randn
import seaborn as sns
import pandas as pd 

# %%
df1 = pd.read_csv('C:\\Users\\plape\\OneDrive\\Escritorio\\Python-Finance\\Python-Finance\\Notebooks\\04-Visualization-Matplotlib-Pandas\\04-02-Pandas Visualization\\df1',index_col=0)
df1.head()

# %%
df2 = pd.read_csv('C:\\Users\\plape\\OneDrive\\Escritorio\\Python-Finance\\Python-Finance\\Notebooks\\04-Visualization-Matplotlib-Pandas\\04-02-Pandas Visualization\\df2')
df2.head()

# %%
#Tipos de graficos
df1['A'].hist(bins=30)

# %%
df1['A'].plot(kind='hist',bins=30)

# %%
df1['A'].plot.hist()
# %%
df2.plot.area(alpha=0.4)
# %%
df2.plot.bar() #se le puede pedir bar(stacked=True)
# %%
df1['A'].plot.hist(bins=50)
# %%
df1.plot.line(figsize=(12,3),lw=1) #no me deja hacer el line especificando x=df1.index, y='B
# %%
df1.plot.scatter(x='A',y='B',c='C',cmap='coolwarm') #Estoy mostrando 3 partes de informacion, otra forma de hacerlo es:
# %%
df1.plot.scatter(x='A',y='B',s=df1['C']*30) #el *30 dice para q los puntos sean mas grandes porq si no son muy chicos
# %%
df2.plot.box()
# %%
df = pd.DataFrame(np.random.randn(1000,2),columns=['a','b'])
# %%
df.plot.hexbin(x='a',y='b',gridsize=25) #gridsize te agranda los puntos porq si no son muy chicos
# %%
df2['a'].plot.kde() #kernel density estimator plot, se puede hacer de todo el dataframe, no tiene q ser si o si de una column
# %%
df2['a'].plot.density() #tambien se puede hacer de todo el dataframe
# %%
df2.plot.density()
# %%
