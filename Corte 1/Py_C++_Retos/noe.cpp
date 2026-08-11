#include <iostream>

using namespace std;

int main() {
    double valor_compra;
    cout << "Ingrese el valor total de su compra: ";
    cin >> valor_compra;
    
    if (valor_compra > 50000) {
        cout << "\nFelicidades, Su compra es mayor a 50.000 y participa en el juego de las bolitas." << endl;
        cout << "Elija el color de la bolita que saco:" << endl;
        cout << "1. Roja" << endl;
        cout << "2. Azul" << endl;
        cout << "3. Amarilla" << endl;
        cout << "4. Blanca" << endl;
        
        int opcion;
        cout << "Ingrese el numero correspondiente a su bolita (1-4): ";
        cin >> opcion;
        
        double descuento = 0.0;
        string mensaje_premio = "";
        bool valido = true;
        
        if (opcion == 1) {
            descuento = valor_compra * 0.10;
            mensaje_premio = "Bolita Roja";
        } else if (opcion == 2) {
            descuento = valor_compra * 0.30;
            mensaje_premio = "Bolita Azul";
        } else if (opcion == 3) {
            descuento = valor_compra * 0.50;
            mensaje_premio = "Bolita Amarilla";
        } else if (opcion == 4) {
            descuento = valor_compra;
            mensaje_premio = "Bolita Blanca";
        } else {
            cout << "Opcion no valida. No se aplicara descuento." << endl;
            valido = false;
        }
        
        if (valido) {
            double valor_final = valor_compra - descuento;
            cout << "Bolita obtenida: " << mensaje_premio << endl;
            cout << "Valor inicial de la compra: $" << valor_compra << endl;
            cout << "Valor del descuento: $" << descuento << endl;
            cout << "Valor final a pagar: $" << valor_final << endl;
        }
    } else {
        cout << "\nLo sentimos, su compra fue de $" << valor_compra << " y debe ser mayor a 50.000 para participar." << endl;
        cout << "Valor final a pagar: $" << valor_compra << endl;
    }
    
    return 0;
}