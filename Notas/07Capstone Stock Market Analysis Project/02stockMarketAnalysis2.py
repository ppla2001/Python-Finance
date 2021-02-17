#%%
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import pandas_datareader
import datetime
import pandas_datareader.data as web
#%%
start = datetime.datetime(2012,1,1)
end = datetime.datetime(2017,1,1)
#%%
tesla = web.DataReader('TSLA','yahoo',start,end)
# %%
ford = web.DataReader('F','yahoo',start,end)
general_m = web.DataReader('GM','yahoo',start,end)
# %%
tesla.head()
# %%
ford.head()
# %%
general_m.head()
# %%
