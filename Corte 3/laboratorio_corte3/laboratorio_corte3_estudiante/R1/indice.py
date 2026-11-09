# ============================================================
#  Laboratorio integrador · Corte 3 · RETO 1  (25 puntos)
#  Sesiones 35 y 36 — Arboles binarios y BST
#  Sistema: RedAcopio — indice de recursos por codigo
#
#  MODIFIQUE SOLO ESTE ARCHIVO.  NO TOQUE pruebas_r1.py
#  Ejecute:   python3 pruebas_r1.py
# ============================================================

class Nodo:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
        self.izq = None
        self.der = None
def insertar(n, codigo, nombre):
    """Inserta en el BST respetando la invariante: menores a la izquierda,
       mayores a la derecha. Si el codigo ya existe, NO se inserta.
       Devuelve la raiz del subarbol (patron de reenganche)."""
    if n is None:
        return Nodo(codigo, nombre)
    if codigo < n.codigo:
        n.izq = insertar(n.izq, codigo, nombre)
    elif codigo > n.codigo:
        n.der = insertar(n.der, codigo, nombre)
    return n

def inorden(n, salida):
    """Ya implementado: recorre izquierda, raiz, derecha."""
    if n is None:
        return
    inorden(n.izq, salida)
    salida.append(n.codigo)
    inorden(n.der, salida)


def altura(n):
    """Numero de aristas del camino mas largo de n hasta una hoja.
       Un arbol vacio tiene altura -1; un solo nodo, altura 0."""

    if n is None:
        return -1 #se resta el 1 para que un arbol vacio tenga altura -1

    else:
        altura_izq = altura(n.izq) #se busca la altura del subarbol izquierdo
        altura_der = altura(n.der) #se busca la altura del subarbol derecho
        return 1 + max(altura_izq, altura_der) #se suma 1 para contar la arista que conecta el nodo actual con su hijo y se agarra la altura mas grande de los dos hijos


def buscar(n, codigo):
    """Devuelve (nodo, comparaciones). Si no esta, el nodo es None.
       Debe bajar comparando, NO recorrer todo el arbol."""
    comparaciones= 0
    while n is not None:
        comparaciones +=1 #por cada vuelta del while se hace una comparacion
        if codigo==n.codigo: #si el codigo es igual al codigo del nodo actual entonces se encontro el nodo
            return (n, comparaciones)
        elif codigo<n.codigo: 
            n=n.izq #se hace haci para comparar el codigo con el arbol izquierdo ya que si n es menor que n.codigo entonces se debe buscar en el arbol izquierdo
        else:
            n=n.der #esto se se hace haci para comparar el codigo con el arbol derecho ya que si n no es menor que n.codigo entonces es mayor y se debe buscar en el arbol derecho
            
    return (None, comparaciones)


def minimo(n):
    """Ya implementado: el extremo izquierdo."""
    while n.izq is not None:
        n = n.izq
    return n
