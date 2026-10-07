class TablaHash:
    def __init__(self, capacidad_inicial=8):
        self.cap = capacidad_inicial  # Capacidad inicial de la tabla
        self.cubetas = [[] for _ in range(self.cap)]  # Lista de cubetas
        self.n = 0  # Número de elementos en la tabla

    def hash(self, clave):
        # Función hash original (suma todos los caracteres)
        return sum(ord(c) for c in clave) % self.cap

    def hash_mala(self, clave):
        # Función hash mala (solo suma los 4 primeros caracteres)
        return sum(ord(c) for c in clave[:4]) % self.cap

    def factor_carga(self):
        return self.n / self.cap

    def insertar(self, clave, valor):
        if self.factor_carga() > 0.75:
            self.redimensionar()  # Redimensionar si supera el 75%

        i = self.hash(clave)
        for par in self.cubetas[i]:
            if par[0] == clave:
                par[1] = valor  # Actualiza el valor si la clave ya existe
                return
        self.cubetas[i].append([clave, valor])
        self.n += 1

    def buscar(self, clave):
        i = self.hash(clave)
        for k, v in self.cubetas[i]:
            if k == clave:
                return v
        return None

    def eliminar(self, clave):
        i = self.hash(clave)
        for idx, (k, _) in enumerate(self.cubetas[i]):
            if k == clave:
                self.cubetas[i].pop(idx)
                self.n -= 1
                return True
        return False

    def redimensionar(self):
        viejas = self.cubetas
        self.cap *= 2  # Duplicar la capacidad
        self.cubetas = [[] for _ in range(self.cap)]
        self.n = 0  # Se reinicia y se reconstruye con las inserciones
        for cubeta in viejas:
            for clave, valor in cubeta:
                self.insertar(clave, valor)


# Datos de los estudiantes
estudiantes = {
    "EST-2026-0101": "Ana Torres",
    "EST-2026-0102": "Carlos Rojas",
    "EST-2026-0103": "Diego Pardo",
    "EST-2026-0104": "Sofia Mejia",
    "EST-2026-0105": "Juan Gomez",
    "EST-2026-0106": "Maria Lopez",
    "EST-2026-0107": "Pedro Ruiz",
    "EST-2026-0108": "Camila Diaz",
    "EST-2026-0109": "Luis Herrera",
    "EST-2026-0110": "Valentina Cruz",
    "EST-2026-0111": "Andres Vega",
    "EST-2026-0112": "Laura Castro"
}

print(" Prueba con la funcion hash original")
tabla1 = TablaHash()

for codigo, valor in estudiantes.items():
    tabla1.insertar(codigo, valor)

print("Búsqueda de 'EST-2026-0107':", tabla1.buscar("EST-2026-0107"))
print("Capacidad final:", tabla1.cap)
print("Factor de carga final:", round(tabla1.factor_carga(), 2))

# Distribución detallada de cada cubeta
distribucion1 = [len(c) for c in tabla1.cubetas]
print("Distribución por cubeta:", distribucion1)
print("Cubeta más llena (tamaño máximo):", max(distribucion1))
print("Cubetas vacías:", sum(1 for c in tabla1.cubetas if len(c) == 0))


# Estadísticas claras para la Tabla 2 (Hash Malo)
print("\n Prueba con la funcion hash mala")
tabla2 = TablaHash()
tabla2.hash = tabla2.hash_mala  # Asignamos la función hash mala

for codigo, valor in estudiantes.items():
    tabla2.insertar(codigo, valor)

print("Búsqueda de 'EST-2026-0107':", tabla2.buscar("EST-2026-0107"))
print("Capacidad final:", tabla2.cap)
print("Factor de carga final:", round(tabla2.factor_carga(), 2))

# Distribución detallada de cada cubeta
distribucion2 = [len(c) for c in tabla2.cubetas]
print("Distribución por cubeta:", distribucion2)
print("Cubeta más llena (tamaño máximo):", max(distribucion2))
print("Cubetas vacías:", sum(1 for c in tabla2.cubetas if len(c) == 0))