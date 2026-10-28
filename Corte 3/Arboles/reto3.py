class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None

def copiar_arbol(nodo):
    if nodo is None:
        return None
    nuevo = Nodo(nodo.dato)
    nuevo.izq = copiar_arbol(nodo.izq)
    nuevo.der = copiar_arbol(nodo.der)
    return nuevo

def espejo(nodo):
    if nodo is None:
        return
    nodo.izq, nodo.der = nodo.der, nodo.izq
    espejo(nodo.izq)
    espejo(nodo.der)

def sonIguales(a, b):
    # Si ambos nodos son nulos, son iguales en esta rama
    if a is None and b is None:
        return True
    # Si uno es nulo y el otro no, la estructura o tamaño difiere
    if a is None or b is None:
        return False
    
    # Compara el dato actual y verifica recursivamente ambos subárboles
    return (a.dato == b.dato) and sonIguales(a.izq, b.izq) and sonIguales(a.der, b.der)

# 1. Construcción del árbol original
raiz1 = Nodo("CATALOGO")
raiz1.izq = Nodo("HERRAMIENTA"); raiz1.der = Nodo("LIBRO")
raiz1.izq.izq = Nodo("TALADRO");  raiz1.izq.der = Nodo("SIERRA")
raiz1.der.izq = Nodo("ARTE");     raiz1.der.der = Nodo("TECNICO")
raiz1.der.der.der = Nodo("REDES")

# 2. Creamos una copia idéntica para probar una igualdad exitosa
raiz_copia = copiar_arbol(raiz1)

# 3. Creamos otra copia y la convertimos en su espejo
raiz_espejo = copiar_arbol(raiz1)
espejo(raiz_espejo)

# Pruebas
print(f"¿El árbol original es igual a su copia idéntica?: {sonIguales(raiz1, raiz_copia)}")
print(f"¿El árbol original es igual a su propio espejo?: {sonIguales(raiz1, raiz_espejo)}")