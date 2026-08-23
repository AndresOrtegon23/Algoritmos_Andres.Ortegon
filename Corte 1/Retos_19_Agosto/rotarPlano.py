def rotar_90_grados(matriz: list[list[int]]) -> list[list[int]]:
    
    # Determinamos las dimensiones originales
    f = len(matriz)          # Número de filas originales
    c = len(matriz[0])       # Número de columnas originales
    
    # La matriz rotada intercambia sus dimensiones: tendrá c filas y f columnas.
    # Inicializamos la nueva estructura rellenándola con ceros (0).
    matriz_rotada = [[0 for _ in range(f)] for _ in range(c)]
    
    # Recorremos cada elemento de la matriz original
    for i in range(f):
        for j in range(c):
            # Aplicamos la fórmula matemática de rotación horaria:
            # El elemento en la posición (i, j) se reubica en la posición (j, f - 1 - i)
            matriz_rotada[j][f - 1 - i] = matriz[i][j]
            
    return matriz_rotada
    
    # Definimos la matriz de prueba (2 filas x 3 columnas)
    
matriz_original = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    # Mostramos la matriz original en consola
print("--- MATRIZ ORIGINAL (2x3) ---")
for fila in matriz_original:
        print(fila)

    # Aplicamos la función de rotación
matriz_resultado = rotar_90_grados(matriz_original)

    # Mostramos el resultado de la transformación
print("\n--- MATRIZ ROTADA 90° HORARIO (3x2) ---")
for fila in matriz_resultado:
        print(fila)