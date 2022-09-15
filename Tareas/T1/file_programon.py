# archivo para definir al programon

import os


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
            self.experiencia = valor % 100

        else:
            self._experiencia = valor

    def entrenar(self):
        """Metodo donde se entrena al programon"""

        print("este menu todavía no está disponible")

        pass

    def luchar(self):
        pass
