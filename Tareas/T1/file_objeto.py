from random import randint, random
from parametros import (
    PROB_EXITO_BAYA,
    PROB_EXITO_CARAMELO,
    PROB_EXITO_POCION,
    AUMENTAR_ATAQUE_FUEGO,
    AUMENTO_DEFENSA,
    AUMENTAR_VIDA_PLANTA,
    AUMENTAR_VELOCIDAD_AGUA,
    PROB_EXITO_OBJETO,
    PROB_EXITO_BAYA,
    PROB_EXITO_POCION,
    PROB_EXITO_CARAMELO,
)


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

        programon.vida += self.aumento_vida
        programon.ataque += AUMENTAR_ATAQUE_FUEGO
        programon.defensa += AUMENTO_DEFENSA
        programon.vida += self.aumento_vida

        if programon.tipo == "Planta":
            programon.vida += AUMENTAR_VIDA_PLANTA

        print(f"Programon beneficiado {programon.nombre}")
        print(f"Objeto utilizado {self.nombre} de tipo {self.tipo}")
        print(f"Aumento de vida {self.aumento_vida}")
        print(
            f"La vida subió de {programon.vida - self.aumento_vida} a {programon.vida}"
        )
        print(f"Aumento de ataque {AUMENTAR_ATAQUE_FUEGO}")
        print(
            f"El ataque subió de {programon.ataque - AUMENTAR_ATAQUE_FUEGO} a {programon.ataque}"
        )
        print(f"Aumento de defensa {AUMENTO_DEFENSA}")
        print(
            f"La defensa subió de {programon.defensa - AUMENTO_DEFENSA} a {programon.defensa}"
        )
        print(f"Aumento de velocidad {AUMENTAR_VELOCIDAD_AGUA}")
        print(f"La velocidad subió de {programon.velocidad} a {programon.velocidad}")
        pass

    pass

    def crear_objeto(self, entrenador, tipo):

        if tipo == "Baya":

            if random() > PROB_EXITO_BAYA:
                print("No se pudo crear el objeto")

            else:
                objeto = Objeto("Baya", "Baya")
                print("Se creó el objeto")
                entrenador.objetos.append(objeto)

        elif tipo == "Pocion":

            if random() > PROB_EXITO_POCION:
                print("No se pudo crear el objeto")

            else:
                objeto = Objeto("Pocion", "Pocion")
                print("Se creó el objeto")
                entrenador.objetos.append(objeto)

        elif tipo == "Caramelo":

            if random() > PROB_EXITO_CARAMELO:
                print("No se pudo crear el objeto")

            else:
                objeto = Objeto("Caramelo", "Caramelo")
                print("Se creó el objeto")
                entrenador.objetos.append(objeto)

        return objeto
