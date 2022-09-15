# en este archivo abriremos el csv de entrenadores y los almacenaremos en una lista
# luego esta lista la visualizaremos en el menu principal

import menus_secundarios
from file_liga import LigaProgramon
from data import liga


def menu_inicio(entrenadores, objetos, programones, liga):
    """funcion para mostrar el menu de inicio"""

    print("\n" + "-" * 70)
    print(" " * 20 + "*** Menu de inicio ***" + " " * 20)
    print("-" * 70)
    print("\n")

    for i, entrenador in enumerate(entrenadores):

        lista_programones = ", ".join(p.nombre for p in entrenador.programones)

        print(f"[{i + 1}] {entrenador.nombre}: {lista_programones}")

    print("\n")
    print("[0] Salir")
    print("\n")
    eleccion = input("Ingrese el numero del entrenador que desea o 0 para Salir: ")

    while not eleccion.isdigit() or not int(eleccion) in range(0, len(entrenadores)):
        print(f"Su respuesta debe ser un numero entero entre 0 y {len(entrenadores)}\n")
        eleccion = input("Ingrese el numero del entrenador que desea o 0 para Salir: ")

    eleccion = int(eleccion)

    if eleccion == 0:
        print("Nos vemos en una próxima instancia")
        print("Saliendo...\n")
        exit()

    else:
        print("entrenador seleccionado!")
        print("Avanzando al menu de entrenadores...\n")

        return menu_entrenador(entrenadores[int(eleccion) - 1], liga)


def menu_entrenador(entrenador, liga):

    print("\n" + "-" * 70)
    print(" " * 20 + "*** Menu Entrenador ***" + " " * 20)
    print("-" * 70)
    print("\n")

    print("[0] Salir")
    print("[1] Volver\n")
    print("[2] Entrenamiento")
    print("[3] Simular ronda")
    print("[4] Resumen campeonato")
    print("[5] Crear objetos")
    print("[6] Utilizar objeto")
    print("[7] Estado entrenador\n")

    eleccion = input("Ingrese el numero del entrenador que desea o 0 para Salir: ")

    while not eleccion.isdigit() or not int(eleccion) in range(0, 8):
        print(f"Su respuesta debe ser un numero entero entre 0 y 7\n")
        eleccion = input("Ingrese el numero del entrenador que desea o 0 para Salir: ")

    if int(eleccion) == 0:
        print("Nos vemos en una próxima instancia")
        print("Saliendo...\n")
        exit()

    elif int(eleccion) == 1:
        print("Volviendo al menu de inicio...\n")
        return menu_inicio()

    elif int(eleccion) == 2:
        print("Avanzando al menu de entrenamiento...\n")
        menus_secundarios.menu_entrenamiento(entrenador)
        menu_entrenador(entrenador, liga)

    elif int(eleccion) == 3:
        print("Avanzando al menu de simulacion de ronda...\n")
        menus_secundarios.menu_simular_ronda(entrenador, liga)
        menu_entrenador(entrenador)

    elif int(eleccion) == 4:
        print("Avanzando al menu de resumen de campeonato...\n")
        liga.resumen_campeonato()
        menu_entrenador(entrenador, liga)

    elif int(eleccion) == 5:
        print("Avanzando al menu de creacion de objetos...\n")
        menus_secundarios.menu_crear_objetos(entrenador)

    elif int(eleccion) == 6:
        print("Avanzando al menu de uso de objetos...\n")
        menus_secundarios.menu_usar_objeto(entrenador)

    elif int(eleccion) == 7:
        print("Avanzando al menu de estado de entrenador...\n")
        entrenador.estado_entrenador()
        menu_entrenador(entrenador, liga)
