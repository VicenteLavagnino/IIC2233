# En este archivo se definen los parametros
import os
from random import randint, random

# JUEGO

SOLES_INICIALES = None

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

# SOLES

INTERVALO_APARICION_SOLES = None

# DIFICULTAD

PONDERADOR_NOCTURNO = 0.8
PONDERADOR_DIURNO = 0.9

# PUNTAJES

PUNTAJE_ZOMBIE_DIURNO = None
PUNTAJE_ZOMBIE_NOCTURNO = None
# por acabar con todos los zombies
# PUNTAJE_EXTRA = PUNTAJE RONDA * PONDERADOR_DIFICULTAD


# RUTAS

# puntajes
RUTA_PUNTAJES = os.path.join("puntajes.txt")

# ventanas (ui files)

RUTA_VENTANA_INICIO = os.path.join("frontend", "uic", "ventana_inicio.ui")
RUTA_VENTANA_PRINCIPAL = os.path.join("frontend", "uic", "ventana_principal.ui")
RUTA_VENTANA_JUEGO = os.path.join("frontend", "uic", "ventana_juego.ui")
RUTA_VENTANA_POSTRONDA = os.path.join("frontend", "uic", "ventana_postronda.ui")
RUTA_VENTANA_RANKING = os.path.join("frontend", "uic", "ventana_ranking.ui")

# imagen noche
RUTA_IMAGEN_NOCHE = os.path.join("frontend", "sprites", "Fondos", "salidaNocturna.png")


# sprites
