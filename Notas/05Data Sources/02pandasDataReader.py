#%%
import pandas_datareader.data as web 
import datetime
# %%
start = datetime.datetime(2015,1,1)
end = datetime.datetime(2017,1,1)
facebook = web.DataReader('FB','yahoo',start,end) #Probe con google y no me deja, me da error
# %%
facebook.head() #el close value puede tomar stock split por el api
# %%
#option reader
#No me funciona, pero lo hice abajo
'''
from pandas_datareader.data import Options
fb_options = Options('FB','yahoo')
options_df = fb_options.get_options_data(expiry=fb_options.expiry_dates[0])
'''
# %%
from pandas_datareader.yahoo.options import Options as YahooOptions
underlying_symbol = 'FB'
options_obj = YahooOptions(underlying_symbol)
options_frame_live = options_obj.get_options_data()
# %%
options_frame_live
# %%
