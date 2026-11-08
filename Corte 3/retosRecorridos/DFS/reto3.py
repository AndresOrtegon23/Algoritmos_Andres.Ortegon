import time

class AnalizadorRutas:

  def __init__(self, redSedes):
    # Recibe un diccionario con la lista de adyacencia de la red
    self.listaAdyacencia = redSedes
    self.caminoMasLargo = []
    self.maxLongitud = -1

  def _backtrackingCaminoLargo(self, actual, destino, visitados, caminoActual):
    """Algoritmo recursivo con backtracking (marcar y desmarcar al regresar)."""
    caminoActual.append(actual)
    visitados.add(actual)

    if actual == destino:
      # Si encontramos el destino, evaluamos si este camino es el más largo hasta ahora
      if len(caminoActual) > self.maxLongitud:
        self.maxLongitud = len(caminoActual)
        self.caminoMasLargo = list(caminoActual)
    else:
      # Exploramos vecinos
      for vecino in self.listaAdyacencia.get(actual, []):
        if vecino not in visitados:
          self._backtrackingCaminoLargo(vecino, destino, visitados, caminoActual)

    # BACKTRACKING: Desmarcar y sacar del camino al regresar
    visitados.remove(actual)
    caminoActual.pop()

  def encontrarCaminoMasLargo(self, origen, destino):
    """Encuentra el camino simple más largo entre origen y destino."""
    self.caminoMasLargo = []
    self.maxLongitud = -1
    visitados = set()
    caminoActual = []

    self._backtrackingCaminoLargo(origen, destino, visitados, caminoActual)
    return self.caminoMasLargo, self.maxLongitud


# --- FUNCIÓN PARA MEDIR TIEMPOS CON 9, 15 Y 20 VÉRTICES ---
def medirTiemposEscalabilidad():
  # 1. Red pequeña de 9 vértices (similar a las sedes de la red)
  red9 = {
      "Quinta": ["Claustro", "Norte"],
      "Claustro": ["Quinta", "Norte", "GSB", "Mederi"],
      "Norte": ["Quinta", "Claustro", "Mederi"],
      "Mederi": ["Norte", "Claustro", "Cardioinfantil"],
      "Cardioinfantil": ["Mederi", "Nuestra Señora"],
      "GSB": ["Claustro", "Nuestra Señora"],
      "Nuestra Señora": ["Cardioinfantil", "GSB", "SedeA"],
      "SedeA": ["Nuestra Señora", "SedeB"],
      "SedeB": ["SedeA"],
  }

  # 2. Generar redes sintéticas de 15 y 20 vértices interconectadas densamente
  def generarRedSintetica(n):
    red = {}
    for i in range(n):
      nombre = f"V{i}"
      vecinos = []
      # Conectamos con varios nodos adyacentes para aumentar las opciones de rutas y ciclos
      for j in range(n):
        if i != j and abs(i - j) <= 3:
          vecinos.append(f"V{j}")
      red[nombre] = vecinos
    return red

  red15 = generarRedSintetica(15)
  red20 = generarRedSintetica(20)

  print("\n  Medicion de tiempo con los caminos ")

  # Prueba con 9 vértices
  analizador9 = AnalizadorRutas(red9)
  inicio = time.time()
  ruta9, lon9 = analizador9.encontrarCaminoMasLargo("Quinta", "SedeB")
  fin = time.time()
  print(f"Red de 9 vértices -> Tiempo: {fin - inicio:.6f} segundos.")

  # Prueba con 15 vértices
  analizador15 = AnalizadorRutas(red15)
  inicio = time.time()
  ruta15, lon15 = analizador15.encontrarCaminoMasLargo("V0", "V14")
  fin = time.time()
  print(f"Red de 15 vértices -> Tiempo: {fin - inicio:.6f} segundos.")

  # Prueba con 20 vértices (Aquí el crecimiento exponencial se hace evidente)
  analizador20 = AnalizadorRutas(red20)
  inicio = time.time()
  ruta20, lon20 = analizador20.encontrarCaminoMasLargo("V0", "V19")
  fin = time.time()
  print(f"Red de 20 vértices -> Tiempo: {fin - inicio:.6f} segundos.")

  print(
        "\n¿Por qué el camino más corto es fácil y el más"
        " largo no?"
    )
  print(
        "Encontrar el camino más corto "
        " es muy rápido porque se rige por una regla lógica: cualquier pedazo "
        "intermedio de una ruta mínima también es el más corto. Eso permite"
        " avanzar por niveles descartando caminos largos al instante, lo que"
        " hace que el programa vuele.\n\n"
        "Con el camino más largo sin repetir vértices pasa todo lo contrario. No"
        " hay atajos ni reglas que salven trabajo, así que el programa se ve"
        " obligado a probar una por una todas las combinaciones posibles"
        " asegurándose de no pasar dos veces por el mismo sitio. Como las"
        " opciones se multiplican de forma exagerada (O(V)), en cuanto"
        " pasamos de 20 vértices las cuentas se vuelven tan gigantescas que el"
        " computador se congela o tarda una eternidad. Es lo que en ciencias"
        " de la computación se conoce como un problema NP-difícil: fácil de"
        " plantear, pero imposible de resolver rápido a gran escala."
    )


# Ejecución de la prueba directamente
medirTiemposEscalabilidad()