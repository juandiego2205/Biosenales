import matplotlib as plt
def impseq(n0, n1, n2):
# Genera x(n) = delta(n-n0); n1 <= n <= n2
# ----------------------------------------------
 n = np.arange(n1,n2+1) # Se crea el vector de muestras
 x = (n-n0) == 0
 return [x,n]
plt.stem()