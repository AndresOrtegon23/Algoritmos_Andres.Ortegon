#include <iostream>
#include <string>

using namespace std;

// Namespace representativo del módulo de gestión de biblioteca/recursos
namespace gestionRecursos {

    // Clase Usuario: Administra los datos del usuario y su estado de sanciones
    class Usuario {
    private:
        // Atributos privados de la clase
        string nombre;          // Nombre completo del usuario
        string documento;       // Documento de identidad del usuario
        bool tieneSanciones;    // Estado que indica si el usuario posee sanciones activas

    public:
        // Constructor parametrizado para inicializar un usuario
        Usuario(string n, string d);

        // Método constante para verificar si el usuario cumple las condiciones para solicitar un préstamo
        bool puedeSolicitar() const;
    };

    // Clase Recurso: Administra los elementos o materiales prestables del sistema
    class Recurso {
    private:
        // Atributos privados de la clase
        string codigo;          // Identificador único del recurso
        string categoria;       // Categoría o tipo de recurso
        bool disponible;        // Estado de disponibilidad del recurso para préstamo

    public:
        // Constructor parametrizado para inicializar las propiedades del recurso
        Recurso(string c, string cat);

        // Método para marcar el recurso como prestado/ocupado
        void ocupar();

        // Método para marcar el recurso como libre para un nuevo préstamo
        void liberar();
    };

    // Clase Prestamo: Relaciona a un usuario con un recurso mediante asociación de punteros
    class Prestamo {
    private:
        // Atributos privados que representan las relaciones con otras clases
        Usuario* usuario;   // Puntero que referencia al usuario asociado al préstamo
        Recurso* recurso;   // Puntero que referencia al recurso prestado
        string fecha;       // Fecha en la que se registra la transacción del préstamo

    public:
        // Constructor parametrizado para crear una transacción de préstamo
        Prestamo(Usuario* u, Recurso* r, string f);

        // Método para procesar y registrar la devolución del recurso
        void registrarDevolucion();
    };

} // Fin del namespace gestionRecursos