from PyQt5.QtWidgets import QApplication

# import backend
from backend.logica_inicio import LogicaInicio
from backend.logica_principal import LogicaPrincipal
from backend.logica_juego import LogicaJuego
from backend.elementos_juego import *

# import frontend
from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_principal import VentanaPrincipal
from frontend.ventana_juego import VentanaJuego
from frontend.ventana_postronda import VentanaPostronda
from frontend.ventana_ranking import VentanaRanking

# codigo inspirado desde dccubitos en AS3


class DCCruz(QApplication):
    def __init__(self, argv) -> None:
        super().__init__(argv)

        # instanciar ventanas
        self.ventana_inicio = VentanaInicio()
        self.ventana_principal = VentanaPrincipal()
        self.ventana_juego = VentanaJuego()
        self.ventana_postronda = VentanaPostronda()
        self.ventana_ranking = VentanaRanking()

        # conectar signals

        self.conectar_inicio()
        self.conectar_principal()
        self.conectar_juego()
        self.conectar_postronda()
        self.conectar_ranking()

    def conectar_inicio(self):
        self.ventana_inicio.senal_login.connect(self.logica_inicio.comprobar_usuario)
        pass

    def conectar_principal(self):
        pass

    def conectar_juego(self):
        pass

    def conectar_postronda(self):
        pass

    def conectar_ranking(self):
        pass

    def iniciar(self):
        self.ventana_inicio.show()
        pass
