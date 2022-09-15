# archivo para definir al programon

import os
from parametros import (
    ENERGIA_ENTRENAMIENTO,
    MIN_AUMENTO_EXPERIENCIA,
    MAX_AUMENTO_EXPERIENCIA,
)
import random

from file_objeto import Objeto


class Programon:
    def __init__(
        self,
        nombre: str,
        tipo: str,
        nivel: int,
        vida: int,
        ataque: int,
        defensa: int,
        velocidad: int,
    ):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.velocidad = velocidad
        self.megaevolucion = None  # BONUS
        self._experiencia = 0

    @property
    def experiencia(self):
        return self._experiencia

    @experiencia.setter
    def experiencia(self, valor):

        if valor >= 100:
            self.nivel += valor // 100

            if self.nivel == 100:
                self.experiencia = 0
                print("El programon ha llegado al nivel maximo")

            else:

                self.experiencia = valor % 100

                for nivel in range(0, valor // 100):

                    aumento = random.randint(
                        MIN_AUMENTO_EXPERIENCIA, MAX_AUMENTO_EXPERIENCIA
                    )

                    self.vida += aumento
                    self.ataque += aumento
                    self.defensa += aumento
                    self.velocidad += aumento

                print(f"El programon {self.nombre} ha ganado {valor} de experiencia")
                print(f"El programon {self.nombre} ha subido al nivel {self.nivel}")

        else:
            self._experiencia = valor
            print(f"El programon {self.nombre} ha ganado {valor} de experiencia")

    def entrenar(self, entrenador):
        """Metodo donde se entrena al programon"""

        entrenador.energia -= ENERGIA_ENTRENAMIENTO
        print(
            f"El entrenador ha gastado {ENERGIA_ENTRENAMIENTO} de energia, su energia actual es {entrenador.energia}"
        )

        valor_experiencia = random.randint(
            MIN_AUMENTO_EXPERIENCIA, MAX_AUMENTO_EXPERIENCIA
        )
        self.experiencia(valor_experiencia)

    def luchar(self, enemigo):
        """Metodo donde se lucha contra un programon enemigo"""

        ventaja_tipo = None
        ventaja_enemigo = None

        if self.tipo == "Fuego":

            if enemigo.tipo == "Agua":
                ventaja_tipo = -1
                ventaja_enemigo = 1

            elif enemigo.tipo == "Planta":
                ventaja_tipo = 1
                ventaja_enemigo = -1

            elif enemigo.tipo == "Fuego":
                ventaja_tipo = 0
                ventaja_enemigo = 0

        elif self.tipo == "Agua":

            if enemigo.tipo == "Agua":
                ventaja_tipo = 0
                ventaja_enemigo = 0

            elif enemigo.tipo == "Planta":
                ventaja_tipo = -1
                ventaja_enemigo = 1

            elif enemigo.tipo == "Fuego":
                ventaja_tipo = 1
                ventaja_enemigo = -1

        elif self.tipo == "Planta":

            if enemigo.tipo == "Agua":
                ventaja_tipo = 1
                ventaja_enemigo = -1

            elif enemigo.tipo == "Planta":
                ventaja_tipo = 0
                ventaja_enemigo = 0

            elif enemigo.tipo == "Fuego":
                ventaja_tipo = -1
                ventaja_enemigo = 1

        puntaje_programon = max(
            0,
            0.2 * self.vida
            + 0.3 * self.nivel
            + 0.15 * self.ataque
            + 0.15 * self.defensa
            + 0.2 * self.velocidad
            + ventaja_tipo * 40,
        )

        puntaje_enemigo = max(
            0,
            0.2 * enemigo.vida
            + 0.3 * enemigo.nivel
            + 0.15 * enemigo.ataque
            + 0.15 * enemigo.defensa
            + 0.2 * enemigo.velocidad
            + ventaja_tipo * 40,
        )


class Entrenador:
    def __init__(
        self,
        nombre: str,
        programones: list[Programon],
        energia: int,
        objetos: list[Objeto],
    ):
        """Constructor de la clase"""

        self.nombre = nombre
        self.programones = programones
        self.energia = energia
        self.objetos = objetos
        self.rondas_jugadas = 0

    def estado_entrenador(self):
        """Metodo para ver el estado del entrenador"""

        show_objetos = ""
        for objeto in self.objetos:
            show_objetos += objeto + ", "
        show_objetos = show_objetos.strip(", ")

        print("\n" + "-" * 70)
        print(" " * 20 + "*** Estado entrenador ***" + " " * 20)
        print("-" * 70)
        print("\n")
        print("Nombre: " + self.nombre)
        print("Energia: " + self.energia)
        print("Objetos: " + show_objetos)
        print("-" * 70)
        print(" " * 20 + "*** Programones ***" + " " * 20)
        print("-" * 70)
        print(f"Nombre    |    Tipo   |   NiveL  | Vida")
        print("-" * 70)
        for programon in self.programones:
            print(
                f"{programon.nombre}    |    {programon.tipo}   |   {programon.nivel}  | {programon.vida}"
            )

        print("\n")
        print("[0] Salir")
        print("[1] Volver\n")
        eleccion = input("Ingrese la opcion que desea para continuar, debe ser 0 o 1: ")

        while eleccion not in ["0", "1"]:
            print("Su respuesta debe ser 0 o 1")
            eleccion = input(
                "Ingrese la opcion que desea para continuar, debe ser 0 o 1: "
            )

        if eleccion == "0":
            print("Nos vemos en una próxima instancia")
            print("Saliendo...\n")
            exit()

        elif eleccion == "1":
            print("Volviendo al menu de entrenadores...\n")
