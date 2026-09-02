# ============================================================
#  Cívica Software  ·  TCK-5510  ·  Severidad P3
#  Sistema: RedAcopio  —  Mapa de cobertura de rutas
#  NO MODIFIQUE la matriz de datos ni el archivo de pruebas.
# ============================================================

# filas = rutas del camion, columnas = zonas del barrio
# cada celda = kilos recogidos por esa ruta en esa zona
cobertura = [
    [5, 0, 3, 0, 2, 4, 0],
    [0, 0, 7, 0, 1, 0, 6],
    [2, 0, 0, 0, 4, 3, 1],
    [0, 0, 5, 0, 0, 8, 2],
]

def total_por_ruta(m):
    """Devuelve una lista con el total recogido por cada ruta (fila)."""
    totales = []
    for fila in m:
        s = 0
        for v in fila:
            s += v
        totales.append(s)
    return totales


def cobertura_por_zona(m):
    """Devuelve una lista con el total recogido en cada zona (columna).
       BUG REPORTADO: la ultima zona nunca aparece en el informe."""
    totales = []
    for j in range(len(m[0])):   # Recorre cada columna
        s = 0      # Suma los valores de la columna j
        for i in range(len(m)):    #Recorre cada fila
            s += m[i][j]   # Suma el valor de la celda (i,j) a la suma de la columna
        totales.append(s)   # Agrega la suma de la columna j a la lista de totales
    return totales  # Devuelve la lista de totales por zona


def ruta_mas_productiva(m):
    """Devuelve el INDICE de la ruta que mas kilos recogio en total.
       PENDIENTE: implementar."""
    totales = total_por_ruta(m)     # Calcula el total de kilos recogidos por cada ruta
    maxKilos = totales[0]     # Inicializa la variable maxKilos con el total de kilos recogidos por la primera ruta
    rutaMax = 0     #Se hace el contador de la ruta que mas kilos recogio
    for i in range(len(totales)):       # Recorre la lista de totales por ruta
        if totales[i] > maxKilos:       # Si el total de kilos recogidos por la ruta i es mayor que maxKilos, actualiza maxKilos y rutaMax
            maxKilos = totales[i]       # Se actualiza maxKilos con el total de kilos recogidos por la ruta i
            rutaMax = i     # Se actualiza rutaMax con el indice de la ruta i
    return rutaMax      # Devuelve el indice de la ruta que mas kilos recogio


def zonas_sin_cubrir(m):
    """Devuelve cuantas zonas (columnas) quedaron COMPLETAMENTE en cero,
       es decir, ninguna ruta recogio nada alli.
       PENDIENTE: implementar."""
    zonas_sin_cobertura = 0     #Inicializa el contador de zoans sin cobertura
    for j in range(len(m[0])):      # Recorre cada columna
        cubierto = False        #Inicializa la variable cubierto en False
        for i in range(len(m)):     # Recorre cada fila
            if m[i][j] > 0:     #Si la celda es mayor que cero, entonces la zona esta cubierta
                cubierto = True     # Marca la zona como cubierta
                break       #Si encuentra una ruta, sale del bucle de filas
        if not cubierto:        
            zonas_sin_cobertura += 1        # Si es cubierta, se incremeta el contador
    return zonas_sin_cobertura          #Devuelve el numero de zonas sin cobertura
