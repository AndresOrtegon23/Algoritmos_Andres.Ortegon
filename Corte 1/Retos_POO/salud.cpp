#include <iostream>
#include <string>

using namespace std;

// Representación del paquete Salud utilizando un namespace de C++
namespace Salud {

    // Declaración de la clase Persona
    class Persona {
    private:
        // Atributos privados para almacenar la información de la persona
        string tipoDoc;    // Tipo de documento de identidad
        string documento;  // Número de documento
        string nombre;     // Nombre de la persona
        string apellido;   // Apellido de la persona
        double peso;       // Peso expresado en kilogramos (kg)
        double estatura;   // Estatura expresada en metros (m)
        int edad;          // Edad en años
        char sexo;         // Sexo de la persona (ej: 'M' o 'F')

    public:
        // Método pedirDatos: Solicita al usuario los datos por consola y los asigna a los atributos
        void pedirDatos() {
            cout << "--- Ingrese los datos de la persona ---" << endl;
            
            cout << "Tipo de documento: ";
            cin >> tipoDoc;
            
            cout << "Número de documento: ";
            cin >> documento;
            
            cout << "Nombre: ";
            cin >> nombre;
            
            cout << "Apellido: ";
            cin >> apellido;
            
            cout << "Edad: ";
            cin >> edad;
            
            cout << "Sexo (M/F): ";
            cin >> sexo;
            
            cout << "Peso (en kg): ";
            cin >> peso;
            
            cout << "Estatura (en metros, ej: 1.75): ";
            cin >> estatura;
        }

        // Método mostrarPersona: Imprime en consola todos los datos almacenados en los atributos
        void mostrarPersona() {
            cout << "\n--- Datos de la Persona ---" << endl;
            cout << "Tipo de Documento: " << tipoDoc << endl;
            cout << "Documento: " << documento << endl;
            cout << "Nombre completo: " << nombre << " " << apellido << endl;
            cout << "Edad: " << edad << " años" << endl;
            cout << "Sexo: " << sexo << endl;
            cout << "Peso: " << peso << " kg" << endl;
            cout << "Estatura: " << estatura << " m" << endl;
        }

        // Método calcularImc: Aplica la fórmula peso / (estatura^2) e informa el estado
        void calcularImc() {
            // Validación para evitar división por cero en caso de estatura inválida
            if (estatura <= 0) {
                cout << "\nError: La estatura debe ser mayor a 0 para calcular el IMC." << endl;
                return;
            }

            // Cálculo del valor del IMC actual
            double pesoActual = peso / (estatura * estatura);

            cout << "\n--- Diagnóstico de IMC ---" << endl;
            
            // Evaluación del resultado según los rangos establecidos
            if (pesoActual < 20) {
                // Caso 1: Resultado menor a 20
                cout << "El peso está por debajo de lo ideal." << endl;
            } else if (pesoActual >= 20 && pesoActual <= 25) {
                // Caso 2: Resultado entre 20 y 25 inclusive
                cout << "El peso es ideal." << endl;
            } else {
                // Caso 3: Resultado mayor a 25
                cout << "Tiene sobrepeso." << endl;
            }
        }

        // Método mayorEdad: Evalúa la edad ingresada y determina si es mayor o menor de edad
        void mayorEdad() {
            cout << "\n--- Condición de Edad ---" << endl;
            
            // Verificación si la edad es mayor o igual al umbral legal de 18 años
            if (edad >= 18) {
                cout << "Es mayor de edad." << endl;
            } else {
                cout << "Es menor de edad." << endl;
            }
        }
    };

} // Fin del namespace Salud

// Representación del paquete Principal utilizando un namespace
namespace Principal {

    // Declaración de la clase Inicio
    class Inicio {
    public:
        // Método principal de ejecución de la clase Inicio
        void ejecutar() {
            // Definición del objeto para la clase Persona (considerando modificadores de acceso)
            Salud::Persona persona1;

            // Ejecución de los métodos definidos en la estructura
            persona1.pedirDatos();      // Solicitar datos al usuario
            persona1.mostrarPersona();  // Imprimir los datos ingresados
            persona1.calcularImc();     // Calcular el IMC y mostrar diagnóstico
            persona1.mayorEdad();       // Determinar si es mayor de edad
        }
    };

} // Fin del namespace Principal

// Función principal del programa
int main() {
    // Creación del objeto de la clase Inicio dentro del paquete Principal
    Principal::Inicio inicioApp;

    // Ejecución de la lógica principal
    inicioApp.ejecutar();

    return 0; // Finalización exitosa del programa
}