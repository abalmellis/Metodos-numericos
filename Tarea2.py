import numpy as np
import matplotlib.pyplot as plt

# Parámetros
N = 20
f = lambda x: x**2 - 2.0
true = np.sqrt(2)


a, b = 1.0, 2.0
err_bis = np.empty(N)
x_bis_hist = []

for k in range(N):
    c = 0.5*(a + b)
    x_bis_hist.append(c)
    err_bis[k] = abs(c - true)
    if f(a)*f(c) <= 0:
        b = c
    else:
        a = c

x_newt = 2.0
err_newt = np.empty(N)
x_newt_hist = [x_newt]

for k in range(N):
    x_newt = 0.5 * (x_newt + 2.0/x_newt)
    x_newt_hist.append(x_newt)
    err_newt[k] = abs(x_newt - true)


plt.semilogy(range(N), err_bis, 'o-', label="Bisección")
plt.semilogy(range(N), err_newt, 's-', label="Newton")
plt.xlabel("Número de iteraciones")
plt.ylabel("Error absoluto")
plt.title("Bisección vs Newton")
plt.legend()
plt.grid()
plt.show()

#

# Nota: 6.0
# Faltó interpretar y comentar como se pedía
