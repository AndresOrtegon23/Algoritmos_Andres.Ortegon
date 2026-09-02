# ============================================================
#  Cívica Software  ·  TCK-5512  ·  Severidad P0  ·  PRODUCCION CAIDA
#  Sistema: TurnoJusto  —  El historial de atenciones esta corrupto.
#
#  Reportes de soporte:
#   - "Registre la primera atencion del dia y el sistema se cayo."
#   - "Deshice la ultima atencion y se borro todo el historial."
#   - "Busco un turno que si existe y me dice que no esta."
# ============================================================

class Nodo:
    def __init__(self, turno, modulo):
        self.turno = turno
        self.modulo = modulo
        self.siguiente = None


class Historial:
    def __init__(self):
        self.cabeza = None

    def registrar(self, turno, modulo):
        """Agrega una atencion al FINAL del historial.
           BUG: se cae cuando el historial esta vacio."""
        nuevo = Nodo(turno, modulo)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza        
            while actual.siguiente is not None:     #Si el historial no esta vacio, recorre la lista hasta el final
                actual = actual.siguiente       # Se mueve al siguiente nodo
            actual.siguiente = nuevo        #se agrega el nuevo nodo al final de la lista

    def deshacer_ultima(self):
        """Elimina la ULTIMA atencion registrada.
           Devuelve True si elimino algo, False si el historial estaba vacio.
           BUG: borra todo el historial."""
        if self.cabeza is None:         #Si el historial esta vacio, devuelve False
            return False
        if self.cabeza.siguiente is None:   #Si solo hay un elemento en el historial, lo elimina y devuelve True  
            self.cabeza = None
            return True
        actual = self.cabeza        #Si hay mas de un elemento en el historial, recorre la lista hasta el penultimo nodo
        while actual.siguiente.siguiente is not None:       #Mientras que el nodo siguiente del nodo actual no sea None
            actual = actual.siguiente       #Se mueve al siguiente nodo
        actual.siguiente = None     #Elimina el ultimo nodo de la lista y devuelve True
        return True

    def buscar(self, turno):
        """Devuelve el modulo que atendio ese turno, o None si no existe.
           PENDIENTE: implementar."""
        modulo = None       #Busca el turno en la lista y devuelve el modulo correspondiente, o None si no se encuentra
        actual = self.cabeza        #Si el historial esta vacio, devuelve None
        while actual is not None:       #Mientras que el nodo actual no es None
            if actual.turno == turno:       #Si el turno del nodo actual es igual al turno buscado, 
                modulo = actual.modulo      #Devuelve el modulo correspondiente
                break       #Si no, se mueve al siguiente nodo
            actual = actual.siguiente       #Si no se encuentra el turno, devuelve None
        return modulo       #Retorna el modulo correspondiente al turno buscado, o None si no se encuentra
    

    def cuantas(self):
        n = 0
        actual = self.cabeza
        while actual is not None:
            n += 1
            actual = actual.siguiente
        return n

    def listar(self):
        r = []
        actual = self.cabeza
        while actual is not None:
            r.append(actual.turno)
            actual = actual.siguiente
        return r
