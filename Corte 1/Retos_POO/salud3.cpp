#include <iostream>
#include <string>

using namespace std;

// Paquete salud representado mediante namespace en camelCase
namespace salud {

    // Clase Persona (inicia en mayúscula)
    class Persona {
    private:
        // Atributos privados
        string tipoDoc;
        string documento;
        string nombre;
        string apellido;
        double peso;
        double estatura;
        int edad;
        char sexo;

    public:
        // Métodos Getters y Setters para garantizar el encapsulamiento
        string getTipoDoc() const { return tipoDoc; }
        void setTipoDoc(const string& tDoc) { tipoDoc = tDoc; }

        string getDocumento() const { return documento; }
        void setDocumento(const string& doc) { documento = doc; }

        string getNombre() const { return nombre; }
        void setNombre(const string& nom) { nombre = nom; }

        string getApellido() const { return apellido; }
        void setApellido(const string& ape) { apellido = ape; }

        double getPeso() const { return peso; }
        void setPeso(double p) { peso = p; }

        double getEstatura() const { return estatura; }
        void setEstatura(double est) { estatura = est; }

        int getEdad() const { return edad; }
        void setEdad(int e) { edad = e; }

        char getSexo() const { return sexo; }
        void setSexo(char s) { sexo = s; }

        // Método para solicitar los datos de la persona
        void pedirDatos() {
            cout << "--- Ingrese los datos personales ---" << endl;
            
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

        // Método para calcular el IMC
        string calcularImc() {
            if (estatura <= 0) {
                return "ERROR_ESTATURA";
            }

            double pesoActual = peso / (estatura * estatura);

            if (pesoActual < 20) {
                return "PESOBAJO";
            } else if (pesoActual >= 20 && pesoActual <= 25) {
                return "PESOIDEAL";
            } else {
                return "SOBREPESO";
            }
        }

        // Método para evaluar la mayoría de edad
        void mayorEdad() {
            cout << "\n--- Condición de Edad ---" << endl;
            
            if (edad >= 18) {
                cout << "Es mayor de edad." << endl;
            } else {
                cout << "Es menor de edad." << endl;
            }
        }
    };

    // Subclase Empleado (inicia en mayúscula) que hereda de Persona
    class Empleado : public Persona {
    private:
        // Atributos propios en camelCase
        string cargo;
        double valorHora;
        double horasTrabajadas;
        string departamento;

    public:
        // Getters y Setters para los atributos propios
        string getCargo() const { return cargo; }
        void setCargo(const string& c) { cargo = c; }

        double getValorHora() const { return valorHora; }
        void setValorHora(double vHora) { valorHora = vHora; }

        double getHorasTrabajadas() const { return horasTrabajadas; }
        void setHorasTrabajadas(double hTrabajadas) { horasTrabajadas = hTrabajadas; }

        string getDepartamento() const { return departamento; }
        void setDepartamento(const string& dep) { departamento = dep; }

        // Método para solicitar los datos del empleado
        void pedirDatosEmpleado() {
            // Llama al método heredado para solicitar datos personales
            pedirDatos();

            cout << "\n--- Ingrese los datos laborales del Empleado ---" << endl;
            cout << "Cargo: ";
            cin >> cargo;

            cout << "Departamento: ";
            cin >> departamento;

            cout << "Valor por hora: ";
            cin >> valorHora;

            cout << "Horas trabajadas: ";
            cin >> horasTrabajadas;
        }

        // Método para calcular y mostrar honorarios
        void calcularHonorarios() {
            double valorTotal = valorHora * horasTrabajadas;
            double reteica = valorTotal * (0.966 / 100.0); // RETEICA de 0.966%
            double totalAPagar = valorTotal - reteica;

            cout << "\n--- Resumen de Honorarios ---" << endl;
            cout << "Tipo de Documento: " << getTipoDoc() << endl;
            cout << "Número de Documento: " << getDocumento() << endl;
            cout << "Nombres: " << getNombre() << endl;
            cout << "Apellidos: " << getApellido() << endl;
            cout << "Cargo: " << cargo << endl;
            cout << "Horas trabajadas: " << horasTrabajadas << endl;
            cout << "Valor por hora: " << valorHora << endl;
            cout << "Total a pagar (con RETEICA restado): " << totalAPagar << endl;
        }
    };

} // Fin del namespace salud

// Paquete principal en camelCase
namespace principal {

    // Clase Inicio (inicia en mayúscula)
    class Inicio {
    public:
        // Método de ejecución en camelCase
        void ejecutar() {
            // Instancia de la subclase Empleado
            salud::Empleado empleado1;

            // Solicitar datos completos del empleado
            empleado1.pedirDatosEmpleado();

            // Calcular y desplegar el total a pagar
            empleado1.calcularHonorarios();
        }
    };

} // Fin del namespace principal

// Función principal del programa
int main() {
    // Objeto de la clase Inicio para ejecutar la aplicación
    principal::Inicio inicioApp;

    // Ejecución del programa
    inicioApp.ejecutar();

    return 0;
}