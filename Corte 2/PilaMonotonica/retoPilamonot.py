def dias_hasta_calor_mayor(temperaturas):
    n = len(temperaturas)
    res = [0] * n  # Inicializamos el resultado con ceros
    pila = []  # Pila para almacenar los índices de los días

    for i in range(n):
        while pila and temperaturas[i] > temperaturas[pila[-1]]:
            indice = pila.pop()
            res[indice] = i - indice  # Calculamos la diferencia de días
        pila.append(i)  # Agregamos el índice del día actual a la pila
    return res

print(dias_hasta_calor_mayor([73, 74, 75, 71, 69, 72, 76, 73]))