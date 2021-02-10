import numpy as np
import pandas as pd 

#open and read cv files 
df = pd.read_csv('C:\\Users\\plape\\OneDrive\\Escritorio\\Python-Finance\\Python-Finance\\Notebooks\\03- General Pandas\\example')
df
df.to_csv('My_output')
pd.read_csv('My_output') #fijarme lo q hace, me pone un index como unnamed, para arreglarlo hay q hacer:
df.to_csv('My_output',index=False) #hay q fijarse para cada caso en particular
pd.read_csv('My_output')

#reading and writing from excel files, solo puede import data
pd.read_excel('C:\\Users\\plape\\OneDrive\\Escritorio\\Python-Finance\\Python-Finance\\Notebooks\\03- General Pandas\\Excel_Sample.xlsx',sheet_name='Sheet1')
df.to_excel('C:\\Users\\plape\\OneDrive\\Escritorio\\Python-Finance\\Python-Finance\\Notebooks\\03- General Pandas\\Excel_Sample2.xlsx',sheet_name='NewSheet') #me creo nueva file de excel justo abajo de donde esta el Excel_Sample.xlsx (Notebook)

#HTML
data = pd.read_html('https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/')
data[0]

#SQL
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:')
df.to_sql('my_table',engine)
sqldf = pd.read_sql('my_table',con=engine)
sqldf