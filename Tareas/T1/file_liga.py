# en este archivo se desarrolla la clase Liga Programon

from select import select
from file_entrenador import Entrenador
from file_programon import Programon


class LigaProgramon:
    """Clase para crear una liga de programones"""

    def __init__(self, entrenadores):
        """Constructor de la clase"""

        self.entrenadores = entrenadores  # list
        self.perdedores = []  # list
        self.ronda_actual = 1  # int
        self.campeon = None  # str
        self.continuan = []  # list

    def continuan_en_liga(self):
        """Metodo para obtener los entrenadores que siguen en la liga"""

        self.continuan = []

        for entrenador in self.entrenadores:
            if entrenador not in self.perdedores:
                self.continuan.append(f"{entrenador} ")

        self.continuan = self.continuan.strip(" ")

        return self.continuan

    def resumen_campeonato(self):
        """Metodo para visualizar el campeonato"""

        print(26 * " " + "Resumen Campeonato" + 26 * " ")
        print("-" * 70 + "\n")
        print("Participantes: " + self.entrenadores)
        print("Ronda actual: " + self.ronda_actual)
        print("Entrenadores que siguen en la liga:" + LigaProgramon.continuan_en_liga())

        # agregar : Luego de mostrar lo anterior,en caso de quedar más rondas, se volverá al Menú Entrenador. !!!!!!!
        # En otro caso, se avisa el resultado, se reinicia el programa y se vuelve al Menú de Inicio. !!!!!!!!!!

    def simular_ronda(entrenador: Entrenador, programon: Programon):
        """Metodo para simular una ronda"""

        entrenador.rondas_jugadas += 1

        if entrenador.rondas_jugadas == 4:
            pass

        pass
