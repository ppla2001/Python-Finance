import numpy as np
arr = np.arange(0,11)
arr[8] #igual q las listas 
arr[1:5] #desde 1 a 5 sin incluirlo
arr[:5] #0 a 4
arr[3:] #de 3 al final

#broadcasting 
arr[0:5] = 100
arr #cambie los primeros 4 index positions a 100, no se puede hacer esto con listas normales, el cambio es permanente 

arr = np.arange(0,11)

slice_of_array = arr[:6]
slice_of_array[:] = 99 #el [:] significa que agarra todo el array 
slice_of_array
arr #todo lo de arriba me cambio el array original
arr_copy = arr.copy() #necesito hacer esto para que no me cambie el array original
arr_copy
arr_copy[:] = 200
arr_copy #me cambio todo a 200
arr #me dejo el array original

#indexing matrix 
# matrix[row,col]
# matrix[row][col]
mat = np.array([[5,10,15],[20,25,30],[35,40,45]])
mat
#index entire row
mat[0]
mat[2]
#index individual value
mat[1][1] #me da el 25
mat[1,1] #tmb me da 25

#slicing
#quiero el square 10,15 / 25,30
mat[:2,1:] #quiero que empieze de row 0 y vaya hasta la 2 sin incluirla ; quiero q empieze de column 1 y vaya al final, eso me da el cuadrado 10,15 / 25,30

#conditional selection
''' fundamental entender '''
arr = np.arange(1,11)
arr
#agarrar todos los numeros mas grandes q 4
arr > 4 #me devuelve boolean
bool_arr = arr > 4 
arr[bool_arr]
#se puede hacer todo en un step
arr[arr > 4]