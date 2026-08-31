# ============================================================
#  Cívica Software  ·  TCK-4420  ·  Severidad P3
#  Sistema: RedAcopio  —  Reporte de ocupación
#  NO MODIFIQUE la seccion de datos ni el archivo de pruebas.
# ============================================================

# filas = puntos de acopio, columnas = dias de la semana
ocupacion = [
    [4, 2, 6, 1, 3, 0],
    [0, 5, 5, 2, 7, 1],
    [8, 1, 0, 4, 2, 6],
    [3, 3, 3, 0, 0, 5],
]

def total_por_punto(m):
    """Devuelve una lista con el total recogido por cada punto (fila)."""
    totales = []
    for fila in m:
        s = 0
        for v in fila:
            s += v
        totales.append(s)
    return totales


def total_por_dia(m):
    """Devuelve una lista con el total recogido cada dia (columna).
       BUG REPORTADO: entrega totales incorrectos."""
    totales = []
    
    for j in range(len(m[0])): # recorre columnas
        s = 0 # suma de la columna j
        for i in range(len(m)):   # recorre filas
            s += m[i][j] # suma el valor de la fila i, columna j
        totales.append(s)    # agrega el total de la columna j a la lista de totales
    return totales


def dia_mas_flojo(m):
    """Devuelve el indice del dia con MENOR recoleccion total.
       PENDIENTE: implementar."""

    totales = total_por_dia(m) # obtiene los totales por dia
    menorTotal = totales[0] # inicializa el menor total con el primer dia
    indiceMenor = 0 # inicializa el indice del dia con menor total con el primer dia
    
    for i in range(1, len(totales)):    # recorre los totales desde el segundo dia
        if totales[i] < menorTotal:  # si el total del dia i es menor que el menor total actual
            menorTotal = totales[i] # actualiza el menor total
            indiceMenor = i  # actualiza el indice del dia con menor total
            
    return indiceMenor # devuelve el indice del dia con menor recoleccion total
    

def puntos_inactivos(m):
    """Devuelve cuantos registros estan en 0 (el punto no opero ese dia).
       PENDIENTE: implementar."""
    inactivos = 0  # inicializa el contador de puntos inactivos
    for fila in m: # recorre cada fila (punto de acopio)
        for v in fila: # recorre cada valor en la fila (dias de la semana)
            if v == 0:  # si el valor es 0, significa que el punto no opero ese dia
                inactivos += 1    # incrementa el contador de puntos inactivos
    return inactivos # devuelve el total de puntos inactivos