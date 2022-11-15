import sys
from PyQt5 import uic
from os.path import join
from helpers import json_reader, name_error, name_error_server, name_error_server_full
from PyQt5.QtWidgets import QApplication, QLineEdit
from PyQt5.QtCore import pyqtSignal

window_name, base_class = uic.loadUiType(join(*json_reader("RUTA_VENTANA_INICIO")))


class VentanaInicio(window_name, base_class):

    senal_validar_usuario = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.vista = False

        self.pushButton_jugar.clicked.connect(self.validar_usuario)

    def abrir(self):
        self.vista = True
        self.show()

    def ocultar(self):
        self.vista = False
        self.hide()

    def cerrar(self):
        self.vista = False
        self.close()

    def validar_usuario(self):

        username = self.lineEdit.text()

        # validar que sea un nombre válido

        if username.isalnum() and 1 <= len(username) <= 10:
            self.senal_validar_usuario.emit(f"LOGIN;{username}")

        else:
            name_error(username)

    def error_name_full(self):
        name_error_server_full()

    def error_name_server(self):
        name_error_server()
