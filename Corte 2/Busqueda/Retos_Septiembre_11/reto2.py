def posicion_insercion(v, x):
    izq, der = 0, len(v) - 1
    
    while izq <= der:
        medio = (izq + der) // 2
        
        if v[medio] == x:
            return medio  # El elemento ya existe
        elif v[medio] < x:
            izq = medio + 1  # Descartar mitad izquierda
        else:
            der = medio - 1  # Descartar mitad derecha
            
    # Al finalizar el ciclo sin éxito, 'izq' conserva la posición exacta de inserción
    return izq

datos_dos = [10, 20, 30, 40, 50]
    
# Inserción en el medio
pos_medio = posicion_insercion(datos_dos, 25)
print(f"El 25 debería ir en la posición: {pos_medio}")  # Salida: 2
    
# Inserción al inicio
pos_inicio = posicion_insercion(datos_dos, 5)
print(f"El 5 debería ir en la posición: {pos_inicio}")   # Salida: 0
    
# Inserción al final
pos_final = posicion_insercion(datos_dos, 60)
print(f"El 60 debería ir en la posición: {pos_final}")  # Salida: 5

# Ejemplo de uso práctico: Insertar un elemento sin romper el orden
nuevo_elemento = 25
pos = posicion_insercion(datos_dos, nuevo_elemento)
datos_dos.insert(pos, nuevo_elemento)
print(f"Vector después de insertar {nuevo_elemento}: {datos_dos}")
print()