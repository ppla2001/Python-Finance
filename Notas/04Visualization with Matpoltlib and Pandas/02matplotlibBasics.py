#%%
import matplotlib.pyplot as plt
import numpy as np

#%%
x = np.linspace(0,5,11)
y = x**2
#%%
x
#%%
y

#%%
#Functional Method 
plt.plot(x,y) #se le puede poner caracteristicas de matplotlib despues de las variables, ej: 'r-', me hace la linea roja 
plt.xlabel('X Label') #poner nombre al eje x
plt.ylabel('Y Label') #poner nombre al eje y
plt.title('Title') #poner titulo
plt.show() #cuando uso jupyter no hace falta que ponga esta parte del codigo
# %%
#Subplot, creating multiple plots at once
plt.subplot(1,2,1) #number of rows, number of colums, plot number reffering to
plt.plot(x,y,'r')

plt.subplot(1,2,2)
plt.plot(y,x,'b')

# %%
#Object Oriented API Method 
fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8]) #add_axes([left,bottom,widht,height])

axes.plot(x,y)
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Title')
# %%
fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3]) #cambiando los primeros dos numeros me cambia el segundo grafico de lugar, los segundos dos me dicen cuanto ocupa en termino de ancho y alto
axes1.plot(x,y)
axes1.set_title('Bigger Plot')

axes2.plot(y,x)
axes2.set_title('Smaller Plot')
# %%
#Subplot Object Oriented
fig,axes = plt.subplots(nrows=3,ncols=3) #nrows,ncols, te dice cuantos subplots hay
plt.tight_layout() #Hace q no se overlap la info de los graficos 
# %%
fig,axes = plt.subplots(nrows=1,ncols=2)

#Para plotear en todos los graficos
for current_axes in axes:
    current_axes.plot(x,y)
# %%
fig,axes = plt.subplots(nrows=1,ncols=2)

#Para plotear en algun grafico en especifico
axes[0].plot(x,y)
axes[0].set_title('First Plot')

axes[1].plot(y,x)
axes[1].set_title('Second Plot')
plt.tight_layout()

# %%
#Figure Size and DPI
fig = plt.figure(figsize=(3,2)) #figsize=() widht and height of figure in inches, dpi= dots per inch
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)
# %%
fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(8,2))
axes[0].plot(x,y)
axes[1].plot(y,x)
plt.tight_layout()
# %%
#Save a figure
fig.savefig('my_picture.png',dpi=200)
# %%
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,x**2,label='X Squared')
ax.plot(x,x**3,label='X Cubed')

ax.legend(loc='best') #checks if there is a label for each plot and matches labels with line, loc= es la location q quiero q esten las labels 
# %%
