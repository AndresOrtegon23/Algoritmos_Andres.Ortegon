import time

def quickSortMalPivote(arreglo):
    if len(arreglo) <= 1:
        return arreglo
    pivote = arreglo[0]  # Pivote fijo al inicio (genera el peor caso si está ordenada)
    izquierda = [x for x in arreglo[1:] if x < pivote]
    derecha = [x for x in arreglo[1:] if x >= pivote]
    return quickSortMalPivote(izquierda) + [pivote] + quickSortMalPivote(derecha)

# Ejemplo y medición con el peor caso (lista ordenada)
tamañoDatos = 400
listaOrdenada = list(range(tamañoDatos))
print(f"Ejecutando Quicksort (peor caso) con lista ordenada de {tamañoDatos} elementos...")

tiempoInicio = time.time()
try:
    quickSortMalPivote(listaOrdenada)
    tiempoFin = time.time()
    print(f"Tiempo de ejecución (O(N^2)): {tiempoFin - tiempoInicio:.6f} segundos\n")
except RecursionError:
    print("¡RecursionError! La lista ordenada desbordó la pila de llamadas.\n")