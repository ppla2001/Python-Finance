import numpy as np
#vectors one dimensional arrays, straight list
#matrix two dimensional, can have only one line or column

#how to create a numpy array

my_list = [1,2,3]
np.array(my_list)

#matrix 
my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
np.array(my_matrix) #cambia dimensionality cuando returns 

#built in methods to build arrays 
list(range(0,5))
np.arange(0,5) #numpy version of range()
np.arange(1,11,2) #es lo mismo q range()
np.zeros(3) #create array or matrix of 0, 0. (floating point number), aca creamos un array
np.zeros((5,5)) #five by five matrix, index 0 es rows, index 1 es columns
np.ones(4) #lo mismo que zeros pero con ones 
#evenly spaced numbers in an interval
np.linspace(0,10,3) #quiero q empiece en 0, vaya a 10 y quiero que hayan solo 3 numeros, siempre tiene el mismo space, spacing out evenly
np.linspace(0,10,30)
np.eye(4) # square matrix lleno de 0 donde diagonalmente hay 1

#numpy random library
np.random.rand(1) #me da un numero entre 0 y 1
np.random.rand(5,5) #me da matrix de 5 por 5 de numeros entre 0 y 1 

np.random.randn(5) #standard normal distribution , centered at 0 with variance of 1

np.random.randint(1,100,10) #anywhere from 1 up to but not including 100, size of array

arr = np.arange(25)
ranarray = np.random.randint(0,50,10)
arr #esta en one dimension, lo puedo cambiar haciendo:
arr.reshape(5,5) #cambio a two dimensional con five by five, (5,4) me da error porq tiene q dar 25

arr.shape #(25,) dice es one dimensional array just has 25 in one axis, en cambio:
arr.reshape(5,5).shape #(5,5) es two dimensional

#key methods 
ranarray.max() #maximum number in array, si quiero el index del max number in array:
ranarray.argmax() #existe los dos mismos methods para min
