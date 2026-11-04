# Quiz 4/11/2026

NOMBRES = ["CENTRO", "NORTE", "SUR", "ORIENTE", "OCCIDENTE", 
           "CHAPINERO", "USAQUEN", "BOSA", "VEREDA"]

ARISTAS = [
    (0,1), (1,3), (0,2), (0,3), (1,5),
    (2,7), (3,6), (5,6), (4,7), (7,8),
    (8,1), (7,5), (5,8), (2,6), (6,8),
    (1,8), (5,7), (5,2)
]

N = len(NOMBRES)

# ---------- Representacion 1: matriz de adyacencia ----------
matriz = [[0]*N for _ in range(N)]
for u, v in ARISTAS:
    matriz[u][v] = 1
    matriz[v][u] = 1               # grafo NO dirigido: la matriz es simetrica

print("MATRIZ DE ADYACENCIA")
print("            " + " ".join(f"{n[:3]:>4}" for n in NOMBRES))
for i in range(N):
    print(f"{NOMBRES[i]:>11} " + " ".join(f"{matriz[i][j]:>4}" for j in range(N)))

# ---------- Representacion 2: lista de adyacencia (evitando duplicados) ----------
lista = [[] for _ in range(N)]
for u, v in ARISTAS:
    if v not in lista[u]:
        lista[u].append(v)
    if u not in lista[v]:
        lista[v].append(u)
for v in lista: v.sort()

print("\nLISTA DE ADYACENCIA")
for i in range(N):
    print(f"  {NOMBRES[i]:>10} -> {', '.join(NOMBRES[j] for j in lista[i])}")

# ---------- Grados ----------
print("\nGRADO DE CADA VERTICE (cuantas vias salen de el)")
for i in range(N):
    g_mat = sum(matriz[i])        # recorrer una fila: O(N)
    g_lis = len(lista[i])         # leer el tamano: O(1)
    assert g_mat == g_lis
    print(f"  {NOMBRES[i]:>10}: {g_lis}")

# ---------- Costos ----------
aristas = len(ARISTAS)
print(f"\nV = {N} vertices,  E = {aristas} aristas")
print(f"  Matriz : {N*N} casillas en memoria. ¿Existe arista? O(1). Recorrer vecinos: O(V) = {N} casillas.")
print(f"  Lista  : {sum(len(l) for l in lista)} referencias en memoria. ¿Existe arista? O(grado). Recorrer vecinos: O(grado).")
densidad = sum(sum(m) for m in matriz) / (N*(N-1))
print(f"  Densidad = 2E / (V(V-1)) = {densidad:.2f}  ->  grafo {'DENSO: conviene matriz' if densidad > 0.5 else 'DISPERSO: conviene lista'}")

# ---------- Consulta de arista ----------
def hay_via_matriz(u, v): return matriz[u][v] == 1
def hay_via_lista(u, v):  return v in lista[u]

for u, v in [(0,1),(0,7),(5,6)]:
    print(f"  ¿{NOMBRES[u]} conecta con {NOMBRES[v]}? matriz={hay_via_matriz(u,v)}  lista={hay_via_lista(u,v)}")

# ---------- Verificación si SUR conecta con todos ----------
print(f"\nVerificando si {NOMBRES[2]} (SUR) se conecta con todas las zonas:")
for v in range(N):
    m_res = hay_via_matriz(2, v)
    l_res = hay_via_lista(2, v)
    print(f"  ¿Conecta con {NOMBRES[v]:<10}? matriz={m_res!s:<5} lista={l_res!s:<5}")