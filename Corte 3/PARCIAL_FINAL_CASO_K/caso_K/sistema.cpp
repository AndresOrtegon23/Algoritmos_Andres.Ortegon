#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include "sistema.h"
using namespace std;

// ============================================================
//   BASE YA RESUELTA — lea estas funciones: son su punto de partida
//   y muestran el estilo con el que debe escribir las que faltan.
//   En la mesa se le puede preguntar por cualquiera de ellas.
// ============================================================

Punto::Punto(int c, const string& n, int cantidad) {
    codigo = c;
    nombre = n;
    nm = cantidad;
    mediciones = new int[nm];              // memoria dinamica
    for (int i = 0; i < nm; i++) mediciones[i] = 0;
    sig = nullptr;
}

int Punto::total() const {
    int s = 0;
    for (int i = 0; i < nm; i++) s += mediciones[i];
    return s;
}

NodoIndice::NodoIndice(int c, Punto* p) {
    codigo = c; dato = p; izq = nullptr; der = nullptr;
}

Sistema::Sistema(int capacidadCola, const vector<pair<int,int>>& vias, int vertices) {
    lista  = nullptr;
    indice = nullptr;
    cap    = capacidadCola;
    cola   = new int[cap];
    frente = 0;
    enCola = 0;
    aristas = vias;
    red.assign(vertices, {});
    for (size_t i = 0; i < vias.size(); i++) {
        red[vias[i].first ].push_back(vias[i].second);
        red[vias[i].second].push_back(vias[i].first);
    }
    for (size_t i = 0; i < red.size(); i++) sort(red[i].begin(), red[i].end());
}

Sistema::~Sistema() {
    liberarTodo();                         // usted escribe liberarTodo()
    delete[] cola;
}

bool Sistema::encolar(int codigo) {
    if (enCola == cap) return false;                 // desbordamiento controlado
    cola[(frente + enCola) % cap] = codigo;          // el final se CALCULA
    enCola++;
    return true;
}

bool Sistema::siguiente(int& codigo) {
    if (enCola == 0) return false;                   // subdesbordamiento
    codigo = cola[frente];
    frente = (frente + 1) % cap;
    enCola--;
    return true;
}

string Sistema::enEspera() const {
    string r;
    for (int i = 0; i < enCola; i++) {
        if (i > 0) r += " ";
        r += to_string(cola[(frente + i) % cap]);
    }
    return r;
}

int Sistema::cuantos() const {
    int k = 0;
    for (Punto* a = lista; a != nullptr; a = a->sig) k++;
    return k;
}

string Sistema::codigos() const {
    string r;
    for (Punto* a = lista; a != nullptr; a = a->sig) {
        if (!r.empty()) r += " ";
        r += to_string(a->codigo);
    }
    return r;
}

void Sistema::medir(int codigo, int i, int valor) {
    Punto* p = buscar(codigo);                       // usa SU buscar()
    if (p == nullptr) return;
    if (i < 0 || i >= p->nm) return;                 // indice fuera de rango
    p->mediciones[i] = valor;
}

int Sistema::sumaTotales() const {
    int s = 0;
    for (Punto* a = lista; a != nullptr; a = a->sig) s += a->total();
    return s;
}
// ------------------------------------------------------------
//   Estas cinco funciones TAMBIEN se le entregan resueltas.
//   Lealas: son el modelo de lo que usted debe escribir, y en la
//   mesa se le puede preguntar por cualquiera de ellas.
// ------------------------------------------------------------

Punto* Sistema::buscar(int codigo) const {
    NodoIndice* n = indice;                 // DESCIENDE por el indice:
    while (n != nullptr) {                  // no recorre la lista
        if (codigo == n->codigo) return n->dato;
        n = (codigo < n->codigo) ? n->izq : n->der;
    }
    return nullptr;
}

static int altura(NodoIndice* n) {
    if (n == nullptr) return -1;
    return 1 + max(altura(n->izq), altura(n->der));
}

int Sistema::alturaIndice() const { return altura(indice); }

static void borrarIndice(NodoIndice* n) {
    if (n == nullptr) return;
    borrarIndice(n->izq);
    borrarIndice(n->der);
    delete n;                      // NO se borra n->dato: es de la lista
}

void Sistema::liberarTodo() {
    Punto* a = lista;
    while (a != nullptr) {
        Punto* s = a->sig;         // guardar el siguiente ANTES de borrar
        delete a;
        a = s;
    }
    lista = nullptr;
    borrarIndice(indice);
    indice = nullptr;
}

void Sistema::ampliarCola() {
    int* nueva = new int[cap * 2];
    for (int i = 0; i < enCola; i++)
        nueva[i] = cola[(frente + i) % cap];        // en ORDEN DE SALIDA
    delete[] cola;
    cola = nueva;
    cap *= 2;
    frente = 0;
}

