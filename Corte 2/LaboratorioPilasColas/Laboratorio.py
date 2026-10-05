# PARTE A — La cola de atención sobre lista enlazada

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ColaEnlazada:
    def __init__(self):
        self.frente = None
        self.fin = None
        self._tamano = 0

    def encolar(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self.frente = nuevo
            self.fin = nuevo
        else:
            self.fin.siguiente = nuevo
            self.fin = nuevo
        self._tamano += 1

    def desencolar(self):
        if self.esta_vacia():
            return None
        dato = self.frente.dato
        self.frente = self.frente.siguiente
        self._tamano -= 1
        if self.frente is None:
            self.fin = None
        return dato

    def ver_frente(self):
        if self.esta_vacia():
            return None
        return self.frente.dato

    def tamano(self):
        return self._tamano

    def esta_vacia(self):
        return self.frente is None

# PARTE B — El deshacer (Pila de operaciones)
class SistemaRecursos:
    def __init__(self):
        self.recursos_disponibles = {"LibroA", "LibroB", "Laptop1"}
        self.recursos_prestados = set()
        self.pila_operaciones = []  # Pila LIFO para registrar operaciones

    def prestar_recurso(self, recurso):
        if recurso in self.recursos_disponibles:
            self.recursos_disponibles.remove(recurso)
            self.recursos_prestados.add(recurso)
            self.pila_operaciones.append(("PRESTAMO", recurso))
            print(f"[Préstamo] Recurso '{recurso}' entregado.")
        else:
            print(f"[Aviso] El recurso '{recurso}' no está disponible.")

    def deshacer(self):
        """Deshace la última operación real, revirtiendo su estado."""
        if not self.pila_operaciones:
            print("[Aviso] No hay operaciones para deshacer.")
            return
        
        operacion, recurso = self.pila_operaciones.pop()
        if operacion == "PRESTAMO":
            self.recursos_prestados.remove(recurso)
            self.recursos_disponibles.add(recurso)
            print(f"[Deshacer] Se revirtió el préstamo. '{recurso}' vuelve a estar disponible.")

# PREGUNTAS

# 1. En una cola sobre lista enlazada, saco el último elemento. ¿Qué dos referencias tengo que actualizar y por qué?
# R/ Si sacas el único elemento que quedaba (o sea, la cola se vacía), tienes que actualizar tanto 
#    el 'frente' como el 'fin' a None. ¿Por qué? Porque ya no hay nodos en la cola, y si dejas esas 
#    referencias apuntando al nodo viejo, vas a tener problemas y la cola va a seguir creyendo que tiene cosas.
#
# 2. En una cola circular de capacidad cinco, el frente está en tres y hay cuatro elementos. ¿En qué posición se guarda el siguiente que encole?
# R/ Se guarda en la posición 2. 
#    Haciendo la cuenta con la fórmula circular: (frente 3 + cantidad 4) % capacidad 5 = 7 % 5 = 2.
#
# 3. Quiero deshacer las últimas tres operaciones. ¿Pila o cola? ¿Por qué?
# R/ Una Pila. 
#    Porque como necesitas deshacer lo último que hiciste, la estructura tiene que seguir la regla 
#    del último en entrar, primero en salir.
#
# 4. Quiero atender por orden de llegada. ¿Pila o cola?
# R/ Una Cola. 
#    Porque los primeros que llegan tienen que ser los primeros en ser atendidos, respetando el orden tal cual llegaron.

print(" PARTE A: COLA DE ATENCIÓN ")
cola = ColaEnlazada()
cola.encolar("Cliente 1")
cola.encolar("Cliente 2")
    
print(f"Frente actual: {cola.ver_frente()} | Tamaño: {cola.tamano()}")
print(f"Desencolado: {cola.desencolar()}")
print(f"Desencolado: {cola.desencolar()}")
print(f"¿Cola vacía?: {cola.esta_vacia()}")

print("\nPRUEBA EXPLÍCITA: VACIAR Y VOLVER A ENCOLAR")
cola.encolar("Cliente 3")
cola.encolar("Cliente 4")
print(f"Frente tras re-encolar: {cola.ver_frente()} | Tamaño: {cola.tamano()}")
print(f"Desencolado: {cola.desencolar()}")
print(f"Desencolado: {cola.desencolar()}")
print(f"¿Cola vacía al final?: {cola.esta_vacia()}")

print("\n PARTE B: SISTEMA DE DESHACER")
sistema = SistemaRecursos()
sistema.prestar_recurso("LibroA")
sistema.prestar_recurso("Laptop1")
print(f"Recursos disponibles: {sistema.recursos_disponibles}")

print("\nEjecutando acción de deshacer")
sistema.deshacer()  # Debe devolver Laptop1 a disponible
print(f"Recursos disponibles tras deshacer: {sistema.recursos_disponibles}")