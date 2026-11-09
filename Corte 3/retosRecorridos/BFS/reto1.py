from collections import deque 

class ModuloRutas:

  def __init__(self):
    self.sedes = [
        "Quinta",
        "Claustro",
        "Norte",
        "Mederi",
        "Cardioinfantil",
        "GSB",
        "Nuestra Señora",
    ]

    # Lista de adyacencia de la red de sedes (grafo no dirigido)
    self.listaAdyacencia = {
        "Quinta": ["Claustro"],
        "Claustro": ["Quinta", "Norte", "GSB"],
        "Norte": ["Claustro", "Mederi"],
        "Mederi": ["Norte", "Cardioinfantil"],
        "Cardioinfantil": ["Mederi", "Nuestra Señora"],
        "GSB": ["Claustro"],
        "Nuestra Señora": ["Cardioinfantil"],
    }

  def desconectarSede(self, u, v):
    """Método auxiliar para simular una red partida o inalcanzable."""
    if v in self.listaAdyacencia[u]:
      self.listaAdyacencia[u].remove(v)
    if u in self.listaAdyacencia[v]:
      self.listaAdyacencia[v].remove(u)

  def ruta(self, origen, destino):
    """Calcula el camino con menos tramos (aristas) usando BFS,

    su longitud y maneja los casos especiales.
    """
    if origen not in self.listaAdyacencia or destino not in self.listaAdyacencia:
      return "Error: El origen o el destino no existen en la red de sedes.", -1

    # Caso especial: Origen igual a destino
    if origen == destino:
      return [origen], 0

    # Inicialización de estructuras para BFS
    visitado = {sede: False for sede in self.sedes}
    dist = {sede: -1 for sede in self.sedes}
    padre = {sede: None for sede in self.sedes}
    cola = deque([origen])

    visitado[origen] = True  # Se marca al encolar
    dist[origen] = 0

    while cola:
      u = cola.popleft()

      for v in self.listaAdyacencia.get(u, []):
        if not visitado[v]:
          visitado[v] = True
          dist[v] = dist[u] + 1
          padre[v] = u
          cola.append(v)

    # Verificación del caso sin camino (si la distancia sigue en -1)
    if dist[destino] == -1:
      return f"No hay camino disponible entre {origen} y {destino}.", -1

    # Reconstrucción del camino usando el arreglo padre
    rutaReconstruida = []
    actual = destino
    while actual is not None:
      rutaReconstruida.append(actual)
      actual = padre[actual]

    rutaReconstruida.reverse()
    longitudTramos = dist[destino]

    return rutaReconstruida, longitudTramos

sistemaRutas = ModuloRutas()

print(" Ruta normal (Alcanzable) ")
camino, longitud = sistemaRutas.ruta("Quinta", "Nuestra Señora")
print(f"Camino: {' -> '.join(camino)} | Longitud (tramos): {longitud}")

print("\n Origen igual a destino ")
camino, longitud = sistemaRutas.ruta("Claustro", "Claustro")
print(f"Camino: {camino} | Longitud (tramos): {longitud}")

print("\n Destino inalcanzable (desconectando una arista) ")
# Desconectamos el puente principal hacia Cardioinfantil y Nuestra Señora
sistemaRutas.desconectarSede("Mederi", "Cardioinfantil")
camino, longitud = sistemaRutas.ruta("Quinta", "Nuestra Señora")
print(f"Resultado: {camino} | Longitud: {longitud}")