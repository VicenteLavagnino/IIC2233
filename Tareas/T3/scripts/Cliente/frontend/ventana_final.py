import sys
from PyQt5 import uic
from os.path import join
from helpers import json_reader


window_name, base_class = uic.loadUiType(join(*json_reader("RUTA_VENTANA_FINAL")))


class VentanaFinal(window_name, base_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.vista = False

        self.pushButton_volver.clicked.connect(self.volver)

    def abrir(self, ganador, usuario):
        self.vista = True

        if ganador == usuario:
            self.mensaje.setText("¡Felicidades, has ganado!")

        else:
            self.mensaje.setText("Has perdido :(, suerte para la próxima")

        self.show()

    def ocultar(self):
        self.vista = False
        self.hide()

    def cerrar(self):
        self.vista = False
        self.close()

    def volver(self):
        self.ocultar()
        pass

    def desconexion_repentina(self):

        self.vista = True
        self.mensaje.setText("¡Felicidades, has ganado!")
        self.show()

    def desconexion_servidor(self):

        self.vista = True
        self.mensaje.setText("Lo sentimos, hay un problema con el servidor :(")
        self.show()
