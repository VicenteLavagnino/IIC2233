# backend de inicio de juego

from PyQt5.QtCore import QObject, pyqtSignal

# codigo reutilizado de la AS3
class LogicaInicio(QObject):

    senal_respuesta_validacion = pyqtSignal(bool)
    senal_abrir_juego = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def comprobar_usuario(self, usuario: str) -> None:

        if usuario.isalnum():

            self.senal_abrir_juego.emit(usuario)
            self.senal_respuesta_validacion.emit(True)

        elif not usuario.isalnum():
            self.senal_respuesta_validacion.emit(False)
