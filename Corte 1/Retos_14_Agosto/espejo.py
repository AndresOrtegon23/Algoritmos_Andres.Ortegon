def es_palindromo(arreglo):
    indice_inicio = 0
    indice_final = len(arreglo) - 1

    while indice_inicio < indice_final:
        if arreglo[indice_inicio] != arreglo[indice_final]:
            return False 
        
        indice_inicio += 1
        indice_final -= 1

    return True 

codigo_valido = [1, 4, 7, 4, 1]
codigo_invalido = [1, 4, 7, 8, 2]

print(f"¿El código {codigo_valido} es válido (palíndromo)? {es_palindromo(codigo_valido)}")
print(f"¿El código {codigo_invalido} es válido (palíndromo)? {es_palindromo(codigo_invalido)}")