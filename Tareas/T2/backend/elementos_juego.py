# en este archivo se crearan las clases de plantas, zombies y soles principales

from PyQt5.QtCore import QObject
from random import random
from aparicion_zombies import intervalo_aparicion
from time import time
from parametros import (
    CANTIDAD_SOLES,
    DANO_ZOMBIE,
    INTERVALO_APARICION_SOLES,
    INTERVALO_SOLES_GIRASOL,
    INTERVALO_TIEMPO_MORDIDA,
    PONDERADOR_DIURNO,
    PONDERADOR_NOCTURNO,
    RALENTIZAR_ZOMBIE,
    SOLES_INICIALES,
    VELOCIDAD_ZOMBIE,
    VIDA_PLANTA,
    INTERVALO_DISPARO,
    DANO_PROYECTIL,
    VIDA_ZOMBIE,
)

# JUEGO


class Juego(QObject):
    def __init__(self, modo, usuario):
        super().__init__()
        self.tablero = [
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
        ]

        self.ronda = 1
        self.modo = modo
        self.usuario = usuario
        self.soles = SOLES_INICIALES
        self.nivel = 0
        self.puntaje = 0
        self.zombies_destruidos = 0
        self.zombies_restantes = 0
        self.ponderador_difficultad = self.ponderador()

        self.plantas = []
        self.zombies = []

    def ponderador(self):
        if self.modo == "dia":
            return PONDERADOR_DIURNO
        elif self.modo == "noche":
            return PONDERADOR_NOCTURNO

    def agregar_planta(self, planta: classmethod) -> None:

        self.tablero[planta.ubicacion[1]][planta.ubicacion[0]] = planta
        pass

    def aparicion_soles(self):

        lugar = random.randint(0, 20)

        if lugar <= 9:
            lugar = [0, lugar]
        elif lugar >= 10:
            lugar = [1, lugar - 10]

        if self.tablero[lugar[1]][lugar[0]] == "":
            self.tablero[lugar[1]][lugar[0]] = "sol"
            time.sleep(INTERVALO_APARICION_SOLES)
        else:
            self.aparicion_soles()

    def agregar_zombies(self):

        intervalo_aparicion(self.ronda, self.modo)


# PLANTAS
class PlantaClasica(QObject):
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


class ZombieClasico(QObject):
    def __init__(self, ubicacion) -> None:
        super().__init__()
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


class Sol(QObject):
    def __init__(self, ubicacion) -> None:
        super().__init__()
        self.ubicacion = ubicacion
        self.vida = 1  # 0 si muere
