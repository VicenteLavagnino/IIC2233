from random import randint, choice, random
from fauna import Carnivoro, Herbivoro, Omnivoro
from parametros import MULTIPLICADOR_RECAUDACION, EVENTO_HERBIVOROS \
                        ,EVENTO_CARNIVOROS, FEROCIDAD, ADORABILIDAD \
                        ,PROBABILIDAD_EVENTO, VISITANTES


# MODIFICAR

from abc import ABC, abstractmethod
import fauna
class Atraccion(ABC):

    def __init__(self, numero):
        self.id = numero
        self.animales = []
        self.especies_disponibles = {"Carnivoro":[], "Herbivoro":[], "Omnivoro":[]}
        self.cargar_especies("especimenes.csv")

    def cargar_especies(self, ruta_archivo):
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo.readlines():
                tipo, especie = linea.strip("\n").split(",")
                self.especies_disponibles[tipo].append(especie)

    def alimentar_animales(self):
        for animal in self.animales:
            animal.alimentarse()

    # MODIFICAR
    @property.getter
    def visitantes(self) -> int:
        return random.randint(VISITANTES[0], VISITANTES[1])

    # MODIFICAR
    #arreglarrrrrrrrrrrrrrrrrrrrrrrrrr
    @property.getter
    def recaudacion(self):
        dinero = 0

        for animal in self.animales:
            animal.alimentarse()
            dinero += animal.ganancia_actual

        dinero = dinero * self.visitantes * MULTIPLICADOR_RECAUDACION

        return dinero

    # MODIFICAR   
    def crear_animales(self) -> int:
        pass
      
    # MODIFICAR  
    def __str__(self):
        pass

    # MODIFICAR
    def evento(self):
        pass


# MODIFICAR
class GranjaHerbivoros:

    # MODIFICAR
    def __init__(self, *args, **kwargs):
        pass

    def crear_animales(self):
        tipo = choice(["Herbivoro", "Omnivoro"])
        especies = self.especies_disponibles[tipo]
        seleccionada = choice(especies)
        if tipo == "Herbivoro":
            animal = Herbivoro(especie=seleccionada, adorabilidad=randint(*ADORABILIDAD))
        elif tipo == "Omnivoro":
            animal = Omnivoro(especie=seleccionada, adorabilidad=randint(*ADORABILIDAD), \
                             ferocidad=randint(*FEROCIDAD))
        self.animales.append(animal)

    # MODIFICAR
    def __str__(self):
        pass
    
    # MODIFICAR
    def evento(self):
        pass
        

# MODIFICAR
class PaseoCarnivoros:

    # MODIFICAR
    def __init__(self, *args, **kwargs):
        pass

    def crear_animales(self):
        tipo = choice(["Carnivoro", "Omnivoro"])
        especies = self.especies_disponibles[tipo]
        seleccionada = choice(especies)
        if tipo == "Carnivoro":
            animal = Carnivoro(especie=seleccionada, ferocidad=randint(*FEROCIDAD))
        elif tipo == "Omnivoro":
            animal = Omnivoro(especie=seleccionada, adorabilidad=randint(*ADORABILIDAD), \
                             ferocidad=randint(*FEROCIDAD))
        self.animales.append(animal)

    # MODIFICAR
    def __str__(self):
        pass
    
    # MODIFICAR
    def evento(self):
        pass
