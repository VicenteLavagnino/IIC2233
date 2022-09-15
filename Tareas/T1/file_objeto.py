from random import randint
from parametros import PROB_EXITO_BAYA, PROB_EXITO_CARAMELO, PROB_EXITO_POCION


class Objeto:
    def __init__(self, nombre: str, tipo: str):
        self.nombre = nombre
        self.tipo = tipo  # Baya, Pocion, Caramelo
        self.costo = None
        self._probabilidad_efecto = None
        self._aumento_vida = None

    @property
    def probabilidad_efecto(self):

        if self.tipo == "Baya":
            self._probabilidad_efecto = PROB_EXITO_BAYA

        elif self.tipo == "Caramelo":
            self._probabilidad_efecto = PROB_EXITO_CARAMELO

        elif self.tipo == "Pocion":
            self._probabilidad_efecto = PROB_EXITO_POCION

    @property
    def aumento_vida(self):

        if self.tipo == "Baya":
            self._aumento_vida = randint(1, 10)

        elif self.tipo == "Pocion":
            self._aumento_vida = randint(1, 7)

        elif self.tipo == "Caramelo":
            self._aumento_vida = randint(1, 7)  # ARREGLAR

    def aplicar_objeto(self, entrenador, programon):

        print(f"Programon beneficiado {programon.nombre}")
        print(f"Objeto utilizado {self.nombre} de tipo {self.tipo}")

        print(f"Aumento de vida")
        pass

    pass
