//Quiz 28/10/2026 

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

struct Nodo {
    int clave; string nombre;
    Nodo *izq, *der;
    Nodo(int c, string n = "") : clave(c), nombre(n), izq(nullptr), der(nullptr) {}
};

Nodo* insertar(Nodo* n, int clave, string nombre="") {
    if(n==nullptr) return new Nodo(clave, nombre);
    if (clave < n->clave) n->izq = insertar(n->izq, clave, nombre);
    else if (clave > n->clave) n->der = insertar(n->der, clave, nombre);
    return n;
}

void inorden(Nodo* n, vector<int>& s) {
    if (n == nullptr) return;
    inorden(n->izq, s);
    s.push_back(n->clave);
    inorden(n->der, s);
}

Nodo* buscar(Nodo* n, int clave, vector<string>& pasos) {
    pasos.push_back(n == nullptr ? "vacio" : to_string(n->clave));
    if (n == nullptr || n->clave == clave) return n;
    if (clave < n->clave) return buscar(n->izq, clave, pasos);
    else return buscar(n->der, clave, pasos);
}

// Sobrecarga de buscar sin pasos para la función hijos()
Nodo* buscar(Nodo* n, int clave) {
    if (n == nullptr || n->clave == clave) return n;
    if (clave < n->clave) return buscar(n->izq, clave);
    return buscar(n->der, clave);
}

Nodo* minimo(Nodo* n) {
    while (n != nullptr && n->izq != nullptr) n = n->izq;
    return n;
}

Nodo* maximo(Nodo* n) {
    while (n != nullptr && n->der != nullptr) n = n->der;
    return n;
}

Nodo* eliminar(Nodo* n, int clave) {
    if (n == nullptr) return nullptr;
    if (clave < n->clave) {
        n->izq = eliminar(n->izq, clave);
    } else if (clave > n->clave) {
        n->der = eliminar(n->der, clave);
    } else {
        if (n->izq == nullptr) { Nodo* temp = n->der; delete n; return temp; }
        if (n->der == nullptr) { Nodo* temp = n->izq; delete n; return temp; }
        Nodo* suc = minimo(n->der);
        n->clave = suc->clave;
        n->nombre = suc->nombre;
        n->der = eliminar(n->der, suc->clave);
    }
    return n;
}

int altura(Nodo* n) {
    if (n == nullptr) return -1;
    return 1 + max(altura(n->izq), altura(n->der));
}

int hijos(Nodo* n, int clave) {
    n = buscar(n, clave);
    if (n == nullptr) return -1;
    return (n->izq != nullptr ? 1 : 0) + (n->der != nullptr ? 1 : 0);
}

void liberar(Nodo* n) {
    if (n == nullptr) return;
    liberar(n->izq);
    liberar(n->der);
    delete n;
}

void verLista(const string& msg, const vector<int>& s) {
    cout << msg << "[";
    for (size_t i = 0; i < s.size(); i++) {
        cout << s[i] << (i + 1 < s.size() ? ", " : "");
    }
    cout << "]" << endl;
}

int main() {
    Nodo* raiz = nullptr;
    for (int c : {50, 30, 70, 20, 40, 60, 80, 35}) raiz = insertar(raiz, c);
    
    vector<int> s; 
    inorden(raiz, s);
    verLista("Inorden (queda ordenado): ", s);
    
    cout << "minimo = " << minimo(raiz)->clave << "  maximo = " << maximo(raiz)->clave
         << "  altura = " << altura(raiz) << endl;

    for (int objetivo : {40, 65}) {
        vector<string> p; 
        Nodo* r = buscar(raiz, objetivo, p);
        cout << "buscar(" << objetivo << "): camino ";
        for (size_t i = 0; i < p.size(); i++) { 
            cout << p[i]; 
            if (i + 1 < p.size()) cout << " ->"; 
        }
        cout << "  => " << (r ? "ENCONTRADO" : "NO ESTA")
             << " (" << p.size() << " comparaciones)" << endl;
    }

    const char* NOMBRE[] = {"caso 1: hoja, 0 hijos", "caso 2: un hijo", "caso 3: dos hijos"};
    for (int clave : {20, 30, 50}) {
        int k = hijos(raiz, clave);             
        raiz = eliminar(raiz, clave);
        s.clear(); 
        inorden(raiz, s);
        cout << "eliminar(" << clave << ") [" << NOMBRE[k] << "] -> ";
        verLista("", s);
    }
    
    Nodo* deg = nullptr;
    for (int c : {10, 20, 30, 40, 50, 60, 70, 80}) deg = insertar(deg, c);
    
    cout << "\nBTS con datos ordenados: altura = " << altura(deg) << " con 8 nodos (una lista enlazada)" << endl;
    cout << "BTS con datos mezclados: altura = " << altura(raiz) << " con 8 nodos (log2(8) = 3)" << endl;

    liberar(raiz); 
    liberar(deg);
    return 0;
}