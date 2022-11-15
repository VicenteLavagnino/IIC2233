import json
from os.path import join
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox


def json_reader(key):
    """Lee el archivo json y retorna el valor de la llave"""
    ruta = join("parametros.json")

    with open(ruta, "r", encoding="UTF-8") as archivo:
        data = json.load(archivo)
    valor = data[key]
    return valor


# Código extraido de internet desde el siguiente link:
# https://pythonbasics.org/pyqt-qmessagebox/


def name_error(name):

    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText(
        f"El nombre {name} no es válido, recuerda que tu username debe tener entre 1 a 10 caracteres alfanuméricos"
    )
    msgBox.setWindowTitle("Error de usuario")
    msgBox.setStandardButtons(QMessageBox.Ok)

    returnValue = msgBox.exec()
    if returnValue == QMessageBox.Ok:
        print("OK clicked")


def name_error_server():

    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText(f"El nombre ya está en uso, por favor elige otro")
    msgBox.setWindowTitle("Error de servidor")
    msgBox.setStandardButtons(QMessageBox.Ok)

    returnValue = msgBox.exec()
    if returnValue == QMessageBox.Ok:
        print("OK clicked")


def name_error_server_full():

    print("El servidor está lleno")

    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText(f"El servidor está lleno, por favor intenta más tarde")
    msgBox.setWindowTitle("Error de servidor")
    msgBox.setStandardButtons(QMessageBox.Ok)

    returnValue = msgBox.exec()
    if returnValue == QMessageBox.Ok:
        print("OK clicked")
