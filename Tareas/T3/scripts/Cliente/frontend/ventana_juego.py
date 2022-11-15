import sys
from PyQt5 import uic
from os.path import join
from helpers import json_reader
from random import choice


window_name, base_class = uic.loadUiType(join(*json_reader("RUTA_VENTANA_JUEGO")))


class VentanaJuego(window_name, base_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_select.clicked.connect(self.seleccionar)

    def abrir(self, username, oponente):

        cuenta_regresiva = json_reader("CUENTA_REGRESIVA_RONDA")

        self.vista = True
        self.name_oponente.setText(oponente)
        self.name_jugador.setText(username)
        self.numero.setText(str(cuenta_regresiva))
        self.tipo0.hide()
        self.tipo1.hide()
        self.tipoD0.hide()
        self.tipoD1.hide()
        self.tipoD2.hide()

        self.carta_jugador_numero.hide()
        self.carta_jugador_atrib.hide()
        self.show()

    def iniciar_turno(self):
        pass

    def seleccionar(self):
        pass
