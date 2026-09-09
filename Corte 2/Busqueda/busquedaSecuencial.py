from typing import Sequence

def busqueda_secuencial(a: Sequence[int], x: int) -> int:
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

def busqueda_secuencual_pythonica(a, x):
    for i, v in enumerate(a):
        if v == x:
            return i
    return -1

def secuencial_rec (a, x, i=0):
    if i >= len(a):
        return -1
    if a[i] == x:
        return i
    return secuencial_rec(a, x, i + 1)

Vector = [5, 7, 3, 6, 90, 3, 9]


print("Busqueda secuencial")
print ("Buscando el valor: 5")
print ("Numero de pasos: ", busqueda_secuencial(Vector, 5))

print (f"Numero de busquedas: ")
print (f"del Vector: {Vector}")
print(f"Índice del valor encontrado: {busqueda_secuencial(Vector, 5)}")