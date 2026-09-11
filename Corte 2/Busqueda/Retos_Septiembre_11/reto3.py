def binaria_primera_aparicion(v, x):
    izq, der = 0, len(v) - 1
    resultado = -1  # Almacena el primer índice válido encontrado hasta el momento
    
    while izq <= der:
        medio = (izq + der) // 2
        
        if v[medio] == x:
            resultado = medio  # Registramos la posición hallada
            der = medio - 1    # Seguimos buscando hacia la izquierda por si hay más
        elif v[medio] < x:
            izq = medio + 1    # Descartar mitad izquierda
        else:
            der = medio - 1    # Descartar mitad derecha
            
    return resultado


datos_tres = [1, 3, 3, 3, 3, 5, 7, 7, 8, 9]
    
# El valor 3 aparece en los índices 1, 2, 3 y 4
idx_primero = binaria_primera_aparicion(datos_tres, 3)
print(f"Primera aparición de 3 en {datos_tres}: Índice = {idx_primero}")  # Salida: 1
    
# Elemento que no está en la lista
idx_no_esta = binaria_primera_aparicion(datos_tres, 4)
print(f"Primera aparición de 4 en {datos_tres}: Índice = {idx_no_esta}")  # Salida: -1