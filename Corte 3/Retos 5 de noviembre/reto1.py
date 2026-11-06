class Nodo:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
        self.izq = None
        self.der = None


class IndiceRecursos:
    def __init__(self):
        self.raiz = None
        self.n = 0

    def insertar(self, codigo, nombre):
        nuevo = Nodo(codigo, nombre)
        self.n += 1
        if self.raiz is None:
            self.raiz = nuevo
            return
        actual = self.raiz
        while True:
            if codigo < actual.codigo:          # SIEMPRE se compara por código
                if actual.izq is None:
                    actual.izq = nuevo
                    return
                actual = actual.izq
            elif codigo > actual.codigo:
                if actual.der is None:
                    actual.der = nuevo
                    return
                actual = actual.der
            else:                                # código repetido: actualiza nombre
                actual.nombre = nombre
                self.n -= 1
                return

    def listarOrdenado(self):
        """Inorden: izquierda, nodo, derecha. Ordenado por código sin sort."""
        def inorden(nodo):
            if nodo is None:
                return
            inorden(nodo.izq)
            print(f"  {nodo.codigo:>4}  {nodo.nombre}")
            inorden(nodo.der)
        print("LISTADO ORDENADO POR CÓDIGO")
        inorden(self.raiz)

    def informe(self, codigo):
        comparaciones = 0
        actual = self.raiz
        while actual is not None:
            comparaciones += 1
            if codigo == actual.codigo:
                print(f"  [{codigo}] {actual.nombre}  ({comparaciones} comparaciones)")
                return
            actual = actual.izq if codigo < actual.codigo else actual.der
        print(f"  [{codigo}] no encontrado  ({comparaciones} comparaciones)")


# Orden de inserción desordenado a propósito (evita un árbol degenerado)
RECURSOS = [
    (203, "macbook pro"),
    (104, "estructuras de datos"),
    (304, "raspberry pi 4"),
    (101, "matemáticas discretas"),
    (107, "inteligencia artificial"),
    (206, "video beam epson"),
    (302, "multímetro digital"),
    (201, "computador portátil dell"),
    (208, "ipad air"),
    (301, "calculadora científica"),
    (303, "arduino uno kit"),
    (307, "mouse"),
]

indice = IndiceRecursos()
for codigo, nombre in RECURSOS:
    indice.insertar(codigo, nombre)

print(f"{indice.n} recursos insertados\n")
indice.listarOrdenado()

print("\nCONSULTAS")
for c in (203, 307, 208, 250, 999):
        indice.informe(c)