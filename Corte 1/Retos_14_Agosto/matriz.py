def mostrar_matriz_distancias():
    # Matriz 4x4 que representa distancias (en km)
    # Índices:
    # 0 = Casa
    # 1 = Universidad
    # 2 = Gimnasio
    # 3 = Biblioteca
    
    matriz_distancias = [
        [0.0, 5.2, 2.1, 8.5],
        [5.2, 0.0, 4.0, 3.3],
        [2.1, 4.0, 0.0, 6.7],
        [8.5, 3.3, 6.7, 0.0]
    ]
    
    lugares = ["Casa", "Universidad", "Gimnasio", "Biblioteca"]
    
    print("    Matriz 4x4: Distancias entre locaciones (km)   \n")
    
    # Imprimir el encabezado con los nombres de las columnas
    print(f"{'':<14}", end="")
    for lugar in lugares:
        print(f"{lugar:<14}", end="")
    print("\n" + "-" * 70)
    

    indice_fila = 0
    for fila in matriz_distancias:
        print(f"{lugares[indice_fila]:<14}", end="")
        for distancia in fila:
            print(f"{distancia:<14.1f}", end="")
        print() # Salto de línea al terminar la fila
        indice_fila += 1

# Ejecutar la función
mostrar_matriz_distancias()