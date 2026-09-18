# Definición de la clase Nodo para la lista enlazada
class Nodo:
    def __init__(self, valorDato):
        self.valorDato = valorDato
        self.siguienteNodo = None

# Función recursiva para recorrer e imprimir la lista en orden inverso
def imprimirInverso(nodoActual):
    # Caso base: si llegamos al final de la lista (nodo vacío), detenemos la recursión
    if nodoActual is None:
        return
    
    # Paso recursivo: bajamos hasta el final de la lista primero
    imprimirInverso(nodoActual.siguienteNodo)
    
    # Imprimimos DESPUÉS de la llamada recursiva (aprovechando el desapilado)
    print(nodoActual.valorDato)

# Ejemplo de uso:
# Construimos la lista enlazada: 1 -> 2 -> 3 -> None
nodoUno = Nodo(1)
nodoDos = Nodo(2)
nodoTres = Nodo(3)

nodoUno.siguienteNodo = nodoDos
nodoDos.siguienteNodo = nodoTres

# Ejecutamos la función de impresión inversa
imprimirInverso(nodoUno)