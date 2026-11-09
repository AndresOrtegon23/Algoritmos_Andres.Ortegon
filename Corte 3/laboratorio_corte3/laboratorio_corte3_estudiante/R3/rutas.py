# ============================================================
#  Laboratorio integrador · Corte 3 · RETO 3  (25 puntos)
#  Sesiones 40 y 42 — Representacion de grafos y BFS
#  Sistema: RedAcopio — rutas minimas entre puntos de la red
#
#  MODIFIQUE SOLO ESTE ARCHIVO.  NO TOQUE pruebas_r3.py
#  Ejecute:   python3 pruebas_r3.py
# ============================================================
from collections import deque

NOMBRES = ["ACOPIO","NORTE","SUR","ORIENTE","OCCIDENTE",
           "PLANTA","TALLER","PUERTO","VEREDA","MINA"]
ARISTAS = [(0,1),(0,2),(0,3),(1,4),(1,5),(2,7),(3,6),(5,6),(4,7),(7,8),(6,9)]
N = len(NOMBRES)


def construir():
    """Devuelve la lista de adyacencia: una lista de N listas.
       El grafo es NO DIRIGIDO, asi que cada arista se registra en los dos
       extremos. Cada lista de vecinos debe quedar ORDENADA de menor a mayor."""
    lista=[[] for _ in range(N)]
    for u, v in ARISTAS:
        lista[u].append(v)
        lista[v].append(u)
    for vecinos in lista:
        vecinos.sort()
    return lista    


def bfs(inicio):
    """Recorrido en anchura desde 'inicio'.
       Devuelve la tupla (orden, dist, padre):
         orden  lista de vertices en el orden en que se atendieron
         dist   dist[v] = numero de tramos desde inicio (-1 si no se alcanza)
         padre  padre[v] = vertice desde el que se llego a v (-1 para el inicio)

       Recuerde: se marca el vertice al ENCOLARLO, no al sacarlo."""
    lista = construir() #se construye la lista de adyacencia del grafo
    orden = [] #creamos la lista de orden que va marcar el orden de los modulos visitados
    dist = [-1] * N #creamos la lista dist que va marcar la distancia de cada modulo al modulo de inicio
    padre = [-1] * N #creamos lista padre que va marcar el modulo desde el cual se llego a cada modulo
    cola = deque() #se crea la cola que va a almacenar los modulos a visitar

    dist[inicio] = 0 #se marca la distancia del modulo de inicio como 0
    cola.append(inicio) #se encola el modulo de inicio

    while cola: #mientras la cola no este vacia
        v = cola.popleft() #se desencola el primer modulo de la cola
        orden.append(v) #se agrega el modulo a la lista de orden
        for vecino in lista[v]: #se recorren los vecinos del modulo actual
            if dist[vecino] == -1:  # No visitado
                dist[vecino] = dist[v] + 1 #se marca la distancia del vecino como la distancia del modulo actual + 1
                padre[vecino] = v #se marca el modulo actual como el padre del vecino 
                cola.append(vecino) #se encola el vecino para visitarlo posteriormente

    return orden, dist, padre




def camino(destino, padre):
    """Ya implementado: reconstruye la ruta siguiendo el arreglo padre."""
    ruta = []
    v = destino
    while v != -1:
        ruta.append(NOMBRES[v])
        v = padre[v]
    return list(reversed(ruta))


def por_niveles(dist):
    """Devuelve una lista de listas: en la posicion d, los NOMBRES de los
       vertices que estan a distancia d del origen."""
    niveles = [[] for _ in range(max(dist) + 1)] #creamos una lista de listas para almacenar los modulos por niveles
    for v in range(N): #recorremos todos los modulos
        if dist[v] != -1: #si el modulo es alcanzable desde el inicio
            niveles[dist[v]].append(NOMBRES[v]) #agregamos el modulo a la lista correspondiente a su nivel
    return niveles #devolvemos la lista de niveles
