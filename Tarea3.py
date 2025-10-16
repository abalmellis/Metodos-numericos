import itertools

def prob(evento, espacio):
    return (len(evento & espacio)/len(espacio))

def unir(color, numeros):
    return {color + numero for numero in numeros}

urna = unir('B', '12345678') | unir('A', '123456') | unir('R', '123456789')
espacio = set(itertools.permutations(urna, 6))

#¿Cuál es la probabilidad de que entre las tres primeras no haya ninguna roja?

def sin_rojas_en_las_tres_primeras(evento):
    return all(i[0] != 'R' for i in evento[:3])

sin_rojas = {e for e in espacio if sin_rojas_en_las_tres_primeras(e)}

print("Probabilidad de que entre las tres primeras no haya ninguna roja =", str(prob(sin_rojas, espacio)*100) + "%")

#¿Cuál es la probabilidad de sacar dos bolas de cada color?

def dos_de_cada_color(evento):
    colores = [i[0] for i in evento]   
    return (colores.count('B') == 2 and colores.count('A') == 2 and colores.count('R') == 2)

dos_color = {e for e in espacio if dos_de_cada_color(e)}

print("Probabilidad de sacar 2 bolas de cada color =", str(prob(dos_color, espacio)) + "%")

# Nota: 7.0
