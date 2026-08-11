#include <iostream>

using namespace std;

int main() {

    int dado1, dado2;
    
    cout << "Ingresa el valor del primer dado (1-6): ";
    cin >> dado1;
    
    cout << "Ingresa el valor del segundo dado (1-6): ";
    cin >> dado2;
    
    int suma = dado1 + dado2;
    
    cout << "\nDado 1: " << dado1 << endl;
    cout << "Dado 2: " << dado2 << endl;
    cout << "Suma total: " << suma << endl;
    
    if (suma == 2 || suma == 3 || suma == 7 || suma == 11 || suma == 12) {
        cout << "Resultado: HAS GANADO " << endl;
    } else {
        cout << "Resultado: HAS PERDIDO." << endl;
    }
    
    return 0;
}