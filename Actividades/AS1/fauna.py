from random import randint
from parametros import INCREMENTO_FEROCIDAD, MAX_EX_CARNIVORO, MAX_EX_HERVIBORO, \
                        MIN_EX_CARNIVORO, MIN_EX_HERVIBORO, INCREMENTO_ADORABILIDAD, \
                        GAN_CARNIVORO, GAN_HERBIVORO

# MODIFICAR

from abc import ABC, abstractmethod
import random
class Animal(ABC):

    # MODIFICAR
    def __init__(self, especie: str, **kwargs):

        self.especies = especie
        self.ganancia_actual = 0

        pass

    # MODIFICAR
    @abstractmethod
    def alimentarse(self):
        pass

    # MODIFICAR
    @abstractmethod
    def exhibicion(self):
        pass

    def __str__(self):
        return f"Animal de especie {self.especie}"


# MODIFICAR
class Carnivoro(Animal):

    # MODIFICAR
    def __init__(self, ferocidad, **kwargs):
        
        super().__init__(**kwargs)
        self.ferocidad = int(ferocidad)
        self.ganancia_actual += GAN_CARNIVORO
        pass

    # MODIFICAR
    def alimentarse(self):
        super().alimentarse()
        self.ferocidad += INCREMENTO_FEROCIDAD
        print(f"Animal {self.especie} se come un kilogramo de Carne") 


    # MODIFICAR
    def exhibicion(self):
        super().exhibicion()
        self.ganancia_actual += self.ferocidad * random.randint(MIN_EX_CARNIVORO, MAX_EX_CARNIVORO)


# MODIFICAR
class Herbivoro(Animal):

    # MODIFICAR
    def __init__(self, especie: str, adorabilidad: int, **kwargs):
        
        super().__init__(especie, **kwargs)
        self.adorabilidad = int(adorabilidad)
        self.ganancia_actual += GAN_HERBIVORO
        pass

    # MODIFICAR
    def alimentarse(self):
        super().alimentarse()
        self.adorabilidad += INCREMENTO_ADORABILIDAD
        print(f"Animal {self.especie} se come un kilogramo de vegetales")

    # MODIFICAR
    def exhibicion(self):
        super().exhibicion()
        self.ganancia_actual += self.adorabilidad * random.randint(MIN_EX_HERVIBORO, MAX_EX_HERVIBORO)

# MODIFICAR
class Omnivoro(Carnivoro, Herbivoro):

    # MODIFICAR
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass

    # MODIFICAR
    #ver si modificar o no! #####################
    def alimentarse(self):
        super().alimentarse()
        pass

    # MODIFICAR
    #ver si modificar o no! #####################
    def exhibicion(self):
        super().exhibicion()
        pass

