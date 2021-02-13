#%%
import pandas as pd
import matplotlib.pyplot as plt
df3 = pd.read_csv('C:\\Users\\plape\\OneDrive\\Escritorio\\Python-Finance\\Python-Finance\\Notebooks\\04-Visualization-Matplotlib-Pandas\\04-02-Pandas Visualization\\df3')

# %%
df3.info()
# %%
df3.head()
# %%
df3.plot.scatter(x='a',y='b',s=50,figsize=(12,3))
# %%
df3['a'].plot.hist()
# %%
plt.style.use('ggplot')
# %%
df3['a'].plot.hist(alpha=0.5,bins=25)
# %%
df3[['a','b']].plot.box()
# %%
df3['d'].plot.kde()
# %%
df3['d'].plot.kde(lw=2,ls='--')
# %%
df3.loc[0:30].plot.area(alpha=0.5)
# %%
df3.loc[0:30].plot.area(alpha=0.5)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
# %%
