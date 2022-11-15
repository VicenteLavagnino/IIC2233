# este es el archivo main para Cliente
import sys
from PyQt5.QtWidgets import QApplication
from cliente import Cliente
from helpers import json_reader

if __name__ == "__main__":
    HOST = json_reader("HOST")
    PORT = json_reader("PORT")

    # agregar try except

    # Instancia de la aplicación
    juego = QApplication(sys.argv)
    # Instancia del cliente
    cliente = Cliente(HOST, PORT)

    sys.exit(juego.exec_())
