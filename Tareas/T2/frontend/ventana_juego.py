# en este archivo se define el frontend de inicio

# codigo inspirado de contenidos --> Qtdesigner y AS3

import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QPixmap
from helpers import estoy_dentro

from parametros import RUTA_VENTANA_JUEGO, RUTA_IMAGEN_NOCHE

"""
Creamos nuestra ventana principal heredando desde la GUI creada con Designer.
La función loadUiType retorna una tupla en donde el primer elemento
corresponde al nombre de la ventana definido en QtDesigner, y el segundo
elemento a la clase base de la GUI.
"""

window_name, base_class = uic.loadUiType(RUTA_VENTANA_JUEGO)


class VentanaJuego(window_name, base_class):

    senal_click = pyqtSignal(int, int)

    senal_iniciar_juego = pyqtSignal()
    senal_comprobar_avanzar = pyqtSignal()
    senal_avanzar = pyqtSignal()
    senal_cerrar_juego = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setMouseTracking(True)

        self.pushButton_iniciar.clicked.connect(self.iniciar_juego)
        self.pushButton_salir.clicked.connect(self.salir)
        self.pushButton_avanzar.clicked.connect(self.comprobar_avanzar)

    def traduccion_coordenadas(self, x: int, y: int):

        # girasol
        if estoy_dentro((0, 20), (x, y), (100, 70)):
            return ("plantas", "girasol")

        # planta
        elif estoy_dentro((0, 90), (x, y), (100, 70)):
            return ("plantas", "planta")

        # planta hielo

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            x = event.pos().x()
            y = event.pos().y()
            self.click_pantalla.emit(x, y)

    def mostrar_ventana(self, modo: str) -> None:

        if modo == "dia":
            self.show()
            pass

        elif modo == "noche":

            imagen_noche = QPixmap(RUTA_IMAGEN_NOCHE)
            self.label_juego.setPixmap(imagen_noche)
            self.show()
            pass

    def iniciar_juego(self):
        self.senal_iniciar_juego.emit()
        pass

    def avanzar(self, requisito: bool) -> None:

        if requisito:
            self.senal_avanzar.emit()
            self.hide()

        else:
            pass

    def comprobar_avanzar(self) -> None:

        self.senal_comprobar_avanzar.emit()
        pass

    def salir(self):
        self.senal_cerrar_juego.emit()
        pass

    pass
