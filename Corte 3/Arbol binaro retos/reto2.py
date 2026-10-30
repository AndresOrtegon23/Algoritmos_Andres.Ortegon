class NodoRecurso:
    def __init__(self, codigo: str, nombre: str):
        self.codigo = codigo
        self.nombre = nombre
        self.izquierdo = None
        self.derecho = None

class IndiceRecursos:
    def __init__(self):
        self.raiz = None
        self._total_nodos = 0  # Contador global para llevar el total de nodos del árbol

    def _insertar_recursivo(self, nodo: NodoRecurso, codigo: str, nombre: str) -> NodoRecurso:
        if nodo is None:
            self._total_nodos += 1
            return NodoRecurso(codigo, nombre)
        
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

        comparaciones[0] += 1

        if codigo_buscado == nodo.codigo:
            print(f"Encontrado -> Nombre: {nodo.nombre} | Comparaciones realizadas: {comparaciones[0]}")
        elif codigo_buscado < nodo.codigo:
            self._buscar_informe(nodo.izquierdo, codigo_buscado, comparaciones)
        else:
            self._buscar_informe(nodo.derecho, codigo_buscado, comparaciones)

    def informe(self, codigo: str):
        comparaciones = [0]
        self._buscar_informe(self.raiz, codigo, comparaciones)

    # --- Implementación del Reto 2: enRango con Doble Poda ---
    def _en_rango_recursivo(self, nodo: NodoRecurso, a: str, b: str, contador: list):
        if nodo is None:
            return

        # Poda 1: Solo exploramos la izquierda si 'a' es menor que la clave del nodo actual
        if a < nodo.codigo:
            self._en_rango_recursivo(nodo.izquierdo, a, b, contador)

        # Contamos el nodo que estamos visitando efectivamente
        contador[0] += 1

        # Si el nodo actual se encuentra dentro del rango [a, b], lo imprimimos
        if a <= nodo.codigo <= b:
            print(f"-> Código: {nodo.codigo} | Nombre: {nodo.nombre}")

        # Poda 2: Solo exploramos la derecha si la clave del nodo actual es menor que 'b'
        if nodo.codigo < b:
            self._en_rango_recursivo(nodo.derecho, a, b, contador)

    def en_rango(self, a: str, b: str):
        print(f"\n Recursos en el rango [{a}, {b}] ")
        contador_visitados = [0]
        self._en_rango_recursivo(self.raiz, a, b, contador_visitados)
        print(f"Nodos visitados con poda: {contador_visitados[0]}")
        print(f"Total de nodos en el árbol: {self._total_nodos}")


indice = IndiceRecursos()

    # Inserción de al menos diez recursos con códigos uniformes para evaluar rangos
indice.insertar("REC-050", "Servidor central")
indice.insertar("REC-030", "Router Wi-Fi industrial")
indice.insertar("REC-070", "Switch de red 24 puertos")
indice.insertar("REC-015", "Multímetro digital")
indice.insertar("REC-040", "Fuente de poder regulada")
indice.insertar("REC-060", "Cable UTP categoría 6")
indice.insertar("REC-085", "Cautín de estación")
indice.insertar("REC-020", "Sensor ultrasónico")
indice.insertar("REC-035", "Protoboard de alta densidad")
indice.insertar("REC-065", "Kit de resistencias variables")

    # Demostración del rango solicitado
indice.en_rango("REC-035", "REC-065")