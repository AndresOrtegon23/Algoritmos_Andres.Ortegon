def existeGrafo(v, k):
    if (v * k) % 2 != 0:
        return False      # la suma de grados sería impar
    if k > v - 1:
        return False      # no hay suficientes vértices para conectar
    return True

print("Suma de grados:", 5 * 3)
print("¿Existe grafo de 5 vértices con grado 3?", existeGrafo(5, 3))

print()
print("Tabla (SI = existe, NO = imposible)")
print("      k=", end="")
for k in range(1, 8):
    print(k, " ", end="")
print()
for v in range(2, 9):
    print("V =", v, "  ", end="")
    for k in range(1, 8):
        if existeGrafo(v, k):
            print("SI ", end="")
        else:
            print("NO ", end="")
    print()