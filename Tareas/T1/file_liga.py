# en este archivo se desarrolla la clase Liga Programon

from select import select
from file_entrenador_programon import Entrenador, Programon
from random import choice


class LigaProgramon:
    """Clase para crear una liga de programones"""

    def __init__(self, entrenadores):
        """Constructor de la clase"""

        self.entrenadores = entrenadores  # list
        self.perdedores = []  # list
        self.ronda_actual = 1  # int
        self.campeon = None  # str
        self._continuan = []  # list

    @property
    def continuan(self):
        """Metodo para obtener los entrenadores que siguen en la liga"""

        self.continuan = []

        for entrenador in self.entrenadores:
            if entrenador not in self.perdedores:
                self.continuan.append(f"{entrenador} ")

        self.continuan = self.continuan.strip(" ")

        return self._continuan

    def resumen_campeonato(self):
        """Metodo para visualizar el campeonato"""

        print(26 * " " + "Resumen Campeonato" + 26 * " ")
        print("-" * 70 + "\n")
        print("Participantes: " + self.entrenadores)
        print("Ronda actual: " + self.ronda_actual)
        print("Entrenadores que siguen en la liga:" + self.continuan_en_liga())

        eleccion = input(
            "Presione cualquier tecla para volver al menu de entrenadores: "
        )

        pass

    def simular_ronda(self, entrenador: Entrenador, programon: Programon):
        """Metodo para simular una ronda"""

        entrenador.rondas_jugadas += 1

        if entrenador.rondas_jugadas >= 4:
            pass

        else:
            # generar pares
            entrenadores_disponibles = self.entrenadores.copy()
            entrenadores_disponibles.remove(entrenador)

            oponente = choice(entrenadores_disponibles)
            entrenadores_disponibles.remove(oponente)

            lista_pares = [
                [
                    (entrenador, programon),
                    (oponente, oponente.choice(oponente.programones)),
                ]
            ]

            while len(entrenadores_disponibles) > 0:

                rival1 = choice(entrenadores_disponibles)
                entrenadores_disponibles.remove(rival1)
                rival2 = choice(entrenadores_disponibles)
                entrenadores_disponibles.remove(rival2)

                lista_pares.append(
                    [
                        (rival1, rival1.choice(rival1.programones)),
                        (rival2, rival2.choice(rival2.programones)),
                    ]
                )

            for par in lista_pares:
                # simular pelea

                pass
