#en este archivo se desarrolla la clase Liga Programon

class LigaProgramon:
    """Clase para crear una liga de programones"""

    def __init__(self, entrenadores):
        """Constructor de la clase"""

        self.entrenadores = entrenadores #list
        self.perdedores = [] #list
        self.ronda_actual = 1 #int
        self.campeon = None #str
        self.continuan = [] #list

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
