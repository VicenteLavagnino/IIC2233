# backend juego

from PyQt5.QtCore import QObject, pyqtSignal


class LogicaJuego(QObject):
    def __init__(self):
        super().__init__()

        self.usuario = None
        self.modo = None

    def get_usuario(self, usuario):
        self.usuario = usuario

    def get_modo(self, modo):
        self.modo = modo

    pass
