# Función recursiva para invertir una cadena sin usar slicing
def invertirCadena(textoCadena, indiceActual=0):
    # Caso base: si el índice llega al final de la cadena, devolvemos una cadena vacía
    if indiceActual == len(textoCadena):
        return ""
    
    # Caso recursivo: llamamos a la función con el siguiente índice 
    # y le sumamos el carácter actual al final cuando se van desapilando
    return invertirCadena(textoCadena, indiceActual + 1) + textoCadena[indiceActual]

# Ejemplo de uso:
miTexto = "hola como estas"
resultadoInvertido = invertirCadena(miTexto)
print(resultadoInvertido)  # Output: aloh