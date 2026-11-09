from collections import deque

class PropagacionOlas:

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

    # Lista de adyacencia de la red de sedes
    self.listaAdyacencia = {
        "Quinta": ["Claustro"],
        "Claustro": ["Quinta", "Norte", "GSB"],
        "Norte": ["Claustro", "Mederi"],
        "Mederi": ["Norte", "Cardioinfantil"],
        "Cardioinfantil": ["Mederi", "Nuestra Señora"],
        "GSB": ["Claustro"],
        "Nuestra Señora": ["Cardioinfantil"],
    }

  def ejecutarBfsDistancias(self, inicio):
    """Usa BFS para calcular cuántos minutos (tramos) tarda la onda

    en llegar desde el punto de origen a cada sede.
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

  def simularPropagacionFalla(self, puntoOrigen):
    """Simula cómo se riega el problema y en qué minuto le pega a cada punto."""
    distanciasMinutos = self.ejecutarBfsDistancias(puntoOrigen)
    tiempoTotalCaida = max(distanciasMinutos.values())

    print(f"\n--- Simulando qué pasa si la falla arranca en '{puntoOrigen}' ---")
    print(f"La red completa tarda {tiempoTotalCaida} minutos en colapsar.")
    print("Así se va afectando cada sede minuto a minuto:")
    for sede, minuto in distanciasMinutos.items():
      print(f" - {sede}: le pega en el minuto {minuto}")

    return tiempoTotalCaida

  def analizarPuntoMenosConveniente(self):
    """Revisa cuál es el peor punto para que inicie la falla (el más periférico)."""
    excentricidades = {}

    for sede in self.sedes:
      distancias = self.ejecutarBfsDistancias(sede)
      # Buscamos la distancia máxima desde este nodo hacia cualquier otro
      excentricidades[sede] = max(distancias.values())

    # Identificamos el tiempo máximo de excentricidad en la red
    maximaExcentricidad = max(excentricidades.values())
    
    # Filtramos todos los nodos que comparten esa excentricidad máxima (los más periféricos)
    puntosMasPerifericos = [
        sede for sede, exc in excentricidades.items() if exc == maximaExcentricidad
    ]

    print("\n--- ¿Desde dónde conviene MENOS que empiece el problema? ---")
    print("Esto es lo que tarda la falla en llegar al peor punto de la red:")
    for sede, exc in excentricidades.items():
      print(f" - Si arranca en '{sede}': el punto más lejano tarda hasta {exc} minutos en ser alcanzado.")

    print(
        f"\nLos peores lugares para pararse son {puntosMasPerifericos}, ya que"
        f" son los más apartados (periféricos) de la red y la onda tarda hasta"
        f" {maximaExcentricidad} minutos en recorrerlos por completo.\n\n"
        "¿Por qué no poner un centro de distribución en estos extremos? Sería una pésima"
        " idea. Quedarían tan lejos del resto del sistema que cualquier envío urgente,"
        " recurso o respuesta logística tardaría demasiado en cruzar toda la red."
        " Lo lógico es ubicarlo en un nodo central (como el 'Claustro', que tiene menor excentricidad),"
        " para que las cosas fluyan rápido y la operación sea eficiente."
    )


# Pruebas directas
sistemaPropagacion = PropagacionOlas()
sistemaPropagacion.simularPropagacionFalla("Nuestra Señora")
sistemaPropagacion.analizarPuntoMenosConveniente()