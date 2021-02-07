import numpy as np
import pandas as pd

labels = ['a','b','c']
my_list = [10,20,30]
arr = np.array([10,20,30])
d = {'a':10, 'b':20, 'c':100}

pd.Series(my_list,index=labels) #es como hacer una tabla donde el nombre de lo q paso es el index(parte izquierda) y datos son my_list
pd.Series(arr,labels) #es exactamente lo mismo q el de arriba porq los datos q paso son lo mismo
pd.Series(d) #es lo mismo q hacer lo de arriba pero es mas rapido porq cada value ya tiene su key
pd.Series(data=labels) #ahora hice algo donde index son numeros y data son strings, cambia dtype 
pd.Series([sum,print,len]) #pandas es tan flexible q se puede pasar funciones tambien

#ver como funciona index 
ser1 = pd.Series([1,2,3,4],index=['USA','CHINA','FRANCE','ARG'])
ser1

ser2 = pd.Series([1,2,3,4],index=['USA','GERMANY','COLOMBIA','ARG'])
ser2

ser1['USA']
ser2['COLOMBIA'] #si intentas de index algo q no esta en la tabla te da error ej, ser2['JAPAN']

ser1 + ser2 #hace una suma donde los valores e index matched, en los unicos q matchearon en este caso son USA y ARG