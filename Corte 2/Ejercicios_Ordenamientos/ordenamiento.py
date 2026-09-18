# comparo dos vecinos si estan al reves los intercambio y repito el proceso 
# hast que nadie mas se mueva bubble sort

comparaciones = 0
intercambios = 0

def bubble_sort(arr):
    global comparaciones, intercambios
    comparaciones = 0
    intercambios = 0
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparaciones += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambios += 1
                swapped = True
        if not swapped:
            break
    return arr
#buscar el más pequeño y ponerlo al 
# principio selection sort

def selection_sort(arr):
    global comparaciones, intercambios
    comparaciones = 0
    intercambios = 0
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparaciones += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        intercambios += 1
    return arr
# tomo el segundo y lo inserto donde va 
# respecto al primero insertion sort

def insertion_sort(arr):
    global comparaciones, intercambios
    comparaciones = 0
    intercambios = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            comparaciones += 1
        arr[j + 1] = key
        intercambios += 1
    return arr

# datos: [64, 25, 12, 22, 11, 90, 45, 33]

Lista = [64, 25, 12, 22, 11, 90, 45, 33]


print("Lista original:", Lista)
print("Lista ordenada (Bubble Sort):", bubble_sort(Lista.copy()))
print("Numero de comparaciones en bubble sort: ", comparaciones)
print("Numero de intercambios en bubble sort: ", intercambios)

print()

print("Lista ordenada (Selection Sort):", selection_sort(Lista.copy()))
print("Numero de comparaciones en selection sort: ", comparaciones)
print("Numero de intercambios en selection sort: ", intercambios)

print()

print("Lista ordenada (Insertion Sort):", insertion_sort(Lista.copy()))
print("Numero de comparaciones en insertion sort: ", comparaciones)
print("Numero de intercambios en insertion sort: ", intercambios)