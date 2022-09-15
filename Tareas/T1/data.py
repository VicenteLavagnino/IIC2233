import os
from file_entrenador_programon import Entrenador, Programon
from file_objeto import Objeto
from file_liga import LigaProgramon


def read_csv(ruta: str) -> list[list[str]]:
    """funcion para abrir un archivo csv y almacenarlo en una lista de listas"""

    lista = []
    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            lista.append(linea.split(","))

        return lista[1:]


def abrir_entrenadores(
    programones: list[Programon], objetos: list[Objeto]
) -> list[Entrenador]:
    """funcion para abrir el archivo entrenadores.csv y almacenarlos en una lista"""

    ruta = os.path.join("datasets", "entrenadores.csv")

    lista_entrenadores = read_csv(ruta)

    entrenadores = []

    for linea in lista_entrenadores:

        nombres_programones = linea[1].split(";")
        programones_entrenador = []

        for nombre_programon in nombres_programones:
            for programon in programones:
                if nombre_programon == programon.nombre:
                    programones_entrenador.append(programon)

        nombres_objetos = linea[3].split(";")
        objetos_entrenador = []

        for nombre_objeto in nombres_objetos:
            for objeto in objetos:
                if nombre_objeto == objeto.nombre:
                    objetos_entrenador.append(objeto)

        entrenadores.append(
            Entrenador(
                linea[0], programones_entrenador, int(linea[2]), objetos_entrenador
            )
        )

    return entrenadores


def abrir_programones() -> list[Programon]:
    """funcion para abrir el archivo programones y almacenarlos en una lista de clase"""

    # programones.csv = nombre,tipo,nivel,vida,ataque,defensa,velocidad

    ruta = os.path.join("datasets", "programones.csv")
    lista_programones = read_csv(ruta)

    programones = []

    for linea in lista_programones:
        programones.append(
            Programon(
                linea[0],
                linea[1],
                int(linea[2]),
                int(linea[3]),
                int(linea[4]),
                int(linea[5]),
                int(linea[6]),
            )
        )

    return programones


def abrir_objetos() -> list[Objeto]:
    """funcion para abrir el archivo objetos y almacenarlos en una lista"""

    # objetos.csv = nombre,tipo

    ruta = os.path.join("datasets", "objetos.csv")
    lista_objetos = read_csv(ruta)

    objetos = []

    for linea in lista_objetos:
        objetos.append(Objeto(linea[0], linea[1]))

    return objetos


programones = abrir_programones()
objetos = abrir_objetos()
entrenadores = abrir_entrenadores(programones, objetos)
liga = LigaProgramon(entrenadores)

if __name__ == "__main__":
    print(entrenadores)
    print(programones)
    print(objetos)
