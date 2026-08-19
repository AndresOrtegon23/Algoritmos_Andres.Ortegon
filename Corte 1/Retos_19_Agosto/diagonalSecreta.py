def analizar_diagonales(matriz: list[list[int]]) -> None:
    
    # Obtenemos el tamaño de la matriz (número de filas/columnas)
    n = len(matriz)
    
    # Inicializamos los acumuladores para las sumas
    suma_principal = 0
    suma_secundaria = 0

    # Recorremos la matriz en una sola pasada usando el índice 'i'
    for i in range(n):
        # 1. Diagonal principal: Los índices de fila y columna son idénticos (matriz[i][i])
        suma_principal += matriz[i][i]
        
        # 2. Diagonal secundaria: La fila avanza pero la columna retrocede (matriz[i][n - 1 - i])
        suma_secundaria += matriz[i][n - 1 - i]

    # Evaluamos si las sumas de ambas diagonales coinciden
    son_iguales = suma_principal == suma_secundaria

    # Visualización de resultados en consola
    print(f"1. Suma de la diagonal principal: {suma_principal}")
    print(f"2. Suma de la diagonal secundaria: {suma_secundaria}")
    print(f"3. ¿Son iguales?: {'Sí' if son_iguales else 'No'}")


# ==========================================
# BLOQUE PRINCIPAL DE EJECUCIÓN
# ==========================================
if __name__ == "__main__":
    
    # Definimos la matriz cuadrada de prueba (3x3)
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Imprimimos la matriz de forma ordenada para el usuario
    print("--- MATRIZ CUADRADA ---")
    for fila in matriz:
        print(fila)
    print("-" * 25 + "\n")

    # Ejecutamos la función de análisis
    analizar_diagonales(matriz)