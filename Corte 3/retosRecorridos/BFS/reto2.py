from collections import deque

class GradosSeparacion:

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

  def _ejecutarBfsDistancias(self, inicio):
    """Ejecuta un BFS desde un vértice de origen y devuelve un diccionario con

    las distancias mínimas (en número de tramos) a todos los demás alcanzables.
    """
    visitado = {sede: False for sede in self.sedes}
    dist = {sede: -1 for sede in self.sedes}
    cola = deque([inicio])

    visitado[inicio] = True
    dist[inicio] = 0

    while cola:
      u = cola.popleft()
      for v in self.listaAdyacencia.get(u, []):
        if not visitado[v]:
          visitado[v] = True
          dist[v] = dist[u] + 1
          cola.append(v)

    return dist

  def calcularDiametroYAnalisis(self):
    """Calcula la distancia mínima entre cada par de vértices,

    identifica el diámetro de la red y el par de puntos más alejados.
    """
    diametroMaximo = 0
    parMasAlejado = ("", "")
    matrizDistancias = {}

    # Un BFS desde cada vértice: O(V * (V + E))
    for origen in self.sedes:
      distanciasOrigen = self._ejecutarBfsDistancias(origen)
      matrizDistancias[origen] = distanciasOrigen

      for destino, distancia in distanciasOrigen.items():
        # Ignoramos distancias a sí mismo (-1 por si hay nodos desconectados)
        if origen != destino and distancia > diametroMaximo:
          diametroMaximo = distancia
          parMasAlejado = (origen, destino)

    print(f"\n Grados de separacon y de la red ")
    print(f"Diámetro de la red: {diametroMaximo} tramos.")
    print(
        "Par de puntos más alejados (los más distantes entre sí):"
        f" '{parMasAlejado[0]}' y '{parMasAlejado[1]}'."
    )

    print("\n Respuesta")
    print(
        f"El hecho de que el diámetro de nuestra red sea de {diametroMaximo}"
        f" tramos significa que, en el peor de los casos,"
        " cualquier solicitud de préstamo de emergencia o traslado de un"
        " recurso agotado entre los extremos más lejanos de las sedes requerirá"
        f" exactamente {diametroMaximo} saltos intermedios de transporte o"
        " validación logística.\n"
        "Para la operación del sistema, esto indica que los recursos de alta"
        " demanda no deben concentrarse en un solo extremo,"
        " sino distribuirse estratégicamente en nodos"
        " centrales para reducir los tiempos de espera y"
        " evitar cuellos de botella en las zonas periféricas."
    )

analizadorRed = GradosSeparacion()
analizadorRed.calcularDiametroYAnalisis()