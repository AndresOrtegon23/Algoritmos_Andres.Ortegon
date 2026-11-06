// Quiz 6/11/2026

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <utility>

using namespace std;

const vector<string> NOMBRES = {
    "CENTRO", "NORTE", "SUR", "ORIENTE", "OCCIDENTE", 
    "CHAPINERO", "USAQUEN", "BOSA", "VEREDA"
};

const vector<pair<int, int>> ARISTAS = {
    {0,1}, {1,3}, {0,2}, {0,3}, {1,5},
    {2,7}, {3,6}, {5,6}, {4,7}, {7,8},
    {8,1}, {7,5}, {5,8}, {2,6}, {6,8},
    {1,8}, {5,7}, {5,2}
};

int N = NOMBRES.size();

void dfsRec(int u, vector<bool>& vis, vector<int>& orden, const vector<vector<int>>& adj) {
    vis[u] = true;
    orden.push_back(u);
    for (int v : adj[u])
        if (!vis[v]) dfsRec(v, vis, orden, adj);
}

vector<int> dfsIter(int inicio, const vector<vector<int>>& adj) {
    vector<bool> vis(N, false);
    vector<int> pila{inicio}, orden;
    while (!pila.empty()) {
        int u = pila.back(); pila.pop_back();
        if (vis[u]) continue;
        vis[u] = true;
        orden.push_back(u);
        for (auto it = adj[u].rbegin(); it != adj[u].rend(); ++it)
            if (!vis[*it]) pila.push_back(*it);
    }
    return orden;
}

void imprimirOrden(const vector<int>& orden) {
    for (size_t i = 0; i < orden.size(); ++i) {
        cout << NOMBRES[orden[i]];
        if (i + 1 < orden.size()) cout << " -> ";
    }
    cout << endl;
}

vector<vector<string>> obtenerComponentes(const vector<vector<int>>& adj) {
    vector<bool> vis(N, false);
    vector<vector<string>> comps;
    for (int s = 0; s < N; ++s) {
        if (!vis[s]) {
            vector<int> o;
            dfsRec(s, vis, o, adj);
            vector<string> compNombres;
            for (int i : o) compNombres.push_back(NOMBRES[i]);
            comps.push_back(compNombres);
        }
    }
    return comps;
}

void imprimirComponentes(const vector<vector<string>>& comps) {
    cout << "[";
    for (size_t i = 0; i < comps.size(); ++i) {
        cout << "[";
        for (size_t j = 0; j < comps[i].size(); ++j) {
            cout << "'" << comps[i][j] << "'";
            if (j + 1 < comps[i].size()) cout << ", ";
        }
        cout << "]";
        if (i + 1 < comps.size()) cout << ", ";
    }
    cout << "]\n";
}

bool explorarCiclo(int u, int padre, const vector<vector<int>>& adj, vector<bool>& vis) {
    vis[u] = true;
    for (int v : adj[u]) {
        if (!vis[v]) {
            if (explorarCiclo(v, u, adj, vis)) return true;
        } else if (v != padre) {
            return true;
        }
    }
    return false;
}

bool hayCiclo(const vector<vector<int>>& adj) {
    vector<bool> vis(N, false);
    for (int s = 0; s < N; ++s) {
        if (!vis[s] && explorarCiclo(s, -1, adj, vis)) return true;
    }
    return false;
}

int main() {
    vector<vector<int>> lista(N);
    for (const auto& arista : ARISTAS) {
        lista[arista.first].push_back(arista.second);
        lista[arista.second].push_back(arista.first);
    }
    for (auto& v : lista) sort(v.begin(), v.end());

    // 1. DFS Recursivo
    vector<bool> vis(N, false);
    vector<int> ordenRec;
    dfsRec(0, vis, ordenRec, lista);
    cout << "orden de visita: ";
    imprimirOrden(ordenRec);

    // 2. DFS Iterativo
    cout << "\nDFS ITERATIVO (con pila explicita) desde CENTRO\n";
    cout << "  orden de visita: ";
    imprimirOrden(dfsIter(0, lista));

    // 3. Componentes Conexas
    cout << "\nCOMPONENTES CONEXAS de la red completa: ";
    imprimirComponentes(obtenerComponentes(lista));

    // Red cortada
    vector<vector<int>> listaRota(N);
    vector<pair<int, int>> aristasRotas = {{0,1}, {0,2}, {3,6}};
    for (const auto& arista : aristasRotas) {
        listaRota[arista.first].push_back(arista.second);
        listaRota[arista.second].push_back(arista.first);
    }
    for (auto& v : listaRota) sort(v.begin(), v.end());

    cout << "COMPONENTES de una red con tramos cortados: ";
    imprimirComponentes(obtenerComponentes(listaRota));

    // 4. Ciclo
    cout << "¿La red tiene algun circuito? " << (hayCiclo(lista) ? "True" : "False") << "\n";

    return 0;
}