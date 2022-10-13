from ast import Str
from parametros import RUTA_PUNTAJES


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


agregar_ranking("usuario", 10)
agregar_ranking("aaao", 99)
agregar_ranking("aabo", 50)
