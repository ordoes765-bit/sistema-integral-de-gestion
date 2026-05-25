# reservas.py
import logging
from excepciones import ReservaInvalida

# Configuración de logs
logging.basicConfig(
    filename="logs.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Reserva:
    """
    Clase Reserva que integra Cliente y Servicio.
    Permite confirmar, cancelar y manejar errores con robustez.
    """

    def __init__(self, cliente, servicio, duracion):
        if not cliente or not servicio:
            raise ReservaInvalida("Cliente o servicio inválido.")
        if duracion <= 0:
            raise ReservaInvalida("La duración debe ser positiva.")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):
        try:
            costo = self.servicio.calcular_costo(self.duracion)
            self.estado = "Confirmada"
            return f"Reserva confirmada para {self.cliente.nombre}. Costo: {costo}"
        except Exception as e:
            logging.error(f"Error en confirmación de reserva: {e}")
            raise

    def cancelar(self):
        try:
            self.estado = "Cancelada"
            return f"Reserva cancelada para {self.cliente.nombre}."
        except Exception as e:
            logging.error(f"Error al cancelar reserva: {e}")
            raise

    def procesar(self):
        """
        Método que simula el procesamiento de la reserva.
        """
        try:
            if self.estado == "Pendiente":
                return self.confirmar()
            elif self.estado == "Confirmada":
                return "La reserva ya está confirmada."
            elif self.estado == "Cancelada":
