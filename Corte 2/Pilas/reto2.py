class Prestamo:
    def __init__(self, id_prestamo, recurso, usuario):
        self.id_prestamo = id_prestamo
        self.recurso = recurso
        self.usuario = usuario

    def __str__(self):
        return f"Préstamo ID: {self.id_prestamo} | Recurso: {self.recurso} | Usuario: {self.usuario}"


class GestorPrestamos:
    def __init__(self):
        self.prestamos_activos = []  # Almacena los préstamos vigentes en el sistema
        self.pila_deshacer = []      # Pila (Stack) para registrar el historial de acciones

    def registrar_prestamo(self, id_prestamo, recurso, usuario):
        """Registra un nuevo préstamo y lo apila en la estructura de deshacer."""
        nuevo_prestamo = Prestamo(id_prestamo, recurso, usuario)
        
        # Agregamos a la lista principal de activos
        self.prestamos_activos.append(nuevo_prestamo)
        
        # Guardamos la acción en la pila (Última entrada, primera en salir)
        self.pila_deshacer.append(("REGISTRAR", nuevo_prestamo))
        
        print(f"[ÉXITO] Préstamo registrado: {nuevo_prestamo}")

    def deshacer_ultimo_prestamo(self):
        if not self.pila_deshacer:
            print("No hay acciones recientes en la pila para deshacer.")
            return None

        # Extraemos la última acción registrada de la pila (LIFO)
        accion, prestamo = self.pila_deshacer.pop()

        if accion == "REGISTRAR":
            # Reversión: eliminamos el préstamo correspondiente de los activos
            if prestamo in self.prestamos_activos:
                self.prestamos_activos.remove(prestamo)
            print(f"[DESHECHO] Se canceló el último préstamo: {prestamo}")
            return prestamo

        return None

    def mostrar_prestamos(self):
        print("\n Estado Actual: Préstamos Activos")
        if not self.prestamos_activos:
            print("No hay préstamos activos registrados.")
        else:
            for p in self.prestamos_activos:
                print(f" - {p}")
        print("-" * 42)


sistema = GestorPrestamos()

    # 1. Registramos algunos préstamos de recursos comunitarios
sistema.registrar_prestamo(101, "Proyector Epson", "Andrés Ortegón")
sistema.registrar_prestamo(102, "Cable HDMI", "Asier Arguinzones")
sistema.registrar_prestamo(103, "Portátil Core i7", "Camila Gómez")

    # Mostramos cómo va el sistema
sistema.mostrar_prestamos()

    # 2. Aplicamos el requerimiento de Línea 1: Deshacer el último préstamo
print("\n> Ejecutando operación 'Deshacer'")
sistema.deshacer_ultimo_prestamo()

    # Mostramos el estado posterior al deshacer
sistema.mostrar_prestamos()

    # 3. Podemos deshacer de nuevo si lo requerimos
print("\n> Ejecutando otra operación 'Deshacer'")
sistema.deshacer_ultimo_prestamo()

sistema.mostrar_prestamos()