import time

# Variables globales para rastrear la mejor solucion y el conteo de caminos
pasosMinimos = 100000
mejorCamino = None
totalCaminosEncontrados = 0


def contarCaminosParteA(f, c, laberinto, caminoActual, filas, cols):
    # Declaracion de variables globales a modificar
    global totalCaminosEncontrados

    # 1. ¿Me sali del tablero?
    if f < 0 or f >= filas or c < 0 or c >= cols:
        return

    # 2. ¿Es muro (1) o ya pase por esta casilla en la ruta actual?
    if laberinto[f][c] == 1 or caminoActual[f][c] == 1:
        return

    # 3. Marco la casilla como parte del camino actual
    caminoActual[f][c] = 1

    # 4. CASO BASE: Llegar a la esquina inferior derecha
    if f == filas - 1 and c == cols - 1:
        totalCaminosEncontrados += 1
    else:
        # 5. CASO RECURSIVO: Probar las 4 direcciones para explorar todos los caminos
        direcciones = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for df, dc in direcciones:
            contarCaminosParteA(f + df, c + dc, laberinto, caminoActual, filas, cols)

    # 6. BACKTRACKING: Desmarco la casilla para evaluar rutas alternativas
    caminoActual[f][c] = 0


def resolverParteBMejorRuta(f, c, acopiosRecogidos, totalAcopios, laberinto, caminoActual, pasosActuales, filas, cols):
    # Declaracion de variables globales a modificar
    global pasosMinimos, mejorCamino, totalCaminosEncontrados

    # 1. ¿Me sali del tablero?
    if f < 0 or f >= filas or c < 0 or c >= cols:
        return

    # 2. ¿Es muro (1) o ya pase por esta casilla en la ruta actual?
    if laberinto[f][c] == 1 or caminoActual[f][c] == 1:
        return

    # Verifico si la casilla actual es un punto de acopio (2)
    esAcopio = (laberinto[f][c] == 2)
    nuevoAcopiosRecogidos = acopiosRecogidos + 1 if esAcopio else acopiosRecogidos

    # 3. Marco la casilla como parte del camino actual
    caminoActual[f][c] = 1

    # 4. CASO BASE: Esquina inferior derecha habiendo recogido TODOS los acopios
    if f == filas - 1 and c == cols - 1:
        if nuevoAcopiosRecogidos == totalAcopios:
            totalCaminosEncontrados += 1
            if pasosActuales < pasosMinimos:
                pasosMinimos = pasosActuales
                # Guarda una copia de la mejor matriz de camino encontrada
                mejorCamino = [fila[:] for fila in caminoActual]
    else:
        # 5. CASO RECURSIVO: Explora las 4 direcciones posibles sin podas para contar todo
        direcciones = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for df, dc in direcciones:
            resolverParteBMejorRuta(
                f + df,
                c + dc,
                nuevoAcopiosRecogidos,
                totalAcopios,
                laberinto,
                caminoActual,
                pasosActuales + 1,
                filas,
                cols
            )

    # 6. BACKTRACKING: Desmarco la casilla para evaluar otras rutas
    caminoActual[f][c] = 0


def contarAcopios(laberinto):
    # Cuenta el numero total de puntos de acopio (2) en el mapa
    total = 0
    for fila in laberinto:
        total += fila.count(2)
    return total


def imprimirMapa(laberinto, camino):
    # Imprime la matriz del laberinto marcando la ruta con viñetas
    filas = len(laberinto)
    cols = len(laberinto[0])
    for f in range(filas):
        for c in range(cols):
            if camino[f][c] == 1:
                print("•", end=" ")
            else:
                print(laberinto[f][c], end=" ")
        print()
    print()


def ejecutarPruebas(nombreMapa, mapa):
    # Variables globales para almacenar los resultados
    global pasosMinimos, mejorCamino, totalCaminosEncontrados

    filas = len(mapa)
    cols = len(mapa[0])
    totalAcopios = contarAcopios(mapa)
    caminoInicial = [[0] * cols for _ in range(filas)]

    print(f" MAPA {nombreMapa} ")

    # PARTE A: Conteo de todos los caminos básicos sin acopios
    totalCaminosEncontrados = 0
    contarCaminosParteA(0, 0, mapa, caminoInicial, filas, cols)
    print(f"Parte A - Cantidad de caminos distintos hacia la salida: {totalCaminosEncontrados}")

    # PARTE B: Conteo de caminos con recolección completa y selección del mejor
    pasosMinimos = 100000
    mejorCamino = None
    totalCaminosEncontrados = 0

    inicioTiempo = time.time()
    resolverParteBMejorRuta(0, 0, 0, totalAcopios, mapa, caminoInicial, 0, filas, cols)
    finTiempo = time.time()

    print(f"Parte B - Cantidad de caminos distintos con recolección completa: {totalCaminosEncontrados}")

    if mejorCamino is not None:
        print("Ruta más rápida y eficiente (menor cantidad de pasos):")
        imprimirMapa(mapa, mejorCamino)
        print(f"Pasos mínimos requeridos: {pasosMinimos}")
    else:
        print("No se encontró ninguna ruta válida que recoja todos los acopios sin repetir casillas.")

    print(f"Tiempo real de ejecución: {finTiempo - inicioTiempo:.6f} segundos\n" )
    
if __name__ == "__main__":
    # Definicion de mapas de prueba
    mapa5x5 = [
        [0, 0, 0, 0, 0],
        [0, 2, 1, 0, 0],
        [0, 0, 1, 0, 2],
        [1, 0, 0, 0, 1],
        [0, 0, 1, 0, 0]
    ]

    mapa10x10 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 1, 0, 0, 1, 0, 2, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 0, 1, 1, 0, 0],
        [0, 1, 0, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 2, 0],
        [0, 1, 0, 1, 0, 1, 0, 0, 0, 0]
    ]

    # Ejecucion de las pruebas
    ejecutarPruebas("5x5", mapa5x5)
    ejecutarPruebas("10x10", mapa10x10)