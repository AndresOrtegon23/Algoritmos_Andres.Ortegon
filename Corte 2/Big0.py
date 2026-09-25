def insertionSort(arr):
    # Inicializa el contador de comparaciones
    comparacion = 0
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        # Desplaza elementos mayores hacia la derecha
        while j >= 0:
            comparacion += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
                
        arr[j + 1] = key
        
    return arr, comparacion

#Secuuencia de pasos de un algoritmo secuencial de ordenamiento por selección
#1. ¿Que es n en esa secuencia? = n es el total de elementos en la lista que se va a ordenar.
#2. ¿Cuantas veces se ejecuta el proceso si se duplican los datos? = Si se duplican los datos, el proceso se ejecuta el doble de veces, ya que n se incrementa y el bucle for depende de n.
#3. Dentro de esa secuencia se invoca otro proceso, ¿cuantos procesos se invocan? = En esta secuencia se invoca un proceso de búsqueda del mínimo en cada iteración del bucle externo, por lo que se invoca n veces.
#4. ¿Que tipo de estructura de datos se utliza? = En esta estructura de datos se utiliza una lista (array) para almacenar los elementos que se van a ordenar.