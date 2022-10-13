# en este archivo se crearan las clases de plantas, zombies y soles principales

from parametros import (
    CANTIDAD_SOLES,
    DANO_ZOMBIE,
    INTERVALO_SOLES_GIRASOL,
    INTERVALO_TIEMPO_MORDIDA,
    RALENTIZAR_ZOMBIE,
    VELOCIDAD_ZOMBIE,
    VIDA_PLANTA,
    INTERVALO_DISPARO,
    DANO_PROYECTIL,
    VIDA_ZOMBIE,
)

# PLANTAS


class PlantaClasica:
    def __init__(self, dispara, precio, ubicacion) -> None:

        self.dispara = dispara
        self.precio = precio
        self.ubicacion = ubicacion

        self.vida = VIDA_PLANTA

        if self.dispara:
            self.intervalo_disparo = INTERVALO_DISPARO
            self.dano_proyectil = DANO_PROYECTIL


class PlantaAzul(PlantaClasica):
    def __init__(self, dispara, precio, ubicacion) -> None:

        super().__init__(dispara, precio, ubicacion)

        self.ralentizar = RALENTIZAR_ZOMBIE
        pass


class Girasol(PlantaClasica):
    def __init__(self, dispara, precio, ubicacion) -> None:

        super().__init__(dispara, precio, ubicacion)

        self.intervalo_soles = INTERVALO_SOLES_GIRASOL
        self.cantidad_soles = CANTIDAD_SOLES


class Patata(PlantaClasica):
    def __init__(self, dispara, precio, ubicacion) -> None:

        super().__init__(dispara, precio, ubicacion)
        self.vida = 2 * VIDA_PLANTA


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# ZOMBIES


class ZombieClasico:
    def __init__(self, ubicacion) -> None:

        self.ubicacion = ubicacion

        self.vida = VIDA_ZOMBIE
        self.velocidad = VELOCIDAD_ZOMBIE
        self.dano = DANO_ZOMBIE
        self.intervalo_mordida = INTERVALO_TIEMPO_MORDIDA


class ZombieRapido(ZombieClasico):
    def __init__(self, ubicacion) -> None:

        super().__init__(ubicacion)

        self.velocidad = 1.5 * VELOCIDAD_ZOMBIE


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# SOLES


class Sol:
    def __init__(self, ubicacion) -> None:

        self.ubicacion = ubicacion
