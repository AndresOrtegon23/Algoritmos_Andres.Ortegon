import time

def ordenamientoInsercionParaCubetas(arreglo, metricas):
    for i in range(1, len(arreglo)):
        clave = arreglo[i]
        j = i - 1
        while j >= 0:
            metricas["comparaciones"] += 1
            if arreglo[j] > clave:
                arreglo[j + 1] = arreglo[j]
                metricas["intercambios"] += 1
                j -= 1
            else:
                break
        arreglo[j + 1] = clave
    return arreglo

def ordenamientoCubetas(arreglo, numeroCubetas, metricas):
    if len(arreglo) == 0:
        return arreglo

    valorMinimo = min(arreglo)
    valorMaximo = max(arreglo)
    
    if valorMinimo == valorMaximo:
        return arreglo

    rangoCubeta = (valorMaximo - valorMinimo) / numeroCubetas
    cubetas = [[] for _ in range(numeroCubetas)]

    for numero in arreglo:
        indiceCubeta = int((numero - valorMinimo) / rangoCubeta)
        if indiceCubeta == numeroCubetas:
            indiceCubeta -= 1
        cubetas[indiceCubeta].append(numero)

    arregloOrdenado = []
    for cubeta in cubetas:
        ordenamientoInsercionParaCubetas(cubeta, metricas)
        arregloOrdenado.extend(cubeta)

    return arregloOrdenado

# Ejemplo y ejecución
metricasBucket = {"comparaciones": 0, "intercambios": 0}
datosBucket = [i for i in range(1000, 0, -1)]

tiempoInicio = time.time()
ordenamientoCubetas(datosBucket, 50, metricasBucket)
tiempoFin = time.time()

print(" Bucket Sort (50 cubetas) ")
print(f"Comparaciones: {metricasBucket['comparaciones']}")
print(f"Intercambios: {metricasBucket['intercambios']}")
print(f"Tiempo: {tiempoFin - tiempoInicio:.6f} segundos\n")