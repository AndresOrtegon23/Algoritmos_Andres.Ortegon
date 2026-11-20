class PlanEstudios:

  def __init__(self, asignaturas, grafoDirigido):
    self.asignaturas = asignaturas
    self.grafoDirigido = grafoDirigido

  def dfsDetectarCiclo(self, u, estados, padres, cicloActual):
    """Explora recursivamente usando 3 estados:

    0: sin visitar, 1: en proceso, 2: terminado.
    """
    estados[u] = 1  # 1: En proceso

    for v in self.grafoDirigido.get(u, []):
      if estados[v] == 1:
        # Encontramos un ciclo: reconstruimos la secuencia
        cicloActual.append(v)
        actual = u
        while actual != v and actual is not None:
          cicloActual.append(actual)
          actual = padres.get(actual)
        cicloActual.append(v)
        return True

      elif estados[v] == 0:
        padres[v] = u
        if self.dfsDetectarCiclo(v, estados, padres, cicloActual):
          return True

    estados[u] = 2  # 2: Terminado
    return False

  def verificarPlanEstudios(self):
    """Verifica si el plan de estudios es cursable o contiene un ciclo de prerrequisitos."""
    estados = {asignatura: 0 for asignatura in self.asignaturas}
    padres = {asignatura: None for asignatura in self.asignaturas}
    cicloInvertido = []

    tieneCiclo = False
    for asignatura in self.asignaturas:
      if estados[asignatura] == 0:
        if self.dfsDetectarCiclo(asignatura, estados, padres, cicloInvertido):
          tieneCiclo = True
          break

    print(f"\n PLAN DE ESTUDIOS ")
    if tieneCiclo:
      secuenciaCiclo = list(reversed(cicloInvertido))
      print(
          "Plan de estudios imposible: Se ha detectado un ciclo de"
          " prerrequisitos."
      )
      print(
          "Secuencia de asignaturas que forman el ciclo: "
          f"{' -> '.join(secuenciaCiclo)}"
      )
    else:
      print(
          "El plan de estudios es totalmente cursable (no se encontraron"
          " ciclos)."
      )


# Definición común de asignaturas
listaAsignaturas = [
    "Cálculo I",
    "Cálculo II",
    "Álgebra Lineal",
    "Estructuras de Datos",
    "Inteligencia Artificial",
    "Matemáticas Discretas",
]

# Plan CON ciclo a propósito (Debe mostrar la secuencia del ciclo)
grafoConCiclo = {
    "Cálculo I": ["Cálculo II"],
    "Cálculo II": ["Estructuras de Datos"],
    "Álgebra Lineal": ["Inteligencia Artificial"],
    "Estructuras de Datos": [
        "Inteligencia Artificial",
        "Cálculo I",
    ],  # ¡Aquí se cierra el ciclo hacia Cálculo I!
    "Inteligencia Artificial": [],
    "Matemáticas Discretas": ["Estructuras de Datos"],
}

print("EJECUTANDO PRUEBA 1 (Con ciclo):")
plan1 = PlanEstudios(listaAsignaturas, grafoConCiclo)
plan1.verificarPlanEstudios()


# --- PRUEBA 2: Plan SIN ciclos (Debe imprimir que es totalmente cursable) ---
grafoSinCiclo = {
    "Cálculo I": ["Cálculo II"],
    "Cálculo II": ["Estructuras de Datos"],
    "Álgebra Lineal": ["Inteligencia Artificial"],
    "Estructuras de Datos": [
        "Inteligencia Artificial"
    ],  # Sin vuelta a Cálculo I
    "Inteligencia Artificial": [],
    "Matemáticas Discretas": ["Estructuras de Datos"],
}

print("\nEJECUTANDO PRUEBA 2 (Sin ciclos):")
plan2 = PlanEstudios(listaAsignaturas, grafoSinCiclo)
plan2.verificarPlanEstudios()