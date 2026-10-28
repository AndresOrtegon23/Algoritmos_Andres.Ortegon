class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None

def imprimirJerarquia(nodo, nivel=0):
    if nodo is None:
        return
    # Imprime dos espacios por cada nivel de profundidad seguido del dato
    print("  " * nivel + nodo.dato)
    # Recorrido en preorden: izquierda y luego derecha
    imprimirJerarquia(nodo.izq, nivel + 1)
    imprimirJerarquia(nodo.der, nivel + 1)

# Construcción del árbol del ejemplo
raiz = Nodo("CATALOGO")
raiz.izq = Nodo("HERRAMIENTA"); raiz.der = Nodo("LIBRO")
raiz.izq.izq = Nodo("TALADRO");  raiz.izq.der = Nodo("SIERRA")
raiz.der.izq = Nodo("ARTE");     raiz.der.der = Nodo("TECNICO")
raiz.der.der.der = Nodo("REDES")

print("Jerarquía del Catálogo:")
imprimirJerarquia(raiz)