# Listas con los nombres de los recursos y los días de la semana
recursos = ["Computador", "Videobeam", "Sala"]
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

# Matriz que contiene los préstamos de cada recurso (filas) para cada día (columnas)
matriz = [
    [4, 6, 2, 8, 5],
    [2, 3, 1, 4, 2],
    [5, 5, 4, 6, 8]
]

# Se obtienen las dimensiones de la matriz (3 filas x 5 columnas)
numFilas = len(matriz)
numColumnas = len(matriz[0])

# Construir el encabezado alineado con los nombres de días y la columna 'Total'
titulos = f"{'Recurso':<12}" + "".join([f"{dias[j]:>12}" for j in range(numColumnas)]) + f"{'Total':>12}"
print(titulos)
print("-" * len(titulos)) # Imprimir línea divisoria

# Recorrer cada fila (recurso) de la matriz
for i in range(numFilas):
    # Calcular la suma total del recurso actual usando la función sum() en la fila
    sumaRecurso = sum(matriz[i])
    
    # Formatear la fila actual con los datos del recurso, préstamos diarios y el total acumulado
    fila = f"{recursos[i]:<12}" + "".join([f"{matriz[i][j]:>12}" for j in range(numColumnas)]) + f"{sumaRecurso:>12}"
    print(fila)

# Variables auxiliares para almacenar el valor máximo de préstamos y el nombre del día
maxCarga = -1
diaMasCargado = ""

# Recorrer la matriz por columnas (días de la semana)
for j in range(numColumnas):
    # Acumulador para sumar el total de préstamos del día actual
    sumDia = 0
    
    # Sumar los valores de cada recurso prestado en el día j
    for i in range(numFilas):
        sumDia += matriz[i][j]
    
    # Comparar la suma del día con el máximo actual y actualizar si es mayor
    if sumDia > maxCarga:
        maxCarga = sumDia
        diaMasCargado = dias[j]

# Imprimir el resultado final del día con mayor actividad
print("\n" + "-" * 40)
print(f"El dia mas cargado fue el {diaMasCargado} con un total de {maxCarga} prestamos.")