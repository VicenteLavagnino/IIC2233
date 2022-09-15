from time import sleep
from threading import Thread

from centro_urbano import CentroUrbano

from parametros import (
    ENERGIA_RECOLECTOR,
    ORO_RECOLECTADO,
    TIEMPO_RECOLECCION,
    TIEMPO_CONSTRUCCION,
    ORO_CHOZA,
)


# Completar
class Recolector(Thread):
    def __init__(self, nombre: str, centro_urbano: CentroUrbano) -> None:
        self.nombre = nombre
        self.centro_urbano = centro_urbano
        self.energia = ENERGIA_RECOLECTOR  # int
        self.oro = 0  # int

        # Completar
        self.daemon = True

    def run(self) -> None:
        self.trabajar()
        self.ingresar_oro()
        self.dormir()

    def log(self, mensage: str) -> None:
        print(f"El recolector {self.nombre}: {mensage}")

    def trabajar(self) -> None:
        # Completar
        self.log("El recolector ha comenzado a trabajar")

        while self.energia > 0:
            self.oro += ORO_RECOLECTADO
            self.log(f"Se han recolectado {ORO_RECOLECTADO} monedas de oro")
            self.energia -= 1
            sleep(TIEMPO_RECOLECCION)
        pass

    def ingresar_oro(self) -> None:
        # Completar
        centro_urbano = self.centro_urbano
        centro_urbano.oro += self.oro
        self.oro = 0
        self.log(
            f"El recolector ha ingresado {self.oro} monedas de oro al centro urbano"
        )
        self.log(f"El centro urbano tiene {centro_urbano.oro} monedas de oro")
        pass

    def dormir(self) -> None:
        self.log("ha terminado su turno, procede a mimir")


# Completar
class Constructor:
    def __init__(self, nombre, centro_urbano: CentroUrbano) -> None:
        self.nombre = nombre
        self.centro_urbano = centro_urbano
        # Completar

    def run(self) -> None:
        while self.retirar_oro():
            self.log("está construyendo una choza de bárbaros")
            sleep(TIEMPO_CONSTRUCCION)
            self.construir_choza()
        self.log("terminó su trabajo por el día")

    def log(self, mensage: str) -> None:
        print(f"El constructor {self.nombre}: {mensage}")

    def retirar_oro(self) -> bool:
        # Completar
        pass

    def construir_choza(self) -> None:
        # Completar
        pass
