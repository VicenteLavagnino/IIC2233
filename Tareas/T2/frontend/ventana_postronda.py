# en este archivo se define el frontend de inicio

# codigo inspirado de contenidos --> Qtdesigner y AS3

import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSignal

from parametros import RUTA_VENTANA_POSTRONDA

"""
Creamos nuestra ventana principal heredando desde la GUI creada con Designer.
La función loadUiType retorna una tupla en donde el primer elemento
corresponde al nombre de la ventana definido en QtDesigner, y el segundo
elemento a la clase base de la GUI.
"""

window_name, base_class = uic.loadUiType(RUTA_VENTANA_POSTRONDA)


class VentanaPostronda(window_name, base_class):

    senal_salir = pyqtSignal()
    senal_siguiente_ronda = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_salir.clicked.connect(self.salir)
        self.pushButton_siguiente.clicked.connect(self.siguiente_ronda)

    def mostrar_ventana(self) -> None:
        self.show()
        pass

    def salir(self):
        self.senal_salir.emit()
        pass

    def siguiente_ronda(self):
        self.senal_siguiente_ronda.emit()
        self.hide()
        pass

    pass
