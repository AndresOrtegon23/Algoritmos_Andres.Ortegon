// NO MODIFIQUE ESTE ARCHIVO. Alterarlo se considera fraude academico
// segun la seccion 13 de la guia de asignatura.
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <utility>
#include "sistema.h"
using namespace std;

// ---- datos del caso K ----
static int          COD[8]  = {599, 166, 651, 353, 403, 605, 179, 618};
static const char*  NOM[8]  = {"SUBESTACION", "NODO1", "NODO2", "NODO3", "PLANTA", "BATERIA", "MEDIDOR", "RURAL"};
static int          NME[8]  = {3, 4, 4, 6, 6, 4, 3, 5};
static int          MED[][3] = {{0, 0, 25}, {0, 1, 34}, {0, 2, 40}, {1, 0, 17}, {1, 1, 19}, {1, 2, 22}, {1, 3, 5}, {2, 0, 24}, {2, 1, 6}, {2, 2, 4}, {2, 3, 36}, {3, 0, 36}, {3, 1, 3}, {3, 2, 25}, {3, 3, 32}, {3, 4, 11}, {3, 5, 10}, {4, 0, 15}, {4, 1, 18}, {4, 2, 23}, {4, 3, 23}, {4, 4, 15}, {4, 5, 26}, {5, 0, 36}, {5, 1, 40}, {5, 2, 31}, {5, 3, 7}, {6, 0, 39}, {6, 1, 8}, {6, 2, 31}, {7, 0, 27}, {7, 1, 24}, {7, 2, 35}, {7, 3, 2}, {7, 4, 33}};
static const int    NMED = 35;
static vector<pair<int,int>> VIAS = {{0, 1}, {0, 2}, {0, 3}, {0, 4}, {1, 4}, {2, 5}, {3, 6}, {4, 5}, {6, 7}};
static const int    VERT = 8;
static const int    CAPV = 18;
static const int    COLA = 4;

static void cargar(Sistema& S) {
    for (int i = 0; i < 8; i++) S.registrar(COD[i], NOM[i], NME[i]);
    for (int i = 0; i < NMED; i++) S.medir(COD[MED[i][0]], MED[i][1], MED[i][2]);
}

static int fallas = 0;
static string lista2s(const vector<int>& v) {
    string r; for (size_t i=0;i<v.size();i++) { if(i) r+=","; r+=to_string(v[i]); } return r;
}
static void chkS(const string& n, const string& o, const string& e) {
    bool ok = (o == e);
    cout << "  [" << (ok ? "OK " : "FALLA") << "] " << n << ": obtuvo \"" << o << "\"";
    if (!ok) cout << "\n          esperaba \"" << e << "\"";
    cout << endl; if (!ok) fallas++;
}
static void chkI(const string& n, int o, int e) {
    bool ok = (o == e);
    cout << "  [" << (ok ? "OK " : "FALLA") << "] " << n << ": obtuvo " << o;
    if (!ok) cout << "  (esperaba " << e << ")";
    cout << endl; if (!ok) fallas++;
}

