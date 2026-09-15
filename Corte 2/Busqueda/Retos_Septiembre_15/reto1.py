def sumaLista(lista, indice=0):
    # Caso base: si el índice llega al final de la lista
    if indice == len(lista):
        return 0
    
    # Caso recursivo: el elemento actual + la llamada para el siguiente índice
    return lista[indice] + sumaLista(lista, indice + 1)

# Ejemplo :
mi_lista = [1, 2, 3, 4, 5]
resultado = sumaLista(mi_lista)
print(resultado)  # Output: 15
