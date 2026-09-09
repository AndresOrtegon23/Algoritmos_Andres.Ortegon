def binaria (v, x):
    izq, der = 0, len(v) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if v[medio] == x:
            return medio
        elif v[medio] < x:
            izq = medio + 1
        else:
            der = medio - 1
    return -1

Vector = [5, 7, 3, 6, 90, 3, 9]

print("Busqueda binaria")
print ("Buscando el valor: 5")
print ("Numero de pasos: ", binaria(Vector, 5))
print (f"del Vector: {Vector}")
print(f"Índice del valor encontrado: {binaria(Vector, 5)}")