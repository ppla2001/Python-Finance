import numpy as np
import pandas as pd 

df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
df.head()

#finding unique values in dataframe
df['col2'].unique() #array of values 
df['col2'].nunique() #number of unique values 
df['col2'].value_counts() #table of how many times a value occurred 

#applied method 
def times2(x):
    return x*2

df['col1'].apply(times2) 
df['col3'].apply(len) #te deja llamar funciones para los values adentro de la tabla 

df['col2'].apply(lambda x: x*2) #lo mismo q times2 pero mas rapido

#removing colums 
df.drop('col1',axis=1) #inplace=True para q se borre permanente

df.columns #lista de column names 
df.index

#sorting and ordering dataframe 
df.sort_values(by='col2') 

#find null values 
df.isnull()

#pivot table 
data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)
df
df.pivot_table(values='D',index=['A','B'],columns='C') 