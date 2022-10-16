from parametros import RUTA_PUNTAJES
from PyQt5.QtWidgets import QPushButton, QMessageBox


def agregar_ranking(usuario: str, puntaje: int):

    with open(RUTA_PUNTAJES, "a", encoding="utf-8") as archivo:

        archivo.write(usuario + "," + str(puntaje) + "\n")

        archivo.close()

    actualizar_ranking()


def actualizar_ranking():

    with open(RUTA_PUNTAJES, "r", encoding="utf-8") as archivo:

        puntajes = archivo.readlines()

        ranking_ordenado = []

        for puntaje in puntajes:
            puntaje = puntaje.split(",")
            puntaje[1] = puntaje[1].strip()
            ranking_ordenado.append(puntaje)
            ranking_ordenado.sort(key=orden, reverse=True)

    with open(RUTA_PUNTAJES, "w", encoding="utf-8") as archivo:

        for puntaje in ranking_ordenado:
            archivo.write(puntaje[0] + "," + puntaje[1] + "\n")

        archivo.close()


def get_ranking():

    with open(RUTA_PUNTAJES, "r", encoding="utf-8") as archivo:

        puntajes = archivo.readlines()

        ranking_ordenado = []

        for puntaje in puntajes:
            puntaje = puntaje.split(",")
            ranking_ordenado.append(puntaje)
            ranking_ordenado.sort(key=orden, reverse=True)

        return ranking_ordenado


def orden(line):
    return int(line[1])


# Código extraido de internet desde el siguiente link:
# https://pythonbasics.org/pyqt-qmessagebox/


def pop_error(Error: str):

    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText(Error)
    msgBox.setWindowTitle("QMessageBox")
    msgBox.setStandardButtons(QMessageBox.Ok)

    returnValue = msgBox.exec()
    if returnValue == QMessageBox.Ok:
        print("OK clicked")


def estoy_dentro(pos_esquina, pos_mouse, tamano: tuple):

    if (
        pos_esquina[0] < pos_mouse[0] < pos_esquina[0] + tamano[0]
        and pos_esquina[1] < pos_mouse[1] < pos_esquina[1] + tamano[1]
    ):
        return True
    else:
        return False
