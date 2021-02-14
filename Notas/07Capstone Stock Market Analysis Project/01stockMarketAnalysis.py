#%%
#Parte 0 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
# %%
#Parte 1
#FIJARME EN SOLUTIONS COMO SE HACIA PARA SACAR INFO SIN TENER CSV
tesla = pd.read_csv('C:\\Users\\plape\\OneDrive\\Escritorio\\Python-Finance\\Python-Finance\\Notebooks\\07-Stock-Market-Analysis-Capstone-Project\\Tesla_Stock.csv',index_col='Date',parse_dates=True)

ford = pd.read_csv('C:\\Users\\plape\\OneDrive\\Escritorio\\Python-Finance\\Python-Finance\\Notebooks\\07-Stock-Market-Analysis-Capstone-Project\\Ford_Stock.csv',index_col='Date',parse_dates=True)

general_m = pd.read_csv('C:\\Users\\plape\\OneDrive\\Escritorio\\Python-Finance\\Python-Finance\\Notebooks\\07-Stock-Market-Analysis-Capstone-Project\\GM_Stock.csv',index_col='Date',parse_dates=True)
# %%
tesla.head()
# %%
ford.head()
# %%
general_m.head()
# %%
#Parte 2 
tesla['Open'].plot(label='Tesla',figsize=(16,6),title='Open Price')
ford['Open'].plot(label='Ford')
general_m['Open'].plot(label='General Motors')
plt.legend()
# %%
tesla['Volume'].plot(label='Tesla',figsize=(16,6),title='Volume')
ford['Volume'].plot(label='Ford')
general_m['Volume'].plot(label='General Motors')
plt.legend()
# %%
#Bonus
ford['Volume'].argmax()
# What happened:
# http://money.cnn.com/2013/12/18/news/companies/ford-profit/
# https://www.usatoday.com/story/money/cars/2013/12/18/ford-2014-profit-warning/4110015/
# https://media.ford.com/content/dam/fordmedia/North%20America/US/2014/01/28/4QFinancials.pdf
# %%
