#include <iostream>
#include <random> 

using namespace std;

int main() {
    
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> distrib(1, 3); 
    
    int eleccionJugador = 0;
    
    cout << "Elige una opcion:" << endl;
    cout << "1 -> Piedra" << endl;
    cout << "2 -> Papel" << endl;
    cout << "3 -> Tijera" << endl;
    cout << "Ingresa tu eleccion (1, 2 o 3): ";
    cin >> eleccionJugador;

    
    if (eleccionJugador < 1 || eleccionJugador > 3) {
        cout << "Esa opción no es válida. Debes elegir 1, 2 o 3." << endl;
        return 1;
    }

    
    int eleccionMaquina = distrib(gen);

    cout << "Tú elegiste: ";
    if (eleccionJugador == 1) {
        cout << "Piedra" << endl;
    } 
    else if (eleccionJugador == 2) {
        cout << "Papel" << endl;
    } 
    else {
        cout << "Tijera" << endl;
    }

    cout << "La máquina eligió: ";
    if (eleccionMaquina == 1) {
        cout << "Piedra" << endl;
    } else if (eleccionMaquina == 2) {
        cout << "Papel" << endl;
    } else {
        cout << "Tijera" << endl;
    }

    if (eleccionJugador == eleccionMaquina) {
        cout << "Empate Ambos eligieron lo mismo." << endl;
    } else if ((eleccionJugador == 1 && eleccionMaquina == 3) || 
               (eleccionJugador == 2 && eleccionMaquina == 1) || 
               (eleccionJugador == 3 && eleccionMaquina == 2)) { 
        cout << "¡Ganaste! " << endl;
    } else {
        cout << "Perdiste, la máquina te ganó esta vez." << endl;
    }

    return 0;
}