int main() {
    cout << "PARTE C++ · sistema integrado · caso K" << endl;
    cout << "----------------------------------------------------------" << endl;
    Sistema S(COLA, VIAS, VERT);
    cargar(S);

    cout << " A · memoria, lista e indice" << endl;
    chkS("la lista queda ordenada por codigo", S.codigos(), "166 179 353 403 599 605 618 651");
    chkI("cuantos puntos registrados", S.cuantos(), 8);
    chkI("altura del indice", S.alturaIndice(), 3);
    chkI("un codigo repetido no se registra", S.registrar(COD[0], "OTRO", 3) ? 1 : 0, 0);
    chkI("el repetido no altero la cantidad", S.cuantos(), 8);
    chkI("suma de todas las mediciones", S.sumaTotales(), 782);

    cout << " B · consultas sobre el indice" << endl;
    Punto* p = S.buscar(COD[3]);
    chkS("buscar devuelve el punto correcto", p ? p->nombre : string("NULO"), "NODO3");
    chkI("el indice apunta al MISMO punto de la lista", p ? p->total() : -1, 117);
    chkI("buscar un codigo ausente devuelve nulo", S.buscar(1) == nullptr ? 1 : 0, 1);
    chkS("rango amplio: todos en orden", lista2s(S.enRango(0, 1000)), "166,179,353,403,599,605,618,651");
    chkS("rango acotado [353, 605]", lista2s(S.enRango(353, 605)), "353,403,599,605");
    chkS("rango sin resultados", lista2s(S.enRango(1, 2)), "");

    cout << " C · cola circular" << endl;
    for (int i = 0; i < COLA; i++) S.encolar(COD[i]);
    chkI("encolar en cola llena devuelve false", S.encolar(COD[5]) ? 1 : 0, 0);
    chkS("cola llena", S.enEspera(), "599 166 651 353");
    int x;
    S.siguiente(x); chkI("siguiente devuelve el frente", x, 599);
    S.siguiente(x);
    S.encolar(COD[6]); S.encolar(COD[7]);
    chkS("los datos dieron la vuelta", S.enEspera(), "651 353 179 618");
    chkI("capacidad antes de ampliar", S.cap, 4);
    S.ampliarCola();
    chkI("capacidad duplicada", S.cap, 8);
    chkI("frente reubicado en 0", S.frente, 0);
    chkS("orden conservado tras ampliar", S.enEspera(), "651 353 179 618");
    S.encolar(COD[0]);
    chkS("sigue funcionando tras ampliar", S.enEspera(), "651 353 179 618 599");

    cout << " D · la red de puntos" << endl;
    chkS("ruta minima 0 -> 7", lista2s(S.rutaMinima(0, 7)), "0,3,6,7");
    chkS("ruta minima 0 -> 5", lista2s(S.rutaMinima(0, 5)), "0,2,5");
    chkS("ruta de un vertice a si mismo", lista2s(S.rutaMinima(3, 3)), "3");
    vector<string> vc = S.viasCriticas();
    string sc; for (size_t i=0;i<vc.size();i++) { if(i) sc+=","; sc+=vc[i]; }
    chkS("vias criticas", sc, "0-3,3-6,6-7");

    cout << " E · seleccion optima" << endl;
    vector<int> sel = S.mejorSeleccion(CAPV);
    chkS("mejor seleccion con capacidad 18", lista2s(sel), "403,599,605,618");
    int aporte = 0, peso = 0;
    for (size_t i=0;i<sel.size();i++) { Punto* q=S.buscar(sel[i]); aporte+=q->total(); peso+=q->nm; }
    chkI("aporte total de la seleccion", aporte, 454);
    chkI("la seleccion cabe en la capacidad", peso <= CAPV ? 1 : 0, 1);
    chkS("seleccion con capacidad 0", lista2s(S.mejorSeleccion(0)), "");

    cout << "----------------------------------------------------------" << endl;
    if (fallas == 0) {
        // Se entrega a la PARTE F lo necesario para la verificacion cruzada.
        ofstream f("cruce.txt");
        f << "cuantos=" << S.cuantos() << "\n";
        f << "suma="    << S.sumaTotales() << "\n";
        f << "altura="  << S.alturaIndice() << "\n";
        f << "capacidad=" << CAPV << "\n";
        string cods, pes, vals;
        for (Punto* a = S.lista; a != nullptr; a = a->sig) {
            if (!cods.empty()) { cods += ","; pes += ","; vals += ","; }
            cods += to_string(a->codigo);
            pes  += to_string(a->nm);
            vals += to_string(a->total());
        }
        f << "codigos="  << cods << "\n";
        f << "pesos="    << pes  << "\n";
        f << "valores="  << vals << "\n";
        f << "seleccion=" << lista2s(sel) << "\n";
        f << "aporte="   << aporte << "\n";
        f.close();
        cout << "  PARTE C++ COMPLETA. Ahora ejecute la PARTE F:  python3 pruebas.py" << endl;
    } else {
        remove("cruce.txt");
        cout << "  PARTE C++ INCOMPLETA (" << fallas << " falla(s))." << endl;
        cout << "  Corrija y vuelva a ejecutar. El codigo de cierre sale al final," << endl;
        cout << "  cuando las dos partes del sistema funcionen." << endl;
    }
    return 0;
}
