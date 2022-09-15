# archivo para definir al programon

import os
from file_entrenador import Entrenador
from parametros import (
    ENERGIA_ENTRENAMIENTO,
    MIN_AUMENTO_EXPERIENCIA,
    MAX_AUMENTO_EXPERIENCIA,
)
import random


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

    def entrenar(self, entrenador: Entrenador):
        """Metodo donde se entrena al programon"""

        entrenador.energia -= ENERGIA_ENTRENAMIENTO
        print(
            f"El entrenador ha gastado {ENERGIA_ENTRENAMIENTO} de energia, su energia actual es {entrenador.energia}"
        )

        experiencia = random.randint(MIN_AUMENTO_EXPERIENCIA, MAX_AUMENTO_EXPERIENCIA)
        self.experiencia(experiencia)  # nose si está bien

    def luchar(self):
        pass
