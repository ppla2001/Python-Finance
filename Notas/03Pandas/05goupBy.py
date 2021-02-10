import numpy as np
import pandas as pd

data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)
df

#group by company
by_comp = df.groupby('Company')
by_comp.mean()
by_comp.sum()
by_comp.std() #standard deviation
by_comp.sum().loc['FB'] #sales sum of Facebook
#se puede hacer todo en one line 
df.groupby('Company').sum().loc['FB'] #lo mismo de arriba pero en una linea
df.groupby('Company').count() #lineas por cada Company
df.groupby('Company').max()
df.groupby('Company').min() #max y min deberian usarse solo con numeros no con strings 
df.groupby('Company').describe() #te devuelve un monton de info
df.groupby('Company').describe().transpose() #te cambia la forma en q lo ves (formato)
df.groupby('Company').describe().transpose()['FB'] #Single column (Facebook)