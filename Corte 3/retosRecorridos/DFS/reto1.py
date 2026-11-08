class RedSedes:

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

    # Representación mediante lista de adyacencia (grafo no dirigido)
    self.listaAdyacencia = {
        "Quinta": ["Claustro"],
        "Claustro": ["Quinta", "Norte", "GSB"],
        "Norte": ["Claustro", "Mederi"],
        "Mederi": ["Norte", "Cardioinfantil"],
        "Cardioinfantil": ["Mederi", "Nuestra Señora"],
        "GSB": ["Claustro"],
        "Nuestra Señora": ["Cardioinfantil"],
    }

  def eliminarArista(self, u, v):
    """Elimina una conexión (arista) entre dos sedes en ambas direcciones."""
    if v in self.listaAdyacencia[u]:
      self.listaAdyacencia[u].remove(v)
    if u in self.listaAdyacencia[v]:
      self.listaAdyacencia[v].remove(u)

  def dfsComponente(self, u, visitado, componenteActual):
    """Algoritmo DFS recursivo para explorar una componente conexa (isla)."""
    visitado[u] = True  # El hilo de Ariadna
    componenteActual.append(u)
    for v in self.listaAdyacencia[u]:
      if not visitado[v]:
        self.dfsComponente(v, visitado, componenteActual)

  def detectarIslas(self):
    """Identifica todas las componentes conexas (islas) de la red."""
    visitado = {sede: False for sede in self.sedes}
    componentes = []

    for sede in self.sedes:
      if not visitado[sede]:
        componenteActual = []
        self.dfsComponente(sede, visitado, componenteActual)
        componentes.append(componenteActual)

    return componentes

  def generarInforme(self):
    """Genera un informe automático y legible sobre el estado de la red."""
    componentes = self.detectarIslas()
    numComponentes = len(componentes)
    masGrande = max(componentes, key=len)

    print(f"\nINFORME DE CONECTIVIDAD DE LA RED DE SEDES ")
    if numComponentes == 1:
      print("La red está totalmente conectada (forma una única zona operativa).")
    else:
      print(f"La red está partida en {numComponentes} zonas (islas).")

    for i, comp in enumerate(componentes, 1):
      tieneCentro = "Claustro" in comp or "Quinta" in comp
      estadoCentro = (
          "tiene conexión con el centro"
          if tieneCentro
          else "no tiene conexión con el centro"
      )
      print(
          f" - La zona {i} tiene {len(comp)} punto(s) ({', '.join(comp)}) y"
          f" {estadoCentro}."
      )

    print(
        f"-> La zona más grande contiene {len(masGrande)} puntos:"
        f" {', '.join(masGrande)}.\n"
    )
    
# Ejecución directa de prueba
red = RedSedes()

print("Estado inicial de la red de sedes:")
red.generarInforme()

print(
    "Eliminando dos aristas a propósito: 'Claustro - Norte' y 'Mederi"
    " - Cardioinfantil'"
)
red.eliminarArista("Claustro", "Norte")
red.eliminarArista("Mederi", "Cardioinfantil")

print("Estado de la red tras la desconexión de tramos:")
red.generarInforme()