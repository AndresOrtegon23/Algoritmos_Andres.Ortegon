#include <iostream>
#include <string>

using namespace std;

// Paquete salud representado mediante namespace en camelCase
namespace salud {

    // Clase Persona
    class Persona {
    private:
        // Atributos privados
        string tipoDoc;    // Tipo de documento
        string documento;  // Número de documento
        string nombre;     // Nombre
        string apellido;   // Apellido
        double peso;       // Peso en kg
        double estatura;   // Estatura en m
        int edad;          // Edad en años
        char sexo;         // Sexo (M/F)

    public:
        // Método para solicitar los datos de la persona
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

        // Método para mostrar los datos ingresados
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

        // Método calcularImc modificado para retornar una cadena de texto según el caso
        string calcularImc() {
            // Validación para evitar división por cero
            if (estatura <= 0) {
                return "ERROR_ESTATURA";
            }

            // Cálculo del valor del IMC
            double pesoActual = peso / (estatura * estatura);

            // Evaluación según los rangos establecidos y retorno del estado correspondiente
            if (pesoActual < 20) {
                return "PESOBAJO";
            } else if (pesoActual >= 20 && pesoActual <= 25) {
                return "PESOIDEAL";
            } else {
                return "SOBREPESO";
            }
        }

        // Método para determinar si es mayor de edad
        void mayorEdad() {
            cout << "\n--- Condición de Edad ---" << endl;
            
            if (edad >= 18) {
                cout << "Es mayor de edad." << endl;
            } else {
                cout << "Es menor de edad." << endl;
            }
        }
    };

} // Fin del namespace salud

// Paquete principal en camelCase
namespace principal {

    // Clase inicio en camelCase
    class inicio {
    public:
        // Método de ejecución de la lógica principal
        void ejecutar() {
            // Instancia de la clase Persona
            salud::Persona persona1;

            // Solicitar y mostrar datos
            persona1.pedirDatos();
            persona1.mostrarPersona();

            // Capturar el valor retornado por el método calcularImc
            string resultadoImc = persona1.calcularImc();

            cout << "\n--- Diagnóstico de IMC ---" << endl;
            
            // Evaluación del retorno del método mediante un condicional
            if (resultadoImc == "PESOBAJO") {
                cout << "El peso está por debajo de lo ideal." << endl;
            } else if (resultadoImc == "PESOIDEAL") {
                cout << "El peso es ideal." << endl;
            } else if (resultadoImc == "SOBREPESO") {
                cout << "Tiene sobrepeso." << endl;
            } else {
                cout << "Error: La estatura debe ser mayor a 0 para calcular el IMC." << endl;
            }

            // Ejecución de la verificación de mayoría de edad
            persona1.mayorEdad();
        }
    };

} // Fin del namespace principal

// Función principal del programa
int main() {
    // Objeto en camelCase para iniciar la aplicación
    principal::inicio inicioApp;

    // Ejecución del programa
    inicioApp.ejecutar();

    return 0;
}