import numpy as np
import pandas as pd 
from numpy.random import randn
np.random.seed(101) #para q te de los mismos random numbers 

df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z']) #me hace un dataframe (parecido a excel)
df

#selecting columns
df['W'] #para llamar una column en un DataFrame, lo q me devuelve es una series
df.W #Esto es lo mismo q lo de arriba, recomiendan hacer el de arriba 
df[['W','Z']] #multiple colums, me devuelve dataframe

#create new column
df['new'] = df['W'] + df['Y']
df

#remove column
df.drop('new',axis=1) #no me lo borra permanentemente, si llamo df de nuevo, la column new va a seguir apareciendo
df
#para q me lo borre permanentemente hay q hacer lo siguiente:
df.drop('new',axis=1,inplace=True)
df

#remove row
df.drop('E',axis=0) #el axis=0 no hace falta ponerlo porq es el valor default, esto de nuevo no me lo borra permanente
df

#selecting rows
df.loc['A'] #devuelve Series
df.iloc[2] #las dos formas devuelven las rows 

#selecting subsets of rows and columns 
df.loc['B','Y']
df.loc[['A','B'],['W','Y']]

#Conditional Selection
df > 0 #boolean values 
booldf = df > 0
df[booldf] # me da la tabla con los values 
df[df>0] #lo mismo q arriba pero mas rapido
df['W']>0 #boolean values 
df[df['W']>0] #me da solo las columns de W donde esto sea True, osea q se borra la 'C'
df[df['Z']<0] #me devuelve toda la row 

resultdf = df[df['W']>0]
resultdf['X'] #me tiene q devolver solo 'A' 'B' 'D' 'E' 
df[df['W']>0]['X'] #lo mismo q arriba solo q mas rapido
df[df['W']>0][['Y','X']] #lo mismo q arriba pero con mas colums 

#multiple conditions 
df[(df['W']>0) & (df['Y']>1)] #hay q usar los simbolos q representan and/or etc. and = &, or = |, etc.

#reseting index or seting to somthing else 
df.reset_index() #reset index to numerical, no es inplace a menos q lo especifique adentro de ()
newind = 'CA NY WY OR CO'.split() #'CA NY WY OR CO'.split() forma mas rapida de hacer una list en vez de tener q separar todo con ,
df['States'] = newind
df
df.set_index('States') #no es inplace 

#INDEX
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

df = pd.DataFrame(randn(6,2),hier_index,['A','B'])
df #hice un framework con multilevels of index, tambien llamado como index hierarchy
df.loc['G1'] #me da sub dataframe
df.loc['G1'].loc[1] #llamas de afuera y vas llamando para adentro
df.index.names #no hay nombres de index 
df.index.names = ['Groups','Num']
df #ahora los index tienen nombres 
df.loc['G2'].loc[2]['B'] #agarre un value 

#cross section
df.xs(1,level='Num') #se usa con multilevel index, lo q hice fue un cross section, agarre info de los dos niveles G1 y G2, agarre de num=1 los datos de G1 y G2
