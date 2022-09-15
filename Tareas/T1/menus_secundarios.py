# en este archivo se desarrollan todos los menus secundarios
# menus secundarios son los que nacen desde menu entrenadores

from file_entrenador_programon import Entrenador
from file_liga import LigaProgramon


def menu_entrenamiento(entrenador: Entrenador):
    """Menu desplegado en Entrenamiento"""

    programones = entrenador.programones

    print("\n" + "-" * 70)
    print(" " * 20 + "*** Menu de entrenamiento ***" + " " * 20)
    print("-" * 70)
    print("\n")

    print("[0] Salir")
    print("[1] Volver\n")

    for i in range(0, len(programones)):
        print(f"[{i + 2}] {programones[i].nombre}")

    print("\n")

    eleccion = input(
        "Ingrese el numero del programon que desea, 0 para Salir o 1 para Volver: "
    )

    while not eleccion.isdigit() or not int(eleccion) in range(0, len(programones) + 2):
        print(
            f"Su respuesta debe ser un numero entero entre 0 y {len(programones) + 2}\n"
        )
        eleccion = input(
            "Ingrese el numero del programon que desea, 0 para Salir o 1 para Volver: "
        )

    eleccion = int(eleccion)

    if eleccion == 0:
        print("Nos vemos en una próxima instancia")
        print("Saliendo...\n")
        exit()

    elif eleccion == 1:
        print("Volviendo al menu de entrenador...\n")

    else:
        print(f"programon {programones[(eleccion) - 2].nombre} seleccionado!")
        programon_seleccionado = programones[eleccion - 2]

        programon_seleccionado.entrenar(entrenador)


def menu_simular_ronda(entrenador: list, liga: LigaProgramon):
    """Menu desplegado en Simular ronda"""

    programones = entrenador.programones

    print("\n" + "-" * 70)
    print(" " * 20 + "*** Elige tu luchador ***" + " " * 20)
    print("-" * 70)
    print("\n")

    print("[0] Salir")
    print("[1] Volver\n")

    for i in range(0, len(programones)):
        print(f"[{i + 2}] {programones[i].nombre}")

    print("\n")

    eleccion = input(
        "Ingrese el numero del programon que desea, 0 para Salir o 1 para Volver: "
    )

    while not eleccion.isdigit() or not int(eleccion) in range(0, len(programones) + 2):
        print(
            f"Su respuesta debe ser un numero entero entre 0 y {len(programones) + 2}\n"
        )
        eleccion = input(
            "Ingrese el numero del programon que desea, 0 para Salir o 1 para Volver: "
        )

    eleccion = int(eleccion)

    if eleccion == 0:
        print("Nos vemos en una próxima instancia")
        print("Saliendo...\n")
        exit()

    elif eleccion == 1:
        print("Volviendo al menu de entrenador...\n")

    else:
        print(f"programon {programones[(eleccion) - 2].nombre} seleccionado!")
        programon_seleccionado = programones[eleccion - 2]
        liga.simular_ronda(entrenador, programon_seleccionado)


def menu_crear_objeto(entrenador: Entrenador):

    print("\n" + "-" * 70)
    print(" " * 20 + "*** Menu Objetos ***" + " " * 20)
    print("-" * 70)
    print("\n")

    print("[0] Salir")
    print("[1] Volver\n")
    print("[2] Baya")
    print("[3] Pocion")
    print("[4] Caramelo")

    print("\n")

    eleccion = input(
        "Ingrese el tipo de objeto que desea, 0 para Salir o 1 para Volver: "
    )

    while not eleccion.isdigit() or not int(eleccion) in range(0, 5):
        print(f"Su respuesta debe ser un numero entero entre 0 y 4\n")
        eleccion = input(
            "Ingrese el tipo de objeto que desea, 0 para Salir o 1 para Volver: "
        )

    eleccion = int(eleccion)

    if eleccion == 0:
        print("Nos vemos en una próxima instancia")
        print("Saliendo...\n")
        exit()

    elif eleccion == 1:
        print("Volviendo al menu de entrenador...\n")

    elif eleccion == 2:
        print("Has elegido una baya")
        pass

    elif eleccion == 3:
        print("Has elegido una pocion")
        pass

    elif eleccion == 4:
        print("Has elegido un caramelo")
        pass


def menu_usar_objeto(entrenador: Entrenador):
    """Menu para usar objetos"""

    objetos = entrenador.objetos

    print("\n" + "-" * 70)
    print(" " * 20 + "*** Objetos disponibles ***" + " " * 20)
    print("-" * 70)
    print("\n")

    print("[0] Salir")
    print("[1] Volver\n")

    for i in range(0, len(objetos)):
        print(f"[{i + 2}] {objetos[i].nombre}")

    print("\n")

    eleccion = input(
        "Ingrese el numero del objeto que desea, 0 para Salir o 1 para Volver: "
    )

    while not eleccion.isdigit() or not int(eleccion) in range(0, len(objetos) + 2):
        print(f"Su respuesta debe ser un numero entero entre 0 y {len(objetos) + 2}\n")
        eleccion = input(
            "Ingrese el numero del objeto que desea, 0 para Salir o 1 para Volver: "
        )

    eleccion = int(eleccion)

    if eleccion == 0:
        print("Nos vemos en una próxima instancia")
        print("Saliendo...\n")
        exit()

    elif eleccion == 1:
        print("Volviendo al menu de entrenador...\n")

    else:
        print(f"Objeto {objetos[(eleccion) - 2].nombre} seleccionado!")
        objeto_seleccionado = objetos[eleccion - 2]
        objeto_seleccionado.aplicar_objeto()
