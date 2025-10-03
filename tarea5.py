import numpy as np

distribucion = [12.53,1.42,4.68,5.86,13.68,0.69,1.01,0.70,6.25,0.44,0.02,4.97,3.15,6.71,0.31,8.68,2.51,0.88,6.87,7.98,4.63,3.93,0.90,0.01,0.22,0.90,0.52]

p= np.array(distribucion)/100 #porcentaje a frecuencias

H=0
for p_i in p:
    H += -p_i*np.log(p_i)

print("Entropia Shannon :", H)

#Como el poema repite palabras y sufijos constantemente, a diferencia del flujo de letras aleatorias del alfabeto
#el poema tiene menor entropía por lo que aportan menos información por bit por letra que la calculada anteriormente
#haciendo posible una comprensión mas efectiva 