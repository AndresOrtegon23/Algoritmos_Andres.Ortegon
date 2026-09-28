import time

# Parte A

# 2

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

print ("Parte A, punto 2: ")
print()
#Cuando quixk sort se comporta pesimo cuando el arreglo ya esta ordenado
datos = [10, 20, 30, 40, 50]

start_time = time.time()
result = quick_sort(datos)
end_time = time.time()

print(f"Datos con quick sort: {result}")
print(f"Tiempo de ejecución: {end_time - start_time} segundos")

# Parte B

def busquedaSecuencialContador(arreglo, x):
    comparaciones = 0
    for i in range(len(arreglo)):
        comparaciones += 1
        if arreglo[i] == x:
            return i, comparaciones
    return -1, comparaciones

def busquedaBinariaContador(arreglo, x):
    izq, der = 0, len(arreglo) - 1
    comparaciones = 0
    while izq <= der:
        medio = (izq + der) // 2
        comparaciones += 1
        if arreglo[medio] == x:
            return medio, comparaciones
        elif arreglo[medio] < x:
            izq = medio + 1
        else:
            der = medio - 1
    return -1, comparaciones


print("\nParte B: Comparación de búsquedas\n")
print()
arregloDatos = [10, 20, 30, 40, 50]

# Colección de prueba
arregloDatos = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
casosPrueba = [10, 60, 100, 25]

print(f"Colección: {arregloDatos}\n")
for valor in casosPrueba:
    idxSeq, compSeq = busquedaSecuencialContador(arregloDatos, valor)
    idxBin, compBin = busquedaBinariaContador(arregloDatos, valor)
    print(f"Buscando {valor}:")
    print(f"  - Secuencial -> Índice: {idxSeq}, Comparaciones: {compSeq}")
    print(f"  - Binaria    -> Índice: {idxBin}, Comparaciones: {compBin}\n")