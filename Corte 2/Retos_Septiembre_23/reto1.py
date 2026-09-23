def bubbleSort(arr):
    # Inicializa el contador de comparaciones
    comparacion = 0
    n = len(arr)
    
    for i in range(n):
        swappedFlag = False
        for j in range(0, n - i - 1):
            # Incrementa por cada comparación realizada
            comparacion += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swappedFlag = True
                
        # Si no hubo intercambios en esta pasada, la lista ya está ordenada
        if not swappedFlag:
            break
            
    return arr, comparacion


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