from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap
from parametros import RUTA_LOGO

import parametros as p


class VentanaInicio(QWidget):

    senal_enviar_login = pyqtSignal(str, str)

    def __init__(self) -> None:
        super().__init__()
        # Geometría
        self.setGeometry(600, 200, 500, 500)
        self.setWindowTitle("Ventana de Inicio")
        self.setStyleSheet("background-color: lightblue;")
        self.crear_elementos()

    def crear_elementos(self) -> None:

        # COMPLETAR

        # Logo [QLabel]
        self.logo = QLabel(self)
        self.logo.setGeometry(20, 20, 100, 100)
        imagen = QPixmap(RUTA_LOGO)
        self.logo.setPixmap(imagen)
        # preguntar por setScaledContents = true y (20, 20, 100, 100)!!!!

        # Usuario [QLabel] [QLineEdit]
        self.nombre = QLabel("Ingresa tu nombre de usuario", self)
        self.nombre.setGeometry(20, 150, 200, 20)
        self.username = QLineEdit("", self)
        self.username.setGeometry(20, 180, 200, 20)

        # Ingrese su contraseña [QLabel] [debe ser oculta]
        self.contraseña = QLabel("Ingrese su contraseña", self)
        self.contraseña.setGeometry(20, 210, 200, 20)
        self.password = QLineEdit("", self)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setGeometry(20, 240, 200, 20)

        # Boton [QPushButton]
        self.boton = QPushButton("Iniciar Juego", self)
        self.boton.setGeometry(20, 270, 200, 20)
        self.boton.clicked.connect(self.enviar_login)

        pass

    def enviar_login(self) -> None:

        # COMPLETAR
        datos = (self.username, self.password)
        self.senal_enviar_login.emit(datos)
        pass

    def recibir_validacion(self, valid, errores: set) -> None:

        # COMPLETAR

        if valid:
            self.hide()

        else:
            if "usuario" in errores:
                self.username.setText("")
                self.username.setPlaceholderText("Usuario inválido")

            if "contraseña" in errores:
                self.password.setText("")
                self.password.setPlaceholderText("Contraseña inválida")

        pass
