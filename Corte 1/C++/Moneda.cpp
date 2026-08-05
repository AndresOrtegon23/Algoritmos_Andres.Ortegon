#include <iostream>
#include <random> 

using namespace std;

int main() {
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> distrib(0, 1);

    int eleccionJugador = 0;
    
    cout << "Elige una opcion:" << endl;
    cout << "0 -> Sello" << endl;
    cout << "1 -> Cara" << endl;
    cout << "Ingresa tu eleccion: ";
    cin >> eleccionJugador;

    if (eleccionJugador != 0 && eleccionJugador != 1) {
        cout << "Esa opción no es válida. Debes elegir 0 o 1." << endl;
        return 1;
    }

    int resultadoMoneda = distrib(gen);
    
    if (resultadoMoneda == 1) {
        cout << "Cayó CARA" << endl;
    } 
    else {
        cout << "Cayó SELLO" << endl;
    }

    if (eleccionJugador == resultadoMoneda) {
        cout << "Ganaste, Acertaste en el lanzamiento." << endl;
    } 
    else {
        cout << "Perdiste esta vez, inténtalo de nuevo." << endl;
    }

    return 0;
}