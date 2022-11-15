# este es el archivo main para Servidor

import sys
from servidor import Servidor
from helpers_s import json_reader

if __name__ == "__main__":

    HOST = json_reader("HOST")
    PORT = json_reader("PORT")
    servidor = Servidor(HOST, PORT)

    try:
        while True:
            print("\nPresione [ctrl + c] para salir del servidor\n")
            print("Esperando conexiones de cliente...")
            input()

    except KeyboardInterrupt:
        print("\nSaliendo del servidor...")
        print("Servidor cerrado con éxito!")
        print("Gracias por usar el programa!")
        print(
            "Presione [ctrl + c] para cerrar el terminal o simplemente cierre la ventana"
        )
        sys.exit(0)
