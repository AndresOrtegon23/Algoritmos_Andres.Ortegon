#include <iostream>

using namespace std;

// Estructura para almacenar las metricas de rendimiento de los algoritmos
struct Metricas {
    long long comparaciones = 0; // Contador de cuantas veces se comparan elementos
    long long intercambios = 0;   // Contador de cuantos movimientos o intercambios se realizan
};

// Funcion auxiliar para intercambiar el valor de dos variables enteras por referencia
void intercambiar(int& a, int& b) {
    int temp = a; // Guarda temporalmente el valor de a
    a = b;        // Asigna el valor de b a a
    b = temp;     // Asigna el valor guardado de a a b
}

//  Merge Sort
// Funcion para fusionar dos mitades ordenadas utilizando un arreglo auxiliar dinamico
void mezclar(int arreglo[], int izquierda, int medio, int derecha, Metricas& m) {
    int n1 = medio - izquierda + 1; // Tamaño de la mitad izquierda
    int n2 = derecha - medio;       // Tamaño de la mitad derecha

    int* mitadIzquierda = new int[n1]; // Arreglo dinamico para la mitad izquierda
    int* mitadDerecha = new int[n2];   // Arreglo dinamico para la mitad derecha

    // Copiar los datos del arreglo principal a las mitades auxiliares
    for (int i = 0; i < n1; i++) mitadIzquierda[i] = arreglo[izquierda + i];
    for (int j = 0; j < n2; j++) mitadDerecha[j] = arreglo[medio + 1 + j];

    int i = 0; // Indice inicial para recorrer la mitad izquierda
    int j = 0; // Indice inicial para recorrer la mitad derecha
    int k = izquierda; // Indice inicial para colocar los elementos ordenados en el arreglo principal

    // Comparar y fusionar elementos de ambas mitades en orden ascendente
    while (i < n1 && j < n2) {
        m.comparaciones++; // Se incrementa el contador de comparaciones
        if (mitadIzquierda[i] <= mitadDerecha[j]) {
            arreglo[k] = mitadIzquierda[i];
            i++;
        } else {
            arreglo[k] = mitadDerecha[j];
            j++;
        }
        m.intercambios++; // Se cuenta la asignacion/escritura como operacion de movimiento
        k++;
    }

    // Copiar los elementos restantes de la mitad izquierda, si los hay
    while (i < n1) { 
        arreglo[k] = mitadIzquierda[i]; 
        i++; 
        k++; 
    }

    // Copiar los elementos restantes de la mitad derecha, si los hay
    while (j < n2) { 
        arreglo[k] = mitadDerecha[j]; 
        j++; 
        k++; 
    }

    // Liberar la memoria dinamica de las mitades auxiliares para evitar fugas de memoria
    delete[] mitadIzquierda;
    delete[] mitadDerecha;
}

// Funcion recursiva principal de Merge Sort que divide el arreglo en mitades
void mergeSort(int arreglo[], int izquierda, int derecha, Metricas& m) {
    if (izquierda < derecha) {
        int medio = izquierda + (derecha - izquierda) / 2; // Calcula el punto medio exacto
        mergeSort(arreglo, izquierda, medio, m);           // Ordena recursivamente la mitad izquierda
        mergeSort(arreglo, medio + 1, derecha, m);       // Ordena recursivamente la mitad derecha
        mezclar(arreglo, izquierda, medio, derecha, m);    // Mezcla ambas mitades ya ordenadas
    }
}

//  Quicksort 
// Funcion para particionar el arreglo tomando el ultimo elemento como pivote
int particionar(int arreglo[], int bajo, int alto, Metricas& m) {
    int pivote = arreglo[alto]; // Selecciona el ultimo elemento como el pivote actual
    int i = (bajo - 1);         // Indice del limite para los elementos menores al pivote

    // Recorrer el rango para reorganizar los elementos menores a la izquierda
    for (int j = bajo; j <= alto - 1; j++) {
        m.comparaciones++; // Cuenta la comparacion del elemento actual con el pivote
        if (arreglo[j] < pivote) {
            i++;                           // Avanza el limite de los menores
            intercambiar(arreglo[i], arreglo[j]); // Intercambia los elementos fuera de posicion
            m.intercambios++;              // Cuenta el intercambio realizado
        }
    }
    intercambiar(arreglo[i + 1], arreglo[alto]); // Coloca el pivote en su posicion final correcta
    m.intercambios++;                             // Cuenta el intercambio del pivote
    return (i + 1);                               // Retorna el indice donde se ubica el pivote
}

