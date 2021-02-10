#Parte 1
import pandas as pd

banks = pd.read_csv('C:\\Users\\plape\\OneDrive\\Escritorio\\Python-Finance\\Python-Finance\\Notebooks\\03- General Pandas\\Pandas-Exercises\\banklist.csv')

#Parte 2
banks.head()

#Parte 3 
banks.columns

#Parte 4 
banks['ST'].nunique()

#Parte 5
banks['ST'].unique()

#Parte 6
banks.groupby('ST').count().sort_values('Bank Name').tail()

#Parte 7
banks['Acquiring Institution'].value_counts().iloc[:5]

#Parte 7
banks[banks['Acquiring Institution'] == 'State Bank of Texas']

#Parte 8 
banks[banks['ST']=='CA'].groupby('City').count().sort_values('Bank Name',ascending=False).head(1)

#Parte 9
banks['Bank Name'].apply(lambda name: 'Bank' not in name).value_counts()

#Parte 10
sum(banks['Bank Name'].apply(lambda name:name[0].upper() =='S'))

#Parte 11
sum(banks['CERT']>20000)

#Parte 12 
sum(banks['Bank Name'].apply(lambda name: len(name.split())==2))

#BONUS
sum(banks['Closing Date'].apply(lambda date: date[-2:]) == '08')