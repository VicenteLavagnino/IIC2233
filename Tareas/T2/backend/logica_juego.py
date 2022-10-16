# backend juego

from PyQt5.QtCore import QObject, pyqtSignal
from backend.elementos_juego import Juego


class LogicaJuego(QObject):

    senal_avanzar = pyqtSignal(bool)
    senal_siguiete_ronda = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.usuario = None
        self.modo = None
        self.juego = None

    def get_usuario(self, usuario):
        self.usuario = usuario

    def get_modo(self, modo):
        self.modo = modo
        self.juego = Juego(self.modo, self.usuario)

    def comprobar_avanzar(self):

        # agregar logica de avanzar

        if True == True:

            self.senal_avanzar.emit(True)

        elif True == False:

            self.senal_avanzar.emit(False)

    def siguiente_ronda(self):

        # agregar logica

        self.senal_siguiete_ronda.emit(self.modo)
        pass

        pass

    def iniciar_juego(self):

        pass

    pass
