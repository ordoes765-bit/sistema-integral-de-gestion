# servicios.py
from abc import ABC, abstractmethod

class Servicio(ABC):
    """
    Clase abstracta que representa un servicio general.
    Todas las clases de servicios deben heredar de esta clase.
    """

    def __init__(self, nombre_servicio, costo_base):
        if not isinstance(nombre_servicio, str) or nombre_servicio.strip() == "":
            raise ValueError("El nombre del servicio debe ser una cadena válida.")
        if not isinstance(costo_base, (int, float)) or costo_base <= 0:
            raise ValueError("El costo base debe ser un número positivo.")
        
        self.nombre_servicio = nombre_servicio
        self.costo_base = costo_base

    @abstractmethod
    def calcular_costo(self, duracion):
        """
        Método abstracto que debe ser implementado por las clases derivadas.
        Calcula el costo del servicio según la duración o cantidad.
        """
        pass

    def descripcion(self):
        return f"Servicio: {self.nombre_servicio}, Costo base: {self.costo_base}"


# Subclases de Servicio
class ReservaSala(Servicio):
    def calcular_costo(self, horas):
        if horas <= 0:
            raise ValueError("La duración en horas debe ser positiva.")
        return self.costo_base * horas


class AlquilerEquipo(Servicio):
    def calcular_costo(self, dias):
        if dias <= 0:
            raise ValueError("La duración en días debe ser positiva.")
        return self.costo_base * dias


class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, horas):
        if horas <= 0:
            raise ValueError("La duración en horas debe ser positiva.")
        # Ejemplo: costo base por hora + 10% de recargo
        return (self.costo_base * horas) * 1.1
