import time

def particionHoare(arreglo, bajo, alto, metricas):
    pivote = arreglo[bajo]
    indiceIzquierda = bajo - 1
    indiceDerecha = alto + 1
    
    while True:
        while True:
            indiceIzquierda += 1
            metricas["comparaciones"] += 1
            if arreglo[indiceIzquierda] >= pivote:
                break
                
        while True:
            indiceDerecha -= 1
            metricas["comparaciones"] += 1
            if arreglo[indiceDerecha] <= pivote:
                break
                
        if indiceIzquierda >= indiceDerecha:
            return indiceDerecha
            
        arreglo[indiceIzquierda], arreglo[indiceDerecha] = arreglo[indiceDerecha], arreglo[indiceIzquierda]
        metricas["intercambios"] += 1

def quickSortEnLugar(arreglo, bajo, alto, metricas):
    if bajo < alto:
        indicePivote = particionHoare(arreglo, bajo, alto, metricas)
        quickSortEnLugar(arreglo, bajo, indicePivote, metricas)
        quickSortEnLugar(arreglo, indicePivote + 1, alto, metricas)
    return arreglo

# Ejemplo y ejecución
metricasQuick = {"comparaciones": 0, "intercambios": 0}
datosQuick = [64, 34, 25, 12, 22, 11, 90, 45, 33]

tiempoInicio = time.time()
quickSortEnLugar(datosQuick, 0, len(datosQuick) - 1, metricasQuick)
tiempoFin = time.time()

print(" Quicksort In-Place ")
print("Arreglo original:", [64, 34, 25, 12, 22, 11, 90, 45, 33])
print("Arreglo ordenado:", datosQuick)
print(f"Comparaciones: {metricasQuick['comparaciones']}")
print(f"Intercambios: {metricasQuick['intercambios']}")
print(f"Tiempo: {tiempoFin - tiempoInicio:.6f} segundos\n")