// ============================================================
//  Laboratorio integrador · Corte 3 · RETO 4  (25 puntos)
//  Sesiones 41 y 43 — DFS, componentes conexas y vias criticas
//  Sistema: RedAcopio — que vias no pueden cerrarse
//
//  Este archivo NO tiene main(): el main esta en pruebas_r4.cpp
//  MODIFIQUE SOLO ESTE ARCHIVO.  NO TOQUE pruebas_r4.cpp ni red.h
//  Compile y ejecute:
//     g++ -std=c++17 -g -o pruebas_r4 conectividad.cpp pruebas_r4.cpp
//     ./pruebas_r4
//  Estudiante: Andres Felipe Ortegon Porras
// ============================================================
#include <vector>
#include <string>
#include "red.h"
using namespace std;


int cuantasComponentes(const vector<vector<int>>& g) {
    // Cuenta en cuantos pedazos esta partida la red.
    // Lance un DFS desde cada vertice que todavia no haya sido visitado;
    // cada DFS que arranca es una componente nueva.
    // Use una PILA explicita (un vector<int> con push_back y pop_back), no recursion.
   
    int n = g.size();
    vector<bool> visitado(n, false);
    int componentes = 0;


    for (int i = 0; i < n; ++i) {
        if (!visitado[i]) {
            // Cada vez que encontramos un nodo no visitado, arranca una nueva componente
            componentes++;
            vector<int> pila;
            pila.push_back(i);
            visitado[i] = true;


            while (!pila.empty()) {
                int u = pila.back();
                pila.pop_back();


                for (int v : g[u]) {
                    if (!visitado[v]) {
                        visitado[v] = true;
                        pila.push_back(v);
                    }
                }
            }
        }
    }
    return componentes;
}


vector<string> viasCriticas() {
    // Una via es CRITICA si al cerrarla la red deja de estar conectada.
    // Para cada arista: arme la red SIN esa arista y cuente componentes.
    // Si pasa de 1 a mas de 1, la via es critica.
    // Devuelva los nombres con el formato  "ORIGEN-DESTINO"
    // respetando el orden en que aparecen en ARISTAS.


    vector<string> criticas;
    int componentesOriginales = cuantasComponentes(construir(ARISTAS));


    for (size_t i = 0; i < ARISTAS.size(); ++i) {
        vector<pair<int, int>> aristasModificadas;
        for (size_t j = 0; j < ARISTAS.size(); ++j) {
            if (j != i) {
                aristasModificadas.push_back(ARISTAS[j]);
            }
        }


        // Construir la red sin la arista actual
        vector<vector<int>> gSinArista = construir(aristasModificadas);
        int comps = cuantasComponentes(gSinArista);


        // Si el número de componentes aumenta al quitar la arista, es crítica
        if (comps > componentesOriginales) {
            int u = ARISTAS[i].first;
            int v = ARISTAS[i].second;
            string nombreVia = NOMBRES[u] + "-" + NOMBRES[v];
            criticas.push_back(nombreVia);
        }
    }


    return criticas;
}