static int componentes(const vector<vector<int>>& g) {
    int V = (int)g.size();
    vector<bool> vis(V, false);
    int c = 0;
    for (int s = 0; s < V; s++) {
        if (vis[s]) continue;
        c++;
        vector<int> pila;                      // recorrido en PROFUNDIDAD
        pila.push_back(s); vis[s] = true;
        while (!pila.empty()) {
            int u = pila.back(); pila.pop_back();
            for (size_t t = 0; t < g[u].size(); t++)
                if (!vis[g[u][t]]) { vis[g[u][t]] = true; pila.push_back(g[u][t]); }
        }
    }
    return c;
}

vector<string> Sistema::viasCriticas() const {
    vector<string> out;
    int V = (int)red.size();
    for (size_t i = 0; i < aristas.size(); i++) {
        vector<vector<int>> g(V);
        for (size_t j = 0; j < aristas.size(); j++) {
            if (j == i) continue;
            g[aristas[j].first ].push_back(aristas[j].second);
            g[aristas[j].second].push_back(aristas[j].first);
        }
        if (componentes(g) > 1)
            out.push_back(to_string(aristas[i].first) + "-" + to_string(aristas[i].second));
    }
    return out;
}

// ============================================================
//   LO QUE USTED DEBE COMPLETAR
//   Son SEIS funciones: cinco aqui y una en analisis.py.
//   Estan acopladas: medir() usa buscar(), buscar() usa el indice que
//   construye registrar(), y mejorSeleccion() usa total().
//   Si registrar() queda mal, falla casi todo lo demas: empiece por ahi.
// ============================================================

// ---------------- PARTE A · memoria, lista e indice ----------------

Punto::~Punto() {
    // (6 puntos) El constructor pidio memoria con new[]. Devuelvala.
    // PENDIENTE
    delete[] mediciones;
    delete[] sig;
}

bool Sistema::registrar(int codigo, const string& nombre, int cantidad) {
    // (24 puntos) ESTA ES LA FUNCION CENTRAL DEL PARCIAL.
    //
    // Debe hacer TRES cosas, y las tres tienen que quedar coherentes:
    //   1. Si el codigo ya existe, no registrar nada y devolver false.
    //      Tiene buscar() ya resuelta para averiguarlo.
    //   2. Crear el Punto e insertarlo en 'lista' manteniendola ORDENADA
    //      de forma ascendente por codigo. Contemple los tres casos:
    //      lista vacia, insercion antes de la cabeza, e insercion en el
    //      medio o al final.
    //   3. Insertar en 'indice' un NodoIndice con ese codigo que APUNTE
    //      al Punto que acabo de crear. El arbol es un BST por codigo.
    //      Puede escribir una funcion auxiliar libre en este archivo.
    //
    // El indice NO duplica la informacion: guarda un puntero al mismo
    // Punto que esta en la lista. Si inserta una copia, medir() escribira
    // en un sitio y total() leera de otro, y el sistema queda incoherente
    // sin dar un solo error de compilacion.
    //
    // PENDIENTE

    //1.
    if (buscar(codigo) != nullptr){
        return false;
    }       //tiene que buscar() ya resuelta para averiguarlo.

    //2.
    Punto* nuevoPunto = new Punto(codigo, nombre, cantidad);        //Se crea el nuevo punto
    if (lista == nullptr) {
        lista = nuevoPunto;     // Si la lista es vacia, el nuevo punto es el primero de la lista
    } else if (codigo < lista->codigo) {        // Si el codigo es menor que el primer elemnto 
        nuevoPunto->sig = lista;
        lista = nuevoPunto;     // Se inserta al principio de la lista
    } else {
        Punto* actual = lista;      // Se busca la posicion del elemnto en la lista
        while (actual->sig != nullptr && actual->sig->codigo < codigo) {        
            actual = actual->sig;       // Se recorre la lista hasta encontrar el elemento
        }
        nuevoPunto->sig = actual->sig;      // Se encuentra y se inserta el nuevo punto en las lista
        actual->sig = nuevoPunto;       // Se inserta el nuevo puntp en la lista
    }

    //3.
    NodoIndice* nuevoNodo = new NodoIndice(codigo, nuevoPunto);      // Se crea el nodo indice
    if (indice == nullptr) {
        indice = nuevoNodo;      // Si el indice es vacio, el nuevo nodo es el primero del indice
    } else {
        NodoIndice* actual = indice;       // Se busca la posicion del elemnto en el indice
        while (true) {
            if (codigo < actual->codigo) {      // Si el codigo es menor que el actual, se inserta a la izquierda
                if (actual->izq == nullptr) {       // Si no hay nodo a la izquierda, se inserta el nuevo nodo
                    actual->izq = nuevoNodo;
                    break;
                } else {
                    actual = actual->izq;       // Si hay nodo a la izquierda, se recorre el indice
                }
            } else {        // Si el codigo es mayor que el actual, se inserta a la derecha
                if (actual->der == nullptr) {       // Si no hay nodo a la derecha, se inserta el nuevo nodo
                    actual->der = nuevoNodo;
                    break;
                } else {
                    actual = actual->der;       // Si hay nodo a la derecha, se recorre el indice
                }
            }
        }
    
    }

    return false;
}

