# excepciones.py

class DatosInvalidos(Exception):
    """
    Excepción lanzada cuando los datos ingresados no cumplen con las validaciones.
    Ejemplo: correo sin '@', teléfono no numérico, etc.
    """
    pass


class ServicioNoDisponible(Exception):
    """
    Excepción lanzada cuando un servicio solicitado no está disponible
    o no cumple con los parámetros requeridos.
    """
    pass


class ReservaInvalida(Exception):
    """
    Excepción lanzada cuando una reserva no puede procesarse
    por datos incorrectos, parámetros faltantes o estado inválido.
    """
    pass
