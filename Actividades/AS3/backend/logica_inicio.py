from PyQt5.QtCore import QObject, pyqtSignal
from parametros import CONTRASENAS_PROHIBIDAS


class LogicaInicio(QObject):

    senal_respuesta_validacion = pyqtSignal(bool, set)
    senal_abrir_juego = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def comprobar_usuario(self, usuario: str, contrasena: str) -> None:

        # COMPLETAR

        # ver si usuario es alfanumerico

        if usuario.isalnum():

            if contrasena not in CONTRASENAS_PROHIBIDAS:
                self.senal_abrir_juego.emit(usuario)
                self.senal_respuesta_validacion.emit(True, set())

            else:
                self.senal_respuesta_validacion.emit(False, {"contraseña"})

        elif not usuario.isalnum():

            if contrasena in CONTRASENAS_PROHIBIDAS:
                self.senal_respuesta_validacion.emit(False, {"usuario", "contraseña"})

            else:
                self.senal_respuesta_validacion.emit(False, {"usuario"})

        pass
