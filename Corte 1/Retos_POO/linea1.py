# Módulo de gestión de préstamos y recursos para biblioteca

class Usuario:
    # Clase que representa a un usuario del sistema y gestiona sus sanciones
    def __init__(self, nombre, documento):
        # Inicializa los atributos protegidos del usuario
        self._nombre = nombre                  # Nombre completo del usuario
        self._documento = documento            # Documento de identidad del usuario
        self._tiene_sanciones = False          # Estado de sanción (False = sin sanciones por defecto)

    def puede_solicitar(self):
        # Verifica si el usuario está habilitado para realizar una solicitud de préstamo
        # Retorna True si no tiene sanciones activas; False en caso contrario
        return not self._tiene_sanciones


class Recurso:
    # Clase que representa un material o recurso prestable en la biblioteca
    def __init__(self, codigo, categoria):
        # Inicializa los atributos protegidos del recurso
        self._codigo = codigo                  # Código identificador del recurso
        self._categoria = categoria            # Categoría a la que pertenece el recurso
        self._disponible = True                # Estado de disponibilidad (True = libre por defecto)

    def ocupar(self):
        # Cambia el estado del recurso a no disponible al ser prestado
        self._disponible = False

    def liberar(self):
        # Restablece el estado del recurso a disponible al ser devuelto
        self._disponible = True


class Prestamo:
    # Clase que gestiona la transacción de préstamo asociando un usuario y un recurso
    def __init__(self, usuario, recurso, fecha):
        # Asocia los objetos y la fecha de la transacción mediante agregación/composición
        self._usuario = usuario                # Objeto de la clase Usuario asociado al préstamo
        self._recurso = recurso                # Objeto de la clase Recurso prestado
        self._fecha = fecha                    # Fecha en la que se registra el préstamo