# Cliente.py
from Entidad import EntidadSistema

class Cliente(EntidadSistema):
    """
    Clase Cliente que hereda de EntidadSistema.
    Encapsula datos personales y valida la información ingresada.
    """

    def __init__(self, identificador, nombre, correo, telefono):
        super().__init__(identificador, nombre)

        # Validaciones
        if "@" not in correo or "." not in correo:
            raise ValueError("Correo inválido. Debe contener '@' y dominio.")
        if not telefono.isdigit():
            raise ValueError("Teléfono inválido. Debe contener solo números.")

        # Encapsulación de atributos
        self.__correo = correo
        self.__telefono = telefono

    def descripcion(self):
        """
        Devuelve una descripción textual del cliente.
        """
        return f"Cliente: {self.nombre}, Correo: {self.__correo}, Teléfono: {self.__telefono}"

    def __str__(self):
        return f"[Cliente ID: {self.identificador}] {self.nombre} - {self.__correo}"
