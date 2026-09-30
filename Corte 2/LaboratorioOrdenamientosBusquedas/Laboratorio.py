import time
import random

# PARTE A: Demostración del peor caso de Quicksort
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
# Evaluando con datos ordenados (peor escenario de partición)
datos = [10, 20, 30, 40, 50]

start_time = time.time()
result = quick_sort(datos)
end_time = time.time()

print(f"Datos con quick sort: {result}")
print(f"Tiempo de ejecución: {end_time - start_time} segundos")

# PARTE B: Búsqueda Secuencial y Binaria con contadores
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
cedulas = [
    100001, 100002, 100003, 100004, 100005,
    100006, 100007, 100008, 100009, 100010,
    200011, 200012, 200013, 200014, 200015,
    200016, 200017, 200018, 200019, 200020,
    300021, 300022, 300023, 300024, 300025,
    400026, 400027, 400028, 400029, 400030]
casosPrueba = [100001, 200016, 400030, 25]

print(f"Colección: {cedulas}\n")
for valor in casosPrueba:
    idxSeq, compSeq = busquedaSecuencialContador(cedulas, valor)
    idxBin, compBin = busquedaBinariaContador(cedulas, valor)
    print(f"Buscando {valor}:")
    print(f"  - Secuencial -> Índice: {idxSeq}, Comparaciones: {compSeq}")
    print(f"  - Binaria    -> Índice: {idxBin}, Comparaciones: {compBin}\n")


# PARTE C: Los tres ordenamientos básicos con contadores
print("Parte C")
print()
cedulasDesordenadas = list(reversed(cedulas))

# 1. Bubble Sort: Compara elementos vecinos y los intercambia si están desordenados
def bubbleSortContador(arr):
    comparaciones = 0
    intercambios = 0
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparaciones += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambios += 1
                swapped = True
        if not swapped:
            break
    return comparaciones, intercambios

# 2. Selection Sort: Busca el elemento menor y lo ubica al inicio iterativamente
def selectionSortContador(arr):
    comparaciones = 0
    intercambios = 0
    n = len(arr)
    for i in range(n):
        minIdx = i
        for j in range(i + 1, n):
            comparaciones += 1
            if arr[j] < arr[minIdx]:
                minIdx = j
        if minIdx != i:
            arr[i], arr[minIdx] = arr[minIdx], arr[i]
            intercambios += 1
    return comparaciones, intercambios

# 3. Insertion Sort: Inserta cada elemento en su posición ordenada correspondiente
def insertionSortContador(arr):
    comparaciones = 0
    intercambios = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparaciones += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                intercambios += 1
                j -= 1
            else:
                break
        arr[j + 1] = key
    return comparaciones, intercambios

# Ejecución y reporte para datos ordenados y desordenados
algoritmos = [
    ("Bubble Sort", bubbleSortContador),
    ("Selection Sort", selectionSortContador),
    ("Insertion Sort", insertionSortContador)
]

print()
print(" RESULTADOS CON DATOS YA ORDENADOS")
print()
# Iteramos sobre cada algoritmo básico para evaluar el escenario óptimo (datos ya ordenados)
for nombre, funcion in algoritmos:
    copiaDatos = cedulas.copy()     # Copiamos la lista para proteger los datos originales
    comp, inter = funcion(copiaDatos)       # Ejecutamos la función y obtenemos contadores de métricas
    print(f"- {nombre}:")
    print(f"  * Comparaciones: {comp}")
    print(f"  * Intercambios:  {inter}\n")

print()
print(" RESULTADOS CON DATOS DESORDENADOS (INVERTIDOS)")
print()

# Repetimos la evaluación probando ahora el peor escenario (datos invertidos)
for nombre, funcion in algoritmos:
    copiaDatos = cedulasDesordenadas.copy()     # Copiamos la lista invertida
    comp, inter = funcion(copiaDatos)           # Ejecutamos la función y obtenemos contadores
    print(f"- {nombre}:")
    print(f"  * Comparaciones: {comp}")
    print(f"  * Intercambios:  {inter}\n")


# PARTE D: Ordenamiento Avanzado (Merge Sort) y Medición de Tiempos
print("Parte D")
print()

# Merge Sort
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        leftHalf = arr[:mid]
        rightHalf = arr[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i = j = k = 0

        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                arr[k] = leftHalf[i]
                i += 1
            else:
                arr[k] = rightHalf[j]
                j += 1
            k += 1

        while i < len(leftHalf):
            arr[k] = leftHalf[i]
            i += 1
            k += 1

        while j < len(rightHalf):
            arr[k] = rightHalf[j]
            j += 1
            k += 1
    return arr

# Algoritmo básico de referencia para el contraste de rendimiento
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Medición comparativa de tiempos para tres tamaños distintos (N = 1000, 5000, 10000)
tamanosEntrada = [1000, 5000, 10000]

print(f"{'Tamaño (N)':<12} | {'Insertion Sort (ms)':<22} | {'Merge Sort (ms)'}")
print()

for n in tamanosEntrada:
    datosOriginales = [random.randint(1, 100000) for _ in range(n)]
    
    # Medición Insertion Sort
    datosInsertion = datosOriginales.copy()
    inicioIns = time.perf_counter()
    insertionSort(datosInsertion)
    tiempoInsertion = (time.perf_counter() - inicioIns) * 1000
    
    # Medición Merge Sort
    datosMerge = datosOriginales.copy()
    inicioMerge = time.perf_counter()
    mergeSort(datosMerge)
    tiempoMerge = (time.perf_counter() - inicioMerge) * 1000
    
    print(f"{n:<12} | {tiempoInsertion:<22.4f} | {tiempoMerge:.4f}")