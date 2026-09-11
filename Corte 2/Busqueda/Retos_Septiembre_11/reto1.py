def binaria_rec(v, x, izq=0, der=None):
    # Inicialización del límite superior en la primera llamada externa
    if der is None:
        der = len(v) - 1
    
    # el rango es inválido, el elemento no se encuentra en el arreglo
    if izq > der:
        return -1
    
    # Cálculo del punto medio
    medio = (izq + der) // 2
    
    # elemento encontrado
    if v[medio] == x:
        return medio
    
    # descartar la mitad izquierda
    elif v[medio] < x:
        return binaria_rec(v, x, medio + 1, der)
    
    # descartar la mitad derecha
    else:
        return binaria_rec(v, x, izq, medio - 1)

datos_uno = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    
idx_encontrado = binaria_rec(datos_uno, 23)
print(f"Búsqueda de 23 en {datos_uno}: Índice = {idx_encontrado}")  # Salida: 5
    
idx_ausente = binaria_rec(datos_uno, 15)
print(f"Búsqueda de 15 en {datos_uno}: Índice = {idx_ausente}")      # Salida: -1
print()