#include <iostream>
using namespace std;

int main() {
    int lecturas[] = {10, 13, 3, 8, 9};
    int n = 5;

    int maximo = lecturas[0];
    double suma = 0;

    for (int i = 0; i < n; i++) {
        if (lecturas[i] > maximo) {
            maximo = lecturas[i];
        }
        suma += lecturas[i];
    }

    // Calcular el promedio
    double promedio = suma / n;

    // Mostrar los resultados
    cout << "Máximo: " << maximo << endl;
    cout << "Promedio: " << promedio << endl;

    return 0;
}