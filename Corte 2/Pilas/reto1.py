class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class PilaEnlazada:
    def __init__(self):
        self._cima = None  # Apunta al tope de la pila
        self._tamanio = 0

    def apilar(self, x):
        nuevo = Nodo(x)
        nuevo.siguiente = self._cima
        self._cima = nuevo
        self._tamanio += 1

    def desapilar(self):
        if self.vacia():
            return None
        dato = self._cima.dato
        self._cima = self._cima.siguiente
        self._tamanio -= 1
        return dato

    def cima(self):
        return None if self.vacia() else self._cima.dato

    def vacia(self):
        return self._cima is None

# Ejemplo de uso:
p = PilaEnlazada()
p.apilar(10)
p.apilar(20)
p.apilar(30)

print(p.desapilar())  # 30 
print(p.cima())       # 20
print(p.vacia())      # False