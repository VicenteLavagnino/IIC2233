# en este archivo se define el frontend de inicio

# codigo inspirado de contenidos --> Qtdesigner y AS3

import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap

from parametros import RUTA_VENTANA_JUEGO, RUTA_IMAGEN_NOCHE

"""
Creamos nuestra ventana principal heredando desde la GUI creada con Designer.
La función loadUiType retorna una tupla en donde el primer elemento
corresponde al nombre de la ventana definido en QtDesigner, y el segundo
elemento a la clase base de la GUI.
"""

window_name, base_class = uic.loadUiType(RUTA_VENTANA_JUEGO)


class VentanaJuego(window_name, base_class):

    senal_iniciar_juego = pyqtSignal(str)
    senal_cerrar_juego = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # salir
        self.pushButton_salir.clicked.connect(self.salir)

    def mostrar_ventana(self, modo: str) -> None:

        if modo == "dia":
            self.show()
            pass

        elif modo == "noche":

            imagen_noche = QPixmap(RUTA_IMAGEN_NOCHE)
            self.label_juego.setPixmap(imagen_noche)
            self.show()
            pass

    def salir(self):
        self.senal_cerrar_juego.emit()
        pass

    pass
