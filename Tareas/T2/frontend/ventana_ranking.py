# en este archivo se define el frontend de inicio

# codigo inspirado de contenidos --> Qtdesigner y AS3

import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSignal

from parametros import RUTA_VENTANA_RANKING

"""
Creamos nuestra ventana principal heredando desde la GUI creada con Designer.
La función loadUiType retorna una tupla en donde el primer elemento
corresponde al nombre de la ventana definido en QtDesigner, y el segundo
elemento a la clase base de la GUI.
"""

window_name, base_class = uic.loadUiType(RUTA_VENTANA_RANKING)


class VentanaRanking(window_name, base_class):

    senal_volver = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_volver.clicked.connect(self.volver)

    def mostrar_ventana(self) -> None:
        self.show()

    def volver(self):
        self.hide()
        self.senal_volver.emit()
        pass

    pass
