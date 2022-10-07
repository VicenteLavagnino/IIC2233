# EN ESTE ARCHIVO SE CONSTRUYEN CLASES PARA EL JUEGO

from abc import ABC, abstractmethod

from parametros import (
    DANO_MORDIDA,
    DANO_PROYECTIL,
    INTERVALO_DISPARO,
    INTERVALO_TIEMPO_MORDIDA,
    INTERVALOS_APARICION_SOLES,
    VELOCIDAD_ZOMBIE,
    VIDA_PLANTA,
    RALENTIZAR_ZOMBIE,
    INTERVALO_SOLES_GIRASOL,
    CANTIDAD_SOLES,
    PONDERADOR_DIURNO,
    PONDERADOR_NOCTURNO,
    VIDA_ZOMBIE,
)

from aparicion_zombies import intervalo_aparicion

# en esta parte me inspiré del código de la AS1

############################################
# CONSTRUCCÍON DE CLASES PRINCIPALES


class Planta(ABC):
    """Clase abstracta para las plantas"""

    def __init__(self, precio_soles, ubicacion):

        self.precio_soles = precio_soles
        self.ubicacion = ubicacion

        self.vida = VIDA_PLANTA


class Zombie(ABC):
    """Clase abstracta para los zombies"""

    def __init__(self, ubicacion, ronda, hora):

        self.ubicacion = ubicacion
        self.ronda = ronda

        if hora == "diurno":
            self.ponderador = PONDERADOR_DIURNO
        elif hora == "nocturno":
            self.ponderador = PONDERADOR_NOCTURNO

        self.vida = VIDA_ZOMBIE
        self.velocidad = VELOCIDAD_ZOMBIE
        self.dano_mordida = DANO_MORDIDA
        self.intervalo_tiempo_mordida = INTERVALO_TIEMPO_MORDIDA

        pass


class Soles:
    """Clase para los soles"""

    def __init__(self):

        self.intervalo_aparicion = INTERVALOS_APARICION_SOLES


############################################
# CONSTRUCCIÓN DE SUBCLASES

# PLANTAS


class PlantaClasica(Planta):
    """Clase para las plantas clasicas"""

    def __init__(self, precio_soles, ubicacion):

        super().__init__(precio_soles, ubicacion)

        self.intervalo_disparo = INTERVALO_DISPARO
        self.dano_proyectil = DANO_PROYECTIL


class PlantaAzul(Planta):
    """Clase para las plantas azules"""

    def __init__(self, precio_soles, ubicacion):

        super().__init__(precio_soles, ubicacion)

        self.intervalo_disparo = INTERVALO_DISPARO
        self.dano_proyectil = DANO_PROYECTIL
        self.ralentizar_zombie = RALENTIZAR_ZOMBIE


class Girasol(Planta):
    """Clase para las plantas girasoles"""

    def __init__(self, precio_soles, ubicacion):

        super().__init__(precio_soles, ubicacion)

        self.intervalo_soles = INTERVALO_SOLES_GIRASOL
        self.cantidad_soles = CANTIDAD_SOLES


class PlantaPatata(Planta):
    """Clase para las plantas patatas"""

    def __init__(self, precio_soles, ubicacion):

        super().__init__(precio_soles, ubicacion)
        self.vida = 2 * VIDA_PLANTA


# ZOMBIES


class ZombieClasico(Zombie):
    """Clase para los zombies clasicos"""

    def __init__(self, nombre, vida, ataque, defensa, velocidad, costo):

        super().__init__(nombre, vida, ataque, defensa, velocidad, costo)


class ZombieRapido(Zombie):
    """Clase para los zombies rapidos"""

    def __init__(self, ubicacion, ronda, hora):

        super().__init__(ubicacion, ronda, hora)
        self.velocidad = 2 * VELOCIDAD_ZOMBIE
        pass
