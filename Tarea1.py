import h5py
import numpy as np
import matplotlib.pyplot as plt

with h5py.File('datasets.hd5', 'r') as file:
    x = np.array(file['x'])
    y = np.array(file['y'])
    e = np.array(file['e'])

plt.errorbar(x, y, yerr=e, label='Datos')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico con barras de error')
plt.legend()
plt.grid(True)
plt.show()

