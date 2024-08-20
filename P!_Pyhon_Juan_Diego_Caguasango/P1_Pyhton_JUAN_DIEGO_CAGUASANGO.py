import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# a) Cree el siguiente par de vectores:
a = np.array([3.1 , 1 , -0.5, -3.2, 6 ])
b= np.array([ 1, 3 , 2.2 , 5.1, 1 ])
print("vestor a: ",a)
print("vestor b: ",b)

#b) Implemente la multiplicación escalar de a.b
#Para multiplicar dos vectores, ambos deben tener la misma longitud y contener elementos numéricos. 
# Usar una librería como NumPy facilita estas operaciones.

producto_punto = np.dot(a,b)
print("Producto_punto entre a y b: ",producto_punto)

#c) Implemente la multiplicación punto a punto de a.b
multiplicacion = np.multiply(a,b)
print("multiplicaion punto a punto: ",multiplicacion)

#d construya la matriz 
A = np.array([[2,-1,-3],[4,1.5,-2.5],[7.3,-0.9,0.2]])
print("Matriz A: \n",A)

# e) transpuesta 
transp = A.T
print("Transpuesta: \n",transp)

#f) 
# 1. numpy.ones
ones = np.ones((5))
print("Array lleno de unos: ", ones)

# 2. numpy.round
array = np.array([1.234, 5.678, 9.101])
redondeado = np.round(array, 1)
print("Array redondeado a 1 decimal: ",redondeado)

# 3. numpy.ceil
array_1 = np.array([1.2, 2.5, 3.7])
ceiled = np.ceil(array_1)
print("Array redondeado hacia arriba: ",ceiled)

# 4. numpy.floor
array_2 = np.array([1.8, 2.5, 3.7])
floored = np.floor(array_2)
print("Array redondeado hacia abajo: ",floored)

# g)Acceda al valor de la primera fila,
#  tercera columna de la matriz A, imprímalo en consola
valorA = A[0,2]
print("Valor A(3,2): ",valorA)

# h)
print("segunda fila de la matriz A: ",A[1])

#i) 
print("dimensiones de A: ",A.ndim)

# j) 
rango_1 = np.arange(0,100)
seno = np.sin(np.pi*rango_1*0.12)
cos = np.cos(np.pi*2*0.03*rango_1)

fig, ax = plt.figure(1), plt.axes()

ax.plot(rango_1, seno, label='sin⁡(π*0.12n)', color='blue', linestyle='-', linewidth=2)
ax.plot(rango_1, cos, label='cos⁡(2π*0.03n)', color='green', linestyle='-', linewidth=1)
ax.set_title('Función sin⁡(π*0.12n) y cos⁡(2π*0.03n)')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid()
ax.legend()


fig, ax = plt.figure(2), plt.axes()

ax.plot(rango_1, seno, label='sin⁡(π*0.12n)', color='blue', linestyle='-', linewidth=2)
ax.plot(rango_1, cos, label='cos⁡(2π*0.03n)', color='green', linestyle='-', linewidth=1)
ax.set_title('Función sin⁡(π*0.12n) y cos⁡(2π*0.03n)')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid()
ax.legend()
plt.show()


