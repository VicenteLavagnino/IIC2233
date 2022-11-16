import sys
from PyQt5 import uic
from os.path import join
from helpers import json_reader
from PyQt5.QtCore import QTimer, pyqtSignal
from PyQt5.QtGui import QPixmap
from random import choice, randint
from cartas import get_penguins


window_name, base_class = uic.loadUiType(join(*json_reader("RUTA_VENTANA_JUEGO")))


class VentanaJuego(window_name, base_class):

    senal_enviar_carta = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cartas = dict()
        self.orden = list()
        self.carta = dict()

        self.pushButton_select.clicked.connect(self.seleccionar)

    def abrir(self, username, oponente):

        self.cartas = get_penguins()
        self.orden = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        print(self.cartas)

        cuenta_regresiva = json_reader("CUENTA_REGRESIVA_RONDA")

        self.vista = True
        self.name_oponente.setText(oponente)
        self.name_jugador.setText(username)
        self.numero.setText(str(cuenta_regresiva))
        self.esperando_respuesta.hide()
        self.tipo0.hide()
        self.tipo1.hide()
        self.tipoD0.hide()
        self.tipoD1.hide()
        self.tipoD2.hide()
        self.mostrar_carta()
        self.jugar_ronda()
        self.show()

    def jugar_ronda(self):
        self.start_timer()
        pass

    def seleccionar(self):
        self.esperando_respuesta.show()

    def iniciar_turno(self):
        pass

    def start_timer(self):
        self.tiempo_total = json_reader("CUENTA_REGRESIVA_RONDA")
        self.timer = QTimer()
        self.timer.timeout.connect(self.timeout_timer)
        self.timer.start(1000)

    def timeout_timer(self):
        self.tiempo_total -= 1
        self.numero.setText(str(self.tiempo_total))

        if self.tiempo_total == 0:
            self.timer.stop()

    def mostrar_carta(self):

        ruta0 = [
            "..",
            "..",
            "sprites",
            "cartas",
            f'{self.cartas["0"]["color"]}_{self.cartas["0"]["elemento"]}_{self.cartas["0"]["puntos"]}.png',
        ]

        print(ruta0)

        carta0 = QPixmap(join(*ruta0))
        self.table_card0.setPixmap(carta0)

        ruta1 = [
            "..",
            "..",
            "sprites",
            "cartas",
            f'{self.cartas["1"]["color"]}_{self.cartas["1"]["elemento"]}_{self.cartas["1"]["puntos"]}.png',
        ]

        carta1 = QPixmap(join(*ruta1))
        self.table_card1.setPixmap(carta1)

        ruta2 = [
            "..",
            "..",
            "sprites",
            "cartas",
            f'{self.cartas["2"]["color"]}_{self.cartas["2"]["elemento"]}_{self.cartas["2"]["puntos"]}.png',
        ]

        carta2 = QPixmap(join(*ruta2))
        self.table_card2.setPixmap(carta2)

        ruta3 = [
            "..",
            "..",
            "sprites",
            "cartas",
            f'{self.cartas["3"]["color"]}_{self.cartas["3"]["elemento"]}_{self.cartas["3"]["puntos"]}.png',
        ]

        carta3 = QPixmap(join(*ruta3))
        self.table_card3.setPixmap(carta3)

        ruta4 = [
            "..",
            "..",
            "sprites",
            "cartas",
            f'{self.cartas["4"]["color"]}_{self.cartas["4"]["elemento"]}_{self.cartas["4"]["puntos"]}.png',
        ]

        carta4 = QPixmap(join(*ruta4))
        self.table_card4.setPixmap(carta4)

        self.repaint()

        pass

    def carta_seleccionada(self, ubicacion):
        self.carta = self.cartas[self.orden[ubicacion]]
        self.orden.append(self.orden.pop(ubicacion))

    def jugar_carta(self):

        if self.Button0.isChecked():
            self.carta_seleccionada(0)

        elif self.Button1.isChecked():
            self.carta_seleccionada(1)

        elif self.Button2.isChecked():
            self.carta_seleccionada(2)

        elif self.Button3.isChecked():
            self.carta_seleccionada(3)

        elif self.Button4.isChecked():
            self.carta_seleccionada(4)

        else:
            seleccion = randint(0, 4)
            self.carta_seleccionada(seleccion)

        mensaje = f"JUGARCARTA;{self.carta['color']};{self.carta['elemento']};{self.carta['puntos']}"
        self.senal_enviar_carta.emit(mensaje)
