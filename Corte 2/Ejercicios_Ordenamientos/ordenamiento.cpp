#include <iostream>
using namespace std;

int comparaciones = 0;
int intercambios = 0;


void resetContadores() {
    comparaciones = 0;
    intercambios = 0;
}

/* Bubble Sort */
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            comparaciones++;
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                intercambios++;
            }
        }
    }
}
/* Selection Sort */
void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        for (int j = i + 1; j < n; j++) {
            comparaciones++;
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }
        int temp = arr[minIdx];
        arr[minIdx] = arr[i];
        arr[i] = temp;
        intercambios++;
    }
}
/* Insertion Sort */
void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            comparaciones++;
            arr[j + 1] = arr[j];
            intercambios++;
            j--;
        }
        arr[j + 1] = key;
        intercambios++;
    }
}

int main() {
    int datosOrig[] = {64, 25, 12, 22, 11, 90, 45, 33};
    int n = sizeof(datosOrig) / sizeof(datosOrig[0]);
    int arr[8];

    // Probar Bubble Sort
    for(int i=0; i<n; i++) arr[i] = datosOrig[i];
    resetContadores();
    bubbleSort(arr, n);
    cout << "Bubble Sort -> Comparaciones: " << comparaciones << ", Intercambios: " << intercambios << endl;

    // Probar Selection Sort
    for(int i=0; i<n; i++) arr[i] = datosOrig[i];
    resetContadores();
    selectionSort(arr, n);
    cout << "Selection Sort -> Comparaciones: " << comparaciones << ", Intercambios: " << intercambios << endl;

    // Probar Insertion Sort
    for(int i=0; i<n; i++) arr[i] = datosOrig[i];
    resetContadores();
    insertionSort(arr, n);
    cout << "Insertion Sort -> Comparaciones: " << comparaciones << ", Intercambios: " << intercambios << endl;

    return 0;
}