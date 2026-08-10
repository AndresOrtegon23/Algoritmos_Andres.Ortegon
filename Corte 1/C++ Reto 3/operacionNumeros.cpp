#include <iostream>
#include <cmath> 

using namespace std;

int main() {
    double num1, num2;

    // Entrada de datos
    cout << "Ingrese el primer numero: ";
    cin >> num1;
    cout << "Ingrese el segundo numero: ";
    cin >> num2;

    cout << "RESULTADOS";
    

    // Suma
    cout << "Suma: " << num1 + num2 << endl;

    // Resta
    cout << "Resta: " << num1 - num2 << endl;

    // Multiplicación
    cout << "Multiplicacion: " << num1 * num2 << endl;

    // División (validando división por cero)
    if (num2 != 0) {
        cout << "Division (num1 / num2): " << num1 / num2 << endl;
    } else {
        cout << "Division: No se puede dividir entre cero." << endl;
    }

    // Raíz cuadrada
    if (num1 >= 0) {
        cout << "Raiz cuadrada del primer numero: " << sqrt(num1) << endl;
    } else {
        cout << "Raiz cuadrada del primer numero: No tiene raiz real (numero negativo)." << endl;
    }

    if (num2 >= 0) {
        cout << "Raiz cuadrada del segundo numero: " << sqrt(num2) << endl;
    } else {
        cout << "Raiz cuadrada del segundo numero: No tiene raiz real (numero negativo)." << endl;
    }

    // Potenciación (num1 elevado a la potencia de num2)
    cout << "Potenciacion (num1 elevado a num2): " << pow(num1, num2) << endl;

    return 0;
}