// ---------------- PARTE B · consultas sobre el indice ----------------

vector<int> Sistema::enRango(int a, int b) const {
    // (14 puntos) Devuelve los codigos entre a y b, ambos incluidos,
    // en orden ASCENDENTE.
    //
    // No recorra todo el arbol para filtrar despues: PODE. Si el codigo
    // del nodo ya es menor o igual que a, no tiene sentido bajar por la
    // izquierda; si ya es mayor o igual que b, no tiene sentido bajar por
    // la derecha. La pregunta de la mesa es exactamente sobre esto.
    // PENDIENTE

    //   [FALLA] rango amplio: todos en orden: obtuvo ""
        //  esperaba "166,179,353,403,599,605,618,651"
  ///[FALLA] rango acotado [353, 605]: obtuvo ""
     //     esperaba "353,403,599,605"

    vector<int> codigos;        // Se inicializa el vector de codigos
    NodoIndice* indice = this->indice;      // Se inicializa el puntero al indice
    
    while (indice != nullptr) {
        if (indice->codigo >= a && indice->codigo <= b) {       // Si el codigo esta en el rango, se agrega al vector
            codigos.push_back(indice->codigo);
        }
        else if (indice->codigo > a) {       // Si el codigo es mayor que a, se baja por la izquierda
            indice = indice->izq;
        } else if (indice->codigo < a) {        // Si el codigo es menor que a, se baja por la derecha
            indice = indice->der;
        }
        else if (indice->codigo < b) {       // Si el codigo es menor que b, se baja por la derecha
            indice = indice->der;
        } else if (indice->codigo > b) {        // Si el codigo es mayor que b, se baja por la izquierda
            indice = indice->izq;
        }
        else if (indice->codigo == a || indice->codigo == b) {        // Si el codigo es igual a a o b, se baja por ambos lados
            indice = indice->izq;
            indice = indice->der;
        }

    }

    return codigos;     
}

// ---------------- PARTE D · la red de puntos ----------------

vector<int> Sistema::rutaMinima(int origen, int destino) const {
    // (14 puntos) Devuelve la ruta con MENOS tramos entre los dos
    // vertices, como la secuencia de vertices desde 'origen' hasta
    // 'destino', ambos incluidos. Si no hay camino, devuelve un vector
    // vacio. Si origen == destino, devuelve {origen}.
    //
    // Use 'red', que ya esta construida. Recuerde que el recorrido que
    // garantiza el minimo numero de tramos es el de ANCHURA, y que para
    // reconstruir la ruta hace falta recordar de donde se llego a cada
    // vertice. Tiene viasCriticas() resuelta como ejemplo de recorrido
    // sobre la misma red.
    // PENDIENTE

    // Se devuelve la ruta con menos tramos
    // Solucion: bfs para encontrar el camino mas corto
    // Se inicializa el vector de la ruta    

    vector <int> ruta;

    for (int i = 0; i < red.size(); i++) {
        ruta.push_back(-1);       // Se inicializa el vector de la ruta con -1
    }
    if (origen == destino) {       // Si el origen es igual al destino, se devuelve el origen
        ruta[origen] = origen;
        return {origen};
    }
    else if (origen < 0 || origen >= red.size() || destino < 0 || destino >= red.size()) {       // Si el origen o el destino son invalidos, se devuelve un vector vacio
        return {};
    }
    else if (red[origen].empty() || red[destino].empty()) {       // Si el origen o el destino no tienen vecinos, se devuelve un vector vacio
        return {};
    }

    return {};
}

// ---------------- PARTE E · seleccion optima ----------------

vector<int> Sistema::mejorSeleccion(int capacidad) const {
    // (12 puntos) El vehiculo soporta 'capacidad' mediciones en total.
    // Cada punto ocupa 'nm' y aporta 'total()'. Cada punto se lleva o no
    // se lleva: no se parte ni se repite.
    //
    // Devuelva los CODIGOS de la seleccion de mayor aporte total que no
    // pase de la capacidad, en orden ascendente. Si hay empate en aporte,
    // la de MENOS puntos.
    //
    // Resuelvalo con recursion de tomar / no tomar, y pode la rama de
    // tomar cuando el punto ya no quepa.
    // PENDIENTE

    vector<int> seleccion;
    for (Punto* a = lista; a != nullptr; a = a->sig) {
        if (a->nm <= capacidad) {       // Si el punto cabe en la capacidad, se agrega a la seleccion
            seleccion.push_back(a->codigo);
            capacidad -= a->nm;      // Se resta la capacidad del punto agregado
        }
        else if (capacidad == 0) {        // Si la capacidad es 0, se devuelve la seleccion
            return seleccion;
        }
    }
    return seleccion;
}

//Falla rango amplio, rango acotado, ruta minima, mejor seleccion, aporte total de la seleccion