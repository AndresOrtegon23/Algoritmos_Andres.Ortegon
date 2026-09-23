import time

# --- Merge Sort ---
def mezclar(arreglo, izquierda, medio, derecha, metricas):
    mitadIzquierda = arreglo[izquierda:medio + 1]
    mitadDerecha = arreglo[medio + 1:derecha + 1]
    
    i = j = 0
    k = izquierda
    
    while i < len(mitadIzquierda) and j < len(mitadDerecha):
        metricas["comparaciones"] += 1
        if mitadIzquierda[i] <= mitadDerecha[j]:
            arreglo[k] = mitadIzquierda[i]
            i += 1
        else:
            arreglo[k] = mitadDerecha[j]
            j += 1
        metricas["intercambios"] += 1 # Contabiliza la reasignación/escritura
        k += 1
        
    while i < len(mitadIzquierda):
        arreglo[k] = mitadIzquierda[i]
        i += 1
        k += 1
        
    while j < len(mitadDerecha):
        arreglo[k] = mitadDerecha[j]
        j += 1
        k += 1

def mergeSort(arreglo, izquierda, derecha, metricas):
    if izquierda < derecha:
        medio = (izquierda + derecha) // 2
        mergeSort(arreglo, izquierda, medio, metricas)
        mergeSort(arreglo, medio + 1, derecha, metricas)
        mezclar(arreglo, izquierda, medio, derecha, metricas)


# --- Quicksort (In-place con dos índices) ---
def particionar(arreglo, bajo, alto, metricas):
    pivote = arreglo[alto]
    i = bajo - 1
    
    for j in range(bajo, alto):
        metricas["comparaciones"] += 1
        if arreglo[j] < pivote:
            i += 1
            arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
            metricas["intercambios"] += 1
            
    arreglo[i + 1], arreglo[alto] = arreglo[alto], arreglo[i + 1]
    metricas["intercambios"] += 1
    return i + 1

def quickSort(arreglo, bajo, alto, metricas):
    if bajo < alto:
        indicePivote = particionar(arreglo, bajo, alto, metricas)
        quickSort(arreglo, bajo, indicePivote - 1, metricas)
        quickSort(arreglo, indicePivote + 1, alto, metricas)


# --- Heapsort (Máximos) ---
def convertirMaxHeap(arreglo, n, i, metricas):
    mayor = i
    izquierdo = 2 * i + 1
    derecho = 2 * i + 2

    if izquierdo < n:
        metricas["comparaciones"] += 1
        if arreglo[izquierdo] > arreglo[mayor]:
            mayor = izquierdo

    if derecho < n:
        metricas["comparaciones"] += 1
        if arreglo[derecho] > arreglo[mayor]:
            mayor = derecho

    if mayor != i:
        arreglo[i], arreglo[mayor] = arreglo[mayor], arreglo[i]
        metricas["intercambios"] += 1
        convertirMaxHeap(arreglo, n, mayor, metricas)

def heapSort(arreglo, metricas):
    n = len(arreglo)
    for i in range(n // 2 - 1, -1, -1):
        convertirMaxHeap(arreglo, n, i, metricas)

    for i in range(n - 1, 0, -1):
        arreglo[i], arreglo[0] = arreglo[0], arreglo[i]
        metricas["intercambios"] += 1
        convertirMaxHeap(arreglo, i, 0, metricas)


# --- Bucket Sort ---
def bucketSort(arreglo, metricas):
    if len(arreglo) == 0:
        return arreglo

    valorMinimo = min(arreglo)
    valorMaximo = max(arreglo)
    
    if valorMinimo == valorMaximo:
        return arreglo

    numeroCubetas = len(arreglo)
    rangoCubeta = (valorMaximo - valorMinimo) / numeroCubetas
    cubetas = [[] for _ in range(numeroCubetas)]

    for num in arreglo:
        indice = int((num - valorMinimo) / rangoCubeta)
        if indice == numeroCubetas:
            indice -= 1
        cubetas[indice].append(num)

    arreglo.clear()
    for cubeta in cubetas:
        # Usamos ordenamiento por inserción interno para contar métricas en cada cubeta
        for i in range(1, len(cubeta)):
            clave = cubeta[i]
            j = i - 1
            while j >= 0:
                metricas["comparaciones"] += 1
                if cubeta[j] > clave:
                    cubeta[j + 1] = cubeta[j]
                    metricas["intercambios"] += 1
                    j -= 1
                else:
                    break
            cubeta[j + 1] = clave
        arreglo.extend(cubeta)


# --- PRUEBAS Y RESULTADOS EN PYTHON ---
datosPruebaBase = [64, 25, 12, 22, 11, 90, 45, 33]

print(" PRUEBAS DE ORDENAMIENTO EN PYTHON ")

print()

print(" Datos de prueba base:", datosPruebaBase)

print()
# 1. Merge Sort
datos = list(datosPruebaBase)
metricas = {"comparaciones": 0, "intercambios": 0}
inicio = time.time()
mergeSort(datos, 0, len(datos) - 1, metricas)
tiempo = time.time() - inicio
print(f"Merge Sort -> Ordenado: {datos} | Comp: {metricas['comparaciones']} | Intercambios: {metricas['intercambios']} | Tiempo: {tiempo:.6f}s")

# 2. Quick Sort
datos = list(datosPruebaBase)
metricas = {"comparaciones": 0, "intercambios": 0}
inicio = time.time()
quickSort(datos, 0, len(datos) - 1, metricas)
tiempo = time.time() - inicio
print(f"Quick Sort -> Ordenado: {datos} | Comp: {metricas['comparaciones']} | Intercambios: {metricas['intercambios']} | Tiempo: {tiempo:.6f}s")

# 3. Heap Sort
datos = list(datosPruebaBase)
metricas = {"comparaciones": 0, "intercambios": 0}
inicio = time.time()
heapSort(datos, metricas)
tiempo = time.time() - inicio
print(f"Heap Sort  -> Ordenado: {datos} | Comp: {metricas['comparaciones']} | Intercambios: {metricas['intercambios']} | Tiempo: {tiempo:.6f}s")

# 4. Bucket Sort
datos = list(datosPruebaBase)
metricas = {"comparaciones": 0, "intercambios": 0}
inicio = time.time()
bucketSort(datos, metricas)
tiempo = time.time() - inicio
print(f"Bucket Sort-> Ordenado: {datos} | Comp: {metricas['comparaciones']} | Intercambios: {metricas['intercambios']} | Tiempo: {tiempo:.6f}s")