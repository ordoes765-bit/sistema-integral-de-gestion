# Entidad.py
from abc import ABC, abstractmethod

class EntidadSistema(ABC):
    """Entidad abstracta del sistema.

    Las clases que hereden de EntidadSistema deben implementar
    el método descripcion().
    """

    def __init__(self, identificador: int, nombre: str):
        if not isinstance(identificador, int):
            raise ValueError("El identificador debe ser un número entero válido.")
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre debe ser una cadena de texto no vacía.")

        self.identificador = identificador
        self.nombre = nombre

    @abstractmethod
    def descripcion(self) -> str:
        """Devuelve una descripción textual de la entidad."""
        raise NotImplementedError("Las subclases deben implementar descripcion().")

    def __str__(self) -> str:
        return f"EntidadSistema [ID: {self.identificador}, Nombre: {self.nombre}]"

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(identificador={self.identificador!r}, nombre={self.nombre!r})"
        )


class Usuario(EntidadSistema):
    """Ejemplo de entidad concreta que hereda de EntidadSistema."""

    def descripcion(self) -> str:
        return f"Usuario con ID {self.identificador} y nombre {self.nombre}."


if __name__ == "__main__":
    usuario = Usuario(1, "Ana")
    print(usuario)
    print(usuario.descripcion())
