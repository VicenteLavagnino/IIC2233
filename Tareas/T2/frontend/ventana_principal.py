from pydoc import classname


# en este archivo se define el frontend de inicio

# codigo inspirado de contenidos --> Qtdesigner y AS3

import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSignal

from parametros import RUTA_VENTANA_PRINCIPAL

"""
Creamos nuestra ventana principal heredando desde la GUI creada con Designer.
La función loadUiType retorna una tupla en donde el primer elemento
corresponde al nombre de la ventana definido en QtDesigner, y el segundo
elemento a la clase base de la GUI.
"""

window_name, base_class = uic.loadUiType(RUTA_VENTANA_PRINCIPAL)


class VentanaPrincipal(window_name, base_class):

    senal_modo = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_seguir.clicked.connect(self.enviar_modo)

    def mostrar_ventana(self) -> None:
        self.show()

    def enviar_modo(self):

        if self.radioButton_dia.isChecked():
            self.senal_modo.emit("dia")
            self.hide()

        elif self.radioButton_noche.isChecked():
            self.senal_modo.emit("noche")
            self.hide()

    pass
