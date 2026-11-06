#Quiz 6/11/2026

from collections import deque

NOMBRES = ["CENTRO", "NORTE", "SUR", "ORIENTE", "OCCIDENTE", 
           "CHAPINERO", "USAQUEN", "BOSA", "VEREDA"]

ARISTAS = [
    (0,1), (1,3), (0,2), (0,3), (1,5),
    (2,7), (3,6), (5,6), (4,7), (7,8),
    (8,1), (7,5), (5,8), (2,6), (6,8),
    (1,8), (5,7), (5,2)
]

N = len(NOMBRES)

COLORES = {
    "AZUL": [0],
    "VERDE": [1, 2, 3],
    "ROJO": [4, 5, 6, 7],
    "BLANCO": [8]
}

# Construcción de la lista de adyacencia
lista = [[] for _ in range(N)]
for u, v in ARISTAS:
    lista[u].append(v); lista[v].append(u)
for v in lista: v.sort()

def bfs(inicio, destino):
    visitado = [False] * N
    dist = [-1] * N
    padre = [-1] * N
    cola = deque([inicio])
    
    visitado[inicio] = True
    dist[inicio] = 0
    
    while cola:
        u = cola.popleft()
        if u == destino:
            break
        for v in lista[u]:
            if not visitado[v]:
                visitado[v] = True
                dist[v] = dist[u] + 1
                padre[v] = u
                cola.append(v)
                
    # Reconstruir el camino
    camino = []
    actual = destino
    while actual != -1:
        camino.append(actual)
        actual = padre[actual]
    camino.reverse()
    
    return camino, dist[destino]

def dfs(inicio, destino):
    visitado = [False] * N
    padre = [-1] * N
    encontrado = False

    def dfsRec(u):
        nonlocal encontrado
        if u == destino:
            encontrado = True
            return
        visitado[u] = True
        for v in lista[u]:
            if not visitado[v] and not encontrado:
                padre[v] = u
                dfsRec(v)

    dfsRec(inicio)

    # Reconstruir el camino
    camino = []
    actual = destino
    while actual != -1:
        camino.append(actual)
        actual = padre[actual]
    camino.reverse()
    
    return camino if encontrado and len(camino) > 1 else []

# Ejecución y Resultados
inicio = 0  # CENTRO
destino = 8 # VEREDA

caminoBfs, tramosBfs = bfs(inicio, destino)
caminoDfs = dfs(inicio, destino)

print("COLORES")
for color, indices in COLORES.items():
    nombresColor = [NOMBRES[i] for i in indices]
    print(f"Color {color}: {nombresColor}")

print("\n Camino mas corto desde CENTRO hasta VEREDA")
print("Con BFS:")
cadenaBfs = " -> ".join(NOMBRES[i] for i in caminoBfs)
print(f"  Camino: {cadenaBfs} ({tramosBfs} tramos)")

print("\nCon DFS :")
if caminoDfs:
    tramosDfs = len(caminoDfs) - 1
    cadenaDfs = " -> ".join(NOMBRES[i] for i in caminoDfs)
    print(f"  Camino: {cadenaDfs} ({tramosDfs} tramos)")
else:
    print("  No se encontró camino.")