#include <iostream>

class Pila {
private:
    struct Nodo {
        int dato;
        Nodo* siguiente;
        Nodo(int val) : dato(val), siguiente(nullptr) {}
    };

    Nodo* cimaPtr;

public:
    Pila() : cimaPtr(nullptr) {}

    // Destructor para liberar memoria
    ~Pila() {
        while (!vacia()) {
            desapilar();
        }
    }

    void apilar(int x) {
        Nodo* nuevo = new Nodo(x);
        nuevo->siguiente = cimaPtr;
        cimaPtr = nuevo;
    }

    int desapilar() {
        if (vacia()) {
            std::cerr << "Error: Pila vacia\n";
            return -1;
        }
        Nodo* temp = cimaPtr;
        int valor = temp->dato;
        cimaPtr = cimaPtr->siguiente;
        delete temp;
        return valor;
    }

    int cima() const {
        if (vacia()) return -1;
        return cimaPtr->dato;
    }

    bool vacia() const {
        return cimaPtr == nullptr;
    }
};

int main() {
    Pila p;
    p.apilar(10);
    p.apilar(20);
    p.apilar(30);

    std::cout << p.desapilar() << std::endl; // 30
    std::cout << p.cima() << std::endl;       // 20
    std::cout << p.vacia() << std::endl;      // 0 (False)

    return 0;
}