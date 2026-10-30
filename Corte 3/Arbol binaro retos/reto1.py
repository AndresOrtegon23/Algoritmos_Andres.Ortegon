class NodoRecurso:
    def __init__(self, codigo: str, nombre: str):
        self.codigo = codigo
        self.nombre = nombre
        self.izquierdo = None
        self.derecho = None

class IndiceRecursos:
    def __init__(self):
        self.raiz = None

    def _insertar_recursivo(self, nodo: NodoRecurso, codigo: str, nombre: str) -> NodoRecurso:
        if nodo is None:
            return NodoRecurso(codigo, nombre)
        
        # Pista: La comparación se hace estrictamente sobre el código
        if codigo < nodo.codigo:
            nodo.izquierdo = self._insertar_recursivo(nodo.izquierdo, codigo, nombre)
        elif codigo > nodo.codigo:
            nodo.derecho = self._insertar_recursivo(nodo.derecho, codigo, nombre)
            
        return nodo

    def insertar(self, codigo: str, nombre: str):
        self.raiz = self._insertar_recursivo(self.raiz, codigo, nombre)

    def _listar_in_order(self, nodo: NodoRecurso):
        if nodo is None:
            return
        
        # Recorrido In-Order (Izquierda, Raíz, Derecha) -> Garantiza orden sin sort
        self._listar_in_order(nodo.izquierdo)
        print(f"Código: {nodo.codigo} | Nombre: {nodo.nombre}")
        self._listar_in_order(nodo.derecho)

    def listar_ordenado(self):
        print("--- Listado ordenado de recursos por código ---")
        self._listar_in_order(self.raiz)

    def _buscar_informe(self, nodo: NodoRecurso, codigo_buscado: str, comparaciones: list):
        if nodo is None:
            print(f"No encontrado. Comparaciones realizadas: {comparaciones[0]}")
            return

        comparaciones[0] += 1  # Incrementamos el contador de comparaciones sobre el código

        if codigo_buscado == nodo.codigo:
            print(f"Encontrado -> Nombre: {nodo.nombre} | Comparaciones realizadas: {comparaciones[0]}")
        elif codigo_buscado < nodo.codigo:
            self._buscar_informe(nodo.izquierdo, codigo_buscado, comparaciones)
        else:
            self._buscar_informe(nodo.derecho, codigo_buscado, comparaciones)

    def informe(self, codigo: str):
        comparaciones = [0]
        self._buscar_informe(self.raiz, codigo, comparaciones)


indice = IndiceRecursos()

    # Inserción de al menos diez recursos de la línea de proyecto
indice.insertar("REC-010", "Laptop de desarrollo")
indice.insertar("REC-003", "Router Wi-Fi industrial")
indice.insertar("REC-007", "Switch de red 24 puertos")
indice.insertar("REC-001", "Multímetro digital")
indice.insertar("REC-005", "Fuente de poder regulada")
indice.insertar("REC-009", "Cable UTP categoría 6")
indice.insertar("REC-002", "Cautín de estación")
indice.insertar("REC-008", "Sensor ultrasónico")
indice.insertar("REC-004", "Protoboard de alta densidad")
indice.insertar("REC-006", "Kit de resistencias variables")

    # 1. Demostración de listar_ordenado() sin usar sort
indice.listar_ordenado()

print("\n--- Pruebas del método informe(codigo) ---")
    
    # Búsqueda de un elemento existente
print("Buscando REC-007: ", end="")
indice.informe("REC-007")

    # Búsqueda de un elemento no existente
print("Buscando REC-999: ", end="")
indice.informe("REC-999")