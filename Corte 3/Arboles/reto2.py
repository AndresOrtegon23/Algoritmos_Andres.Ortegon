class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None

def inorden(n, salida):
    if n is None: return
    inorden(n.izq, salida)
    salida.append(n.dato)
    inorden(n.der, salida)

def espejo(nodo):
    if nodo is None:
        return
    # Intercambiar los hijos izquierdo y derecho
    nodo.izq, nodo.der = nodo.der, nodo.izq
    # Llamar recursivamente para hacer lo mismo en los subárboles
    espejo(nodo.izq)
    espejo(nodo.der)

# Construcción del árbol original
raiz = Nodo("CATALOGO")
raiz.izq = Nodo("HERRAMIENTA"); raiz.der = Nodo("LIBRO")
raiz.izq.izq = Nodo("TALADRO");  raiz.izq.der = Nodo("SIERRA")
raiz.der.izq = Nodo("ARTE");     raiz.der.der = Nodo("TECNICO")
raiz.der.der.der = Nodo("REDES")

# 1. Obtener e imprimir el inorden original
s_original = []
inorden(raiz, s_original)
print(f"Inorden original: {' -> '.join(s_original)}")

# 2. Aplicar la función espejo
espejo(raiz)

# 3. Obtener e imprimir el inorden del árbol espejado
s_espejo = []
inorden(raiz, s_espejo)
print(f"Inorden espejado: {' -> '.join(s_espejo)}")