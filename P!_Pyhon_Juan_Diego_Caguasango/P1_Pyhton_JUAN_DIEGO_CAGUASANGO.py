import numpy as np
# a) Cree el siguiente par de vectores:
a = np.array([3.1 , 1 , -0.5, -3.2, 6 ])
b= np.array([ 1, 3 , 2.2 , 5.1, 1 ])
print(a,b)

#Implemente la multiplicación escalar de a.b
#ara poder realizar esto se deber crear los array con la libreria de numpy
multiplicaion = np.multiply(a,b)
print("Multiplicaion entre a y b",multiplicaion)