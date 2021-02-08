import numpy as np
import pandas as pd

d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}
df = pd.DataFrame(d)
df

df.dropna() #te borra todas las row q tenga por lo menos 1 missing value y te deja las rows q estan completas, si lo quiero hacer en las columns:
df.dropna(axis=1)
df.dropna(thresh=2) #especificas a partir de cuantos NaN queres q te borre las rows o columns (depende de lo q especifiques en axis)

#replace missing values 
df.fillna(value='FILL') #remplazas NaN con un valor 
#muchas veces lo q se hace es remplazar NaN con el mean de la column, ej:
df['A'].fillna(value=df['A'].mean())