import sys
from PyQt5 import uic
from os.path import join
from helpers import json_reader, name_error, name_error_server, name_error_server_full
from PyQt5.QtWidgets import QApplication, QLineEdit
from PyQt5.QtCore import pyqtSignal

window_name, base_class = uic.loadUiType(join(*json_reader("RUTA_CHAT")))


class Chat(window_name, base_class):

    senal_enviar_mensaje = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.vista = False

        self.pushButton_enviar.clicked.connect(self.enviar_mensaje)

    def abrir(self):
        self.vista = True
        self.show()

    def ocultar(self):
        self.vista = False
        self.hide()

    def cerrar(self):
        self.vista = False
        self.close()

    def enviar_mensaje(self):

        mensaje = self.lineEdit.text()

        self.mensaje_jugador.setText(mensaje)
        self.senal_enviar_mensaje.emit(f"CHAT;{mensaje}")

    def recibir_mensaje(self, mensaje):
        self.mensaje_oponente.setText(mensaje)
