#include <iostream>

using namespace std;

int main() {
    // Arreglos para almacenar los nombres de los recursos y los días de la semana
    const char* recursos[3] = {"Computador", "Videobeam ", "Sala      "};
    const char* dias[5] = {"Lunes", "Martes", "Miercoles", "Jueves", "Viernes"};

    // Matriz de 3 filas (recursos) por 5 columnas (días) con los datos de préstamos
    int matriz[3][5] = {
        {4, 6, 2, 8, 5},
        {2, 3, 1, 4, 2},
        {5, 5, 4, 6, 8}
    };

    // Imprimir el encabezado de la tabla formateado con tabulaciones
    cout << "Recurso   \tLunes\tMartes\tMiercoles\tJueves\tViernes\tTotal\n";
    cout << "-----------------------------------------------------------------------\n";

    // Recorrer las filas de la matriz (recursos)
    for (int i = 0; i < 3; i++) {
        // Imprimir el nombre del recurso actual
        cout << recursos[i] << "\t";
        
        // Variable acumuladora para el uso total del recurso actual
        int sumaRecurso = 0;
        
        // Recorrer las columnas (días) del recurso actual
        for (int j = 0; j < 5; j++) {
            cout << matriz[i][j] << "\t";
            sumaRecurso += matriz[i][j]; // Sumar los préstamos del día al total del recurso
        }
        
        // Imprimir el total calculado para el recurso y salto de línea
        cout << sumaRecurso << "\n";
    }

    // Variables para rastrear el día con la mayor suma de préstamos
    int maxCarga = -1;
    const char* diaMasCargado = "";

    // Recorrer la matriz por columnas (días) para evaluar la carga de cada día
    for (int j = 0; j < 5; j++) {
        // Variable acumuladora para el total de préstamos del día actual
        int sumaDia = 0;
        
        // Sumar todos los recursos prestados en el día j
        for (int i = 0; i < 3; i++) {
            sumaDia += matriz[i][j];
        }
        
        // Actualizar el valor máximo si el día actual supera al mayor registrado
        if (sumaDia > maxCarga) {
            maxCarga = sumaDia;
            diaMasCargado = dias[j];
        }
    }

    // Imprimir los resultados del día más cargado
    cout << "\n-----------------------------------\n";
    cout << "El dia mas cargado fue el " << diaMasCargado 
         << " con un total de " << maxCarga << " prestamos.\n";

    return 0;
}