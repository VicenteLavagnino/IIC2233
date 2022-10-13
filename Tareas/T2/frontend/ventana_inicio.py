# en este archivo se define el frontend de inicio

# codigo inspirado de contenidos --> Qtdesigner y AS3

import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QLineEdit
from PyQt5.QtCore import pyqtSignal


from parametros import RUTA_VENTANA_INICIO

"""
Creamos nuestra ventana principal heredando desde la GUI creada con Designer.
La función loadUiType retorna una tupla en donde el primer elemento
corresponde al nombre de la ventana definido en QtDesigner, y el segundo
elemento a la clase base de la GUI.
"""

window_name, base_class = uic.loadUiType(RUTA_VENTANA_INICIO)


class VentanaInicio(window_name, base_class):

    senal_login = pyqtSignal(str)
    senal_ranking = pyqtSignal(int)
    senal_salir = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_jugar.clicked.connect(self.enviar_login)
        self.pushButton_ranking.clicked.connect(self.ver_ranking)
        self.pushButton_salir.clicked.connect(self.salir)

    def enviar_login(self):
        self.senal_login.emit(self.lineEdit_usuario.text())

    def ver_ranking(self):
        self.senal_ranking.emit(0)
        pass

    def salir(self):
        self.senal_salir.emit(1)
        pass

    def recibir_validacion(self, validacion):

        if not validacion:

            self.lineEdit = QLineEdit("Usuario invalido")

        else:
            pass

    pass
