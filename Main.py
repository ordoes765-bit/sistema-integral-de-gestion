# main.py
from cliente import Cliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reservas import Reserva
from excepciones import DatosInvalidos, ReservaInvalida, ServicioNoDisponible

def ejecutar_pruebas():
    operaciones = []

    # 1. Cliente válido
    try:
        c1 = Cliente(1, "Ana", "ana@mail.com", "123456")
        operaciones.append(c1.descripcion())
    except Exception as e:
        operaciones.append(f"Error: {e}")

    # 2. Cliente inválido (correo incorrecto)
    try:
        c2 = Cliente(2, "Luis", "correo_invalido", "987654")
        operaciones.append(c2.descripcion())
    except Exception as e:
        operaciones.append(f"Error detectado: {e}")

    # 3. Cliente inválido (teléfono no numérico)
    try:
        c3 = Cliente(3, "Maria", "maria@mail.com", "tel123")
        operaciones.append(c3.descripcion())
    except Exception as e:
        operaciones.append(f"Error detectado: {e}")

    # 4. Reserva de sala válida
    try:
        s1 = ReservaSala("Sala de reuniones", 50)
        r1 = Reserva(c1, s1, 3)
        operaciones.append(r1.confirmar())
    except Exception as e:
        operaciones.append(f"Error: {e}")

    # 5. Reserva de sala inválida (horas negativas)
    try:
        s2 = ReservaSala("Sala pequeña", 40)
        r2 = Reserva(c1, s2, -2)
        operaciones.append(r2.confirmar())
    except Exception as e:
        operaciones.append(f"Error detectado: {e}")

    # 6. Alquiler de equipo válido
    try:
        s3 = AlquilerEquipo("Proyector", 100)
        r3 = Reserva(c1, s3, 2)
        operaciones.append(r3.confirmar())
        operaciones.append(r3.cancelar())
    except Exception as e:
        operaciones.append(f"Error: {e}")

    # 7. Alquiler de equipo inválido (días = 0)
    try:
        s4 = AlquilerEquipo("Laptop", 80)
        r4 = Reserva(c1, s4, 0)
        operaciones.append(r4.confirmar())
    except Exception as e:
        operaciones.append(f"Error detectado: {e}")

    # 8. Asesoría especializada válida
    try:
        s5 = AsesoriaEspecializada("Consultoría IA", 200)
        r5 = Reserva(c1, s5, 5)
        operaciones.append(r5.confirmar())
    except Exception as e:
        operaciones.append(f"Error: {e}")

    # 9. Asesoría especializada inválida (horas negativas)
    try:
        s6 = AsesoriaEspecializada("Consultoría Big Data", 150)
        r6 = Reserva(c1, s6, -3)
        operaciones.append(r6.confirmar())
    except Exception as e:
        operaciones.append(f"Error detectado: {e}")

    # 10. Procesar reserva ya confirmada
    try:
        r7 = Reserva(c1, s1, 2)
        operaciones.append(r7.confirmar())
        operaciones.append(r7.procesar())  # Ya confirmada
    except Exception as e:
        operaciones.append(f"Error: {e}")

    # Mostrar resultados
    for i, op in enumerate(operaciones, start=1):
        print(f"Operación {i}: {op}")

if __name__ == "__main__":
    ejecutar_pruebas()

