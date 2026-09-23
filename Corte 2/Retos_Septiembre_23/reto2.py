import time

class RecursoComunitario:
    def __init__(self, codigoRecurso, nombreRecurso, vecesPrestado):
        self.codigoRecurso = codigoRecurso
        self.nombreRecurso = nombreRecurso
        self.vecesPrestado = vecesPrestado

    def __repr__(self):
        return f"[{self.codigoRecurso}] {self.nombreRecurso} (Prestamos: {self.vecesPrestado})"

def convertirAMinHeapPorPrestamos(arreglo, tamaño, indice, metricas):
    masPequeno = indice
    izquierdo = 2 * indice + 1
    derecho = 2 * indice + 2

    # Ordenamos de menor a mayor por 'vecesPrestado' (Min-Heap)
    if izquierdo < tamaño:
        metricas["comparaciones"] += 1
        if arreglo[izquierdo].vecesPrestado < arreglo[masPequeno].vecesPrestado:
            masPequeno = izquierdo

    if derecho < tamaño:
        metricas["comparaciones"] += 1
        if arreglo[derecho].vecesPrestado < arreglo[masPequeno].vecesPrestado:
            masPequeno = derecho

    if masPequeno != indice:
        arreglo[indice], arreglo[masPequeno] = arreglo[masPequeno], arreglo[indice]
        metricas["intercambios"] += 1
        convertirAMinHeapPorPrestamos(arreglo, tamaño, masPequeno, metricas)

def heapSortPorVecesPrestado(arreglo, metricas):
    tamaño = len(arreglo)

    # Construir el min-heap
    for indice in range(tamaño // 2 - 1, -1, -1):
        convertirAMinHeapPorPrestamos(arreglo, tamaño, indice, metricas)

    # Extraer elementos uno a uno
    for indice in range(tamaño - 1, 0, -1):
        arreglo[indice], arreglo[0] = arreglo[0], arreglo[indice]
        metricas["intercambios"] += 1
        convertirAMinHeapPorPrestamos(arreglo, indice, 0, metricas)
    
    return arreglo

# Datos de prueba del inventario de PrestaLab
inventarioRecursos = [
    RecursoComunitario("L-001", "Proyector Epson", 45),
    RecursoComunitario("L-002", "Taladro Percutor", 12),
    RecursoComunitario("L-003", "Kit Arduino Uno", 89),
    RecursoComunitario("L-004", "Multímetro Digital", 34),
    RecursoComunitario("L-005", "Cámara Réflex", 67),
    RecursoComunitario("L-006", "Set de Llaves Allen", 5)
]

metricasInventario = {"comparaciones": 0, "intercambios": 0}

print(" ANTES DE ORDENAR (Inventario PrestaLab) ")
for recurso in inventarioRecursos:
    print(recurso)

# Ejecución y medición del ordenamiento por veces prestado
tiempoInicio = time.time()
heapSortPorVecesPrestado(inventarioRecursos, metricasInventario)
tiempoFin = time.time()

print("\n DESPUÉS DE ORDENAR (Por Veces Prestado - Ascendente) ")
for recurso in inventarioRecursos:
    print(recurso)

print("\n MÉTRICAS DEL PROCESO ")
print(f"Comparaciones realizadas: {metricasInventario['comparaciones']}")
print(f"Intercambios realizados: {metricasInventario['intercambios']}")
print(f"Tiempo de ejecución: {tiempoFin - tiempoInicio:.6f} segundos")