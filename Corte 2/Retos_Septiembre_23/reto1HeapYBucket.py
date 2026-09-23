import time

def convertirAMinHeap(arreglo, tamanio, indice, metricas):
    masPequeno = indice
    izquierdo = 2 * indice + 1
    derecho = 2 * indice + 2

    if izquierdo < tamanio:
        metricas["comparaciones"] += 1
        if arreglo[izquierdo] < arreglo[masPequeno]:
            masPequeno = izquierdo

    if derecho < tamanio:
        metricas["comparaciones"] += 1
        if arreglo[derecho] < arreglo[masPequeno]:
            masPequeno = derecho

    if masPequeno != indice:
        arreglo[indice], arreglo[masPequeno] = arreglo[masPequeno], arreglo[indice]
        metricas["intercambios"] += 1
        convertirAMinHeap(arreglo, tamanio, masPequeno, metricas)

def heapSortMinimo(arreglo, metricas):
    tamanio = len(arreglo)

    for indice in range(tamanio // 2 - 1, -1, -1):
        convertirAMinHeap(arreglo, tamanio, indice, metricas)

    for indice in range(tamanio - 1, 0, -1):
        arreglo[indice], arreglo[0] = arreglo[0], arreglo[indice]
        metricas["intercambios"] += 1
        convertirAMinHeap(arreglo, indice, 0, metricas)
    
    return arreglo

# Ejemplo y ejecución
metricasHeap = {"comparaciones": 0, "intercambios": 0}
datosHeap = [64, 25, 12, 22, 11, 90, 45, 33]

tiempoInicio = time.time()
heapSortMinimo(datosHeap, metricasHeap)
tiempoFin = time.time()

print(" Heapsort Mínimo ")
print("Arreglo ordenado:", datosHeap)
print(f"Comparaciones: {metricasHeap['comparaciones']}")
print(f"Intercambios: {metricasHeap['intercambios']}")
print(f"Tiempo: {tiempoFin - tiempoInicio:.6f} segundos\n")