// Funcion recursiva para ordenar el arreglo mediante Quicksort
void quickSort(int arreglo[], int bajo, int alto, Metricas& m) {
    if (bajo < alto) {
        int indicePivote = particionar(arreglo, bajo, alto, m); // Obtiene la particion del pivote
        quickSort(arreglo, bajo, indicePivote - 1, m);          // Ordena la sublista izquierda
        quickSort(arreglo, indicePivote + 1, alto, m);        // Ordena la sublista derecha
    }
}

// Heapsort
// Funcion para mantener la propiedad de Max-Heap en un arbol binario representado como arreglo
void convertirMaxHeap(int arreglo[], int n, int i, Metricas& m) {
    int mayor = i;             // Inicializa la raiz como el elemento mayor
    int izquierdo = 2 * i + 1; // Calcula la posicion del hijo izquierdo
    int derecho = 2 * i + 2;   // Calcula la posicion del hijo derecho

    // Compara el nodo raiz con el hijo izquierdo si este existe dentro del limite
    if (izquierdo < n) {
        m.comparaciones++; // Cuenta la comparacion con el hijo izquierdo
        if (arreglo[izquierdo] > arreglo[mayor]) mayor = izquierdo;
    }

    // Compara el nodo actual con el hijo derecho si este existe dentro del limite
    if (derecho < n) {
        m.comparaciones++; // Cuenta la comparacion con el hijo derecho
        if (arreglo[derecho] > arreglo[mayor]) mayor = derecho;
    }

    // Si la raiz no es el mayor, realiza un intercambio y propaga el ajuste recursivamente
    if (mayor != i) {
        intercambiar(arreglo[i], arreglo[mayor]); // Intercambia el valor menor con el mayor encontrado
        m.intercambios++;                          // Cuenta el intercambio
        convertirMaxHeap(arreglo, n, mayor, m);    // Llamada recursiva para asegurar el heap en el subarbol
    }
}

// Funcion principal que ejecuta el ordenamiento por monticulos (Heapsort)
void heapSort(int arreglo[], int n, Metricas& m) {
    // Paso 1: Construir un monticulo maximo inicial rearrancando desde el ultimo nodo padre
    for (int i = n / 2 - 1; i >= 0; i--)
        convertirMaxHeap(arreglo, n, i, m);

    // Paso 2: Extraer elementos uno por uno desde el monticulo maximizado
    for (int i = n - 1; i > 0; i--) {
        intercambiar(arreglo[0], arreglo[i]); // Mueve la raiz actual (el valor maximo) al final del arreglo
        m.intercambios++;                      // Cuenta el intercambio
        convertirMaxHeap(arreglo, i, 0, m);    // Restaura la propiedad max-heap en el monticulo reducido
    }
}

// Bucket Sort
// Funcion para ordenar un conjunto distribuyendo los elementos en cubetas dinamicas
void bucketSort(int arreglo[], int n, Metricas& m) {
    if (n <= 0) return; // Validación de seguridad para arreglos vacios

    int valorMinimo = arreglo[0]; // Inicializa el valor minimo con el primer elemento
    int valorMaximo = arreglo[0]; // Inicializa el valor maximo con el primer elemento
    for (int i = 1; i < n; i++) {
        if (arreglo[i] < valorMinimo) valorMinimo = arreglo[i];
        if (arreglo[i] > valorMaximo) valorMaximo = arreglo[i];
    }

    if (valorMinimo == valorMaximo) return; // Si todos los elementos son identicos, no requiere orden

    int numeroCubetas = n;                  // Cantidad de cubetas igual al numero de elementos
    int** cubetas = new int*[numeroCubetas]; // Arreglo dinamico de punteros para las cubetas
    int* tamanioCubetas = new int[numeroCubetas](); // Almacena el conteo actual de elementos por cubeta
    int* capacidadCubetas = new int[numeroCubetas]; // Almacena la capacidad maxima asignada por cubeta

    // Inicializar cada cubeta con una capacidad dinamica base de 10 elementos
    for (int i = 0; i < numeroCubetas; i++) {
        capacidadCubetas[i] = 10;
        cubetas[i] = new int[capacidadCubetas[i]];
    }

    // Distribuir cada elemento del arreglo principal en su cubeta correspondiente mediante calculo lineal
    for (int i = 0; i < n; i++) {
        int indiceCubeta = numeroCubetas * (arreglo[i] - valorMinimo) / (valorMaximo - valorMinimo + 1);
        if (indiceCubeta >= numeroCubetas) indiceCubeta = numeroCubetas - 1;
        
        // Verificar si la cubeta supero su capacidad para redimensionarla duplicando su espacio
        if (tamanioCubetas[indiceCubeta] >= capacidadCubetas[indiceCubeta]) {
            capacidadCubetas[indiceCubeta] *= 2;
            int* nuevoBucket = new int[capacidadCubetas[indiceCubeta]];
            for (int j = 0; j < tamanioCubetas[indiceCubeta]; j++) {
                nuevoBucket[j] = cubetas[indiceCubeta][j];
            }
            delete[] cubetas[indiceCubeta];
            cubetas[indiceCubeta] = nuevoBucket;
        }

        cubetas[indiceCubeta][tamanioCubetas[indiceCubeta]++] = arreglo[i];
    }

    // Ordenar cada cubeta de manera individual utilizando el algoritmo de insercion directa
    for (int i = 0; i < numeroCubetas; i++) {
        for (int j = 1; j < tamanioCubetas[i]; j++) {
            int clave = cubetas[i][j];
            int k = j - 1;
            while (k >= 0) {
                m.comparaciones++; // Cuenta la comparacion interna dentro de la cubeta
                if (cubetas[i][k] > clave) {
                    cubetas[i][k + 1] = cubetas[i][k];
                    m.intercambios++; // Cuenta el desplazamiento de elementos en la cubeta
                    k--;
                } else {
                    break;
                }
            }
            cubetas[i][k + 1] = clave;
        }
    }

    // Recopilar los elementos ordenados de todas las cubetas y devolverlos al arreglo principal
    int indiceArreglo = 0;
    for (int i = 0; i < numeroCubetas; i++) {
        for (int j = 0; j < tamanioCubetas[i]; j++) {
            arreglo[indiceArreglo++] = cubetas[i][j];
        }
        delete[] cubetas[i]; // Libera la memoria dinamica asignada a cada cubeta individual
    }

    // Liberar los arreglos auxiliares de control de memoria de las cubetas
    delete[] cubetas;
    delete[] tamanioCubetas;
    delete[] capacidadCubetas;
}

