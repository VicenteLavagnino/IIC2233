# En este archivo se definen los parametros
import os
from random import randint, random

# PLANTAS

VIDA_PLANTA = None
INTERVALO_DISPARO = None
DANO_PROYECTIL = None

# planta azul
RALENTIZAR_ZOMBIE = None

# girasol
INTERVALO_SOLES_GIRASOL = None
CANTIDAD_SOLES = None


# ZOMBIES

VIDA_ZOMBIE = None
VELOCIDAD_ZOMBIE = None
DANO_ZOMBIE = None
INTERVALO_TIEMPO_MORDIDA = None


# RUTAS

# puntajes
RUTA_PUNTAJES = os.path.join("puntajes.txt")

# ventanas (ui files)

RUTA_VENTANA_INICIO = os.path.join("frontend", "uic", "ventana_inicio.ui")
RUTA_VENTANA_PRINCIPAL = os.path.join("frontend", "uic", "ventana_principal.ui")
RUTA_VENTANA_JUEGO = os.path.join("frontend", "uic", "ventana_juego.ui")
RUTA_VENTANA_POSTRONDA = os.path.join("frontend", "uic", "ventana_postronda.ui")
RUTA_VENTANA_RANKING = os.path.join("frontend", "uic", "ventana_ranking.ui")


# sprites
