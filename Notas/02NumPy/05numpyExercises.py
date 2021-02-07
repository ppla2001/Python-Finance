#Parte 1
import numpy as np

#Parte 2
np.zeros(10)

#Parte 3
np.ones(10)

#Parte 4
np.ones(10) * 5

#Parte 5
np.arange(10,51)

#Parte 6
np.arange(10,51,2)

#Parte 7
np.arange(9).reshape(3,3)

#Parte 8 
np.eye(3)

#Parte 9
np.random.rand(1)

#Parte 10
np.random.randn(25)

#Parte 11
np.arange(1,101).reshape(10,10) / 100

#Parte 12
np.linspace(0,1,20)

#Parte 13
matrix = np.arange(1,26).reshape(5,5)
matrix

#Parte 14
matrix[2:,1:]

#Parte 15
matrix[3,4]

#Parte 16
matrix[:3,1:2]

#Parte 17
matrix[4,:]

#Parte 18
matrix[3:5,:]

#Parte 19
matrix.sum()

#Parte 20
matrix.std()

#Parte 21
matrix.sum(axis=0)

#BONUS QUESTION
np.random.seed(101)