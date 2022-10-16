# backend de inicio de juego

from PyQt5.QtCore import QObject, pyqtSignal
from helpers import get_ranking

# codigo reutilizado de la AS3
class LogicaInicio(QObject):

    senal_respuesta_validacion = pyqtSignal(bool)  # (se puede)
    senal_abrir_principal = pyqtSignal(str)
    senal_usuario = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def validar_usuario(self, usuario: str) -> None:

        if usuario.isalnum() and usuario not in get_ranking() and usuario != "":

            self.senal_respuesta_validacion.emit(True)
            self.senal_abrir_principal.emit(usuario)
            self.senal_usuario.emit(usuario)

        else:
            self.senal_respuesta_validacion.emit(False)
