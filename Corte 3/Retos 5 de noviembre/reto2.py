def pruebaIdaYVuelta(m):
    lista = matrizALista(m)
    vuelta = listaAMatriz(lista)
    return vuelta == m


def pruebaTodas(maxVertices):
    total = 0
    for n in range(maxVertices + 1):
        pares = []
        for i in range(n):
            for j in range(i + 1, n):
                pares.append((i, j))
        for combinacion in range(2 ** len(pares)):
            m = []
            for i in range(n):
                m.append([0] * n)
            for k in range(len(pares)):
                if (combinacion >> k) & 1 == 1:     # ¿la arista k está activa?
                    i, j = pares[k]
                    m[i][j] = 1
                    m[j][i] = 1
            total += 1
            if not pruebaIdaYVuelta(m):
                print("ERROR con la matriz:", m)
                return
    print("OK:", total, "matrices válidas probadas (hasta", maxVertices, "vértices), todas vuelven iguales")


# ---------- 2) LAS CONVERSIONES ----------
def matrizALista(m):
    n = len(m)
    lista = []
    for i in range(n):
        vecinos = []
        for j in range(n):
            if m[i][j] == 1:
                vecinos.append(j)
        lista.append(vecinos)
    return lista


def listaAMatriz(l):
    n = len(l)
    m = []
    for i in range(n):
        m.append([0] * n)
    for u in range(n):
        for v in l[u]:
            m[u][v] = 1
    return m

matriz = [[0, 1, 1, 0],
          [1, 0, 0, 1],
          [1, 0, 0, 0],
          [0, 1, 0, 0]]

print("matriz:", matriz)
print("lista :", matrizALista(matriz))
print("de vuelta:", listaAMatriz(matrizALista(matriz)))
print("¿igual al original?", pruebaIdaYVuelta(matriz))
print()
pruebaTodas(5)