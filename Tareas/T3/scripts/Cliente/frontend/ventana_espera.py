import sys
from PyQt5 import uic
from os.path import join
from helpers import json_reader
from PyQt5.QtCore import QTimer, pyqtSignal


window_name, base_class = uic.loadUiType(join(*json_reader("RUTA_VENTANA_ESPERA")))


class VentanaEspera(window_name, base_class):

    senal_avanzar_juego = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def abrir(self, username):
        print("abriendo ventana de espera")
        self.vista = True
        self.jugador1.setText(username)
        self.text_conteo.hide()
        self.show()

    def avanzar_juego(self, username, oponente):
        self.username = username
        self.oponente = oponente
        tiempo = json_reader("CUENTA_REGRESIVA_INICIO")
        self.text_conteo.setText(str(tiempo))
        self.jugador2.setText(oponente)
        self.text_conteo.show()

        self.start_timer()

        return True

    def ocultar(self):
        self.vista = False
        self.hide()

    def cerrar(self):
        self.vista = False
        self.close()

    # código inspirado en: https://stackoverflow.com/questions/40994187/pyqt-showing-countdown-timer

    def start_timer(self):
        self.tiempo_total = json_reader("CUENTA_REGRESIVA_INICIO")
        self.timer = QTimer()
        self.timer.timeout.connect(self.timeout_timer)
        self.timer.start(1000)

    def timeout_timer(self):
        self.tiempo_total -= 1
        self.text_conteo.setText(str(self.tiempo_total))

        if self.tiempo_total == 0:
            self.timer.stop()
            self.senal_avanzar_juego.emit(self.username, self.oponente)
            self.ocultar()
