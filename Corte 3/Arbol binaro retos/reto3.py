class NodoArbol:
    def __init__(self, valor: int, nombre: str):
        self.valor = valor
        self.nombre = nombre
        self.izquierdo = None
        self.derecho = None

def _es_bst_recursivo(nodo, min_val, max_val):
    # Caso base: un árbol vacío es un BST válido
    if nodo is None:
        return True

    # Verificamos si el valor actual respeta los límites permitidos por sus ancestros
    if (min_val is not None and nodo.valor <= min_val) or \
       (max_val is not None and nodo.valor >= max_val):
        return False

    # Al ir a la izquierda, el valor máximo permitido se restringe al valor del nodo actual
    # Al ir a la derecha, el valor mínimo permitido se restringe al valor del nodo actual
    return (_es_bst_recursivo(nodo.izquierdo, min_val, nodo.valor) and 
            _es_bst_recursivo(nodo.derecho, nodo.valor, max_val))

def es_bst(raiz):
    # Inicialmente no hay límites (infinitos negativos y positivos)
    return _es_bst_recursivo(raiz, None, None)

# Construcción manual del árbol inválido (contraejemplo):
    # - Raíz: 50
    # - Hijo izquierdo de 50: 30
    # - Hijo derecho de 30: 60 (¡Violación! 60 está en el subárbol izquierdo de 50 pero es mayor que 50)
    
    raiz = NodoArbol(50, "Servidor Central")
    
    nodo_30 = NodoArbol(30, "Router Industrial")
    raiz.izquierdo = nodo_30
    
    # El 60 es hijo DERECHO del 30
    nodo_60 = NodoArbol(60, "Switch Auxiliar")
    nodo_30.derecho = nodo_60

    # Evaluación del contraejemplo
    resultado = es_bst(raiz)
    print(f"¿El árbol es un BST válido?: {resultado}")