// Funciones de apoyo para operaciones auxiliares de pruebas
void copiarArreglo(const int origen[], int destino[], int n) {
    for (int i = 0; i < n; i++) {
        destino[i] = origen[i]; // Copia los datos elemento por elemento
    }
}

void imprimirArreglo(const int arreglo[], int n) {
    cout << "[ ";
    for (int i = 0; i < n; i++) cout << arreglo[i] << " "; // Imprime cada elemento formateado
    cout << "]";
}

// Funcion principal para ejecutar y mostrar las pruebas de todos los algoritmos
int main() {
    const int n = 8; // Define el tamaño estatico del arreglo de prueba
    int datosPruebaBase[n] = {64, 25, 12, 22, 11, 90, 45, 33}; // Arreglo base desordenado
    int datos[n]; // Arreglo mutable de trabajo para cada ejecucion

    cout << " PRUEBAS DE ORDENAMIENTO EN C++ " << endl;

    // Ejecucion 1: Prueba del algoritmo Merge Sort
    {
        copiarArreglo(datosPruebaBase, datos, n); // Restaura el arreglo original
        Metricas m;                               // Inicializa las metricas de conteo
        mergeSort(datos, 0, n - 1, m);             // Ejecuta la ordenacion

        cout << "Merge Sort -> Ordenado: ";
        imprimirArreglo(datos, n);                // Muestra el resultado final
        cout << " | Comp: " << m.comparaciones << " | Intercambios: " << m.intercambios << endl;
    }

    // Ejecucion 2: Prueba del algoritmo Quick Sort
    {
        copiarArreglo(datosPruebaBase, datos, n); // Restaura el arreglo original
        Metricas m;                               // Inicializa las metricas de conteo
        quickSort(datos, 0, n - 1, m);             // Ejecuta la ordenacion

        cout << "Quick Sort -> Ordenado: ";
        imprimirArreglo(datos, n);                // Muestra el resultado final
        cout << " | Comp: " << m.comparaciones << " | Intercambios: " << m.intercambios << endl;
    }

    // Ejecucion 3: Prueba del algoritmo Heap Sort
    {
        copiarArreglo(datosPruebaBase, datos, n); // Restaura el arreglo original
        Metricas m;                               // Inicializa las metricas de conteo
        heapSort(datos, n, m);                    // Ejecuta la ordenacion

        cout << "Heap Sort  -> Ordenado: ";
        imprimirArreglo(datos, n);                // Muestra el resultado final
        cout << " | Comp: " << m.comparaciones << " | Intercambios: " << m.intercambios << endl;
    }

    // Ejecucion 4: Prueba del algoritmo Bucket Sort
    {
        copiarArreglo(datosPruebaBase, datos, n); // Restaura el arreglo original
        Metricas m;                               // Inicializa las metricas de conteo
        bucketSort(datos, n, m);                  // Ejecuta la ordenacion

        cout << "Bucket Sort-> Ordenado: ";
        imprimirArreglo(datos, n);                // Muestra el resultado final
        cout << " | Comp: " << m.comparaciones << " | Intercambios: " << m.intercambios << endl;
    }

    return 0; // Termina la ejecucion de forma exitosa
}