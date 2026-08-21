def analizar_mensaje_usuario(mensaje):
    print(f"Mensaje recibido: '{mensaje}'\n")

    # 1. .split() - Divide la frase completa en una lista de palabras individuales
    palabras = mensaje.split()
    print(f"1. .split() - Lista de palabras:\n{palabras}\n")

    # 2. len() - El equivalente nativo a '.size' para contar el tamaño de la lista
    total_palabras = len(palabras)
    print(f"2. len() - El tamaño total de la lista es: {total_palabras} elementos\n")

    # 3. .append() - Añade un mensaje de aliento al final de nuestra lista
    palabras.append("perfecto para")
    palabras.append("salir y jugar")
    print(f"3. .append() - Añadido al final:\n{palabras}\n")

    # --- Otras funciones muy comunes y complementarias ---

    # 4. .extend() - Añade múltiples elementos a la vez (como otra lista completa)
    palabras.extend(["diviertete", "mucho", "hoy"])
    print(f"4. .extend() - Añadiendo varios elementos:\n{palabras}\n")

    # 5. .insert() - Inserta un elemento en una posición específica (en este caso, al inicio, índice 0)
    palabras.insert(0, "¡Hola!")
    print(f"5. .insert() - Agregado al inicio:\n{palabras}\n")

    # 6. .pop() - Remueve y saca de la lista un elemento (por defecto el último, o indicando el índice)
    despedida = palabras.pop()
    print(f"6. .pop() - Elemento extraído del final: '{despedida}'")
    print(f"   Lista actual tras el .pop():\n{palabras}\n")

    # 7. .join() - Lo opuesto a .split(): vuelve a unir todas las palabras de la lista en un solo texto fluido
    mensaje_final = " ".join(palabras)
    
    return mensaje_final

# Ejecución del programa con un mensaje dirigido al usuario
texto_usuario = "Hoy es un dia caluroso y soleado,"
resultado_final = analizar_mensaje_usuario(texto_usuario)

print(f"--- Resultado Final ---")
print(f"Mensaje reconstruido: '{resultado_final}'")