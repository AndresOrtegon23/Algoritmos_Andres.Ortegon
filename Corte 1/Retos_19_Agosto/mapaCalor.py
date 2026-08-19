def analizar_ocupacion_sala() -> None:
    
    # 1. Definición de Estructuras y Datos Iniciales
    
    # Etiquetas para las filas (días de la semana) con espaciado para alineación tabular
    dias = ["Lunes    ", "Martes   ", "Miércoles", "Jueves   ", "Viernes  "]
    
    # Etiquetas para las columnas (franjas horarias)
    franjas = ["F1", "F2", "F3", "F4", "F5", "F6"]

    # Matriz de ocupación (5 filas x 6 columnas) que almacena el número de personas
    matriz_ocupacion = [
        [2, 5, 8, 1, 3, 4],  # Lunes
        [1, 3, 2, 4, 1, 2],  # Martes
        [4, 6, 12, 2, 4, 3], # Miércoles
        [1, 2, 3, 1, 2, 1],  # Jueves
        [3, 4, 5, 2, 1, 3]   # Viernes
    ]

    # ---------------------------------------------------------
    # 2. Impresión Tabular de la Matriz
    # ---------------------------------------------------------
    print("--- MATRIZ DE OCUPACIÓN ---")
    print("          " + "  ".join(franjas))
    for i in range(len(dias)):
        fila = [str(x) for x in matriz_ocupacion[i]]
        print(f"{dias[i]}: {'  '.join(fila)}")
    print("-" * 30 + "\n")

    # ---------------------------------------------------------
    # 3. Análisis 1: Franja más congestionada de la semana
    # ---------------------------------------------------------
    max_personas = -1
    dia_max = ""
    franja_max = ""
    
    for i in range(len(matriz_ocupacion)):
        for j in range(len(matriz_ocupacion[i])):
            if matriz_ocupacion[i][j] > max_personas:
                max_personas = matriz_ocupacion[i][j]
                dia_max = dias[i]
                franja_max = franjas[j]

    print(f"1. Franja más congestionada: {franja_max} del {dia_max.strip()} ({max_personas} personas)")

    # ---------------------------------------------------------
    # 4. Análisis 2: Día con mayor ocupación total acumulada
    # ---------------------------------------------------------
    max_ocupacion_dia = -1
    dia_mas_ocupado = ""
    
    for i in range(len(matriz_ocupacion)):
        ocupacion_dia = sum(matriz_ocupacion[i])
        if ocupacion_dia > max_ocupacion_dia:
            max_ocupacion_dia = ocupacion_dia
            dia_mas_ocupado = dias[i]

    print(f"2. Día de mayor ocupación: {dia_mas_ocupado.strip()} (Total: {max_ocupacion_dia})")

    # ---------------------------------------------------------
    # 5. Análisis 3: Franjas con baja afluencia constante (< 5)
    # ---------------------------------------------------------
    franjas_tranquilas = []
    
    for j in range(len(franjas)):
        # Utiliza all() para verificar si todos los días cumplen la condición en la columna j
        if all(matriz_ocupacion[i][j] < 5 for i in range(len(matriz_ocupacion))):
            franjas_tranquilas.append(franjas[j])

    print(f"3. Franjas siempre < 5 personas: {', '.join(franjas_tranquilas)}")

# ==========================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ==========================================
if __name__ == "__main__":
    analizar_ocupacion_sala()