#en este archivo abriremos el csv de entrenadores y los almacenaremos en una lista
#luego esta lista la visualizaremos en el menu principal

from curses.ascii import isdigit
import os

def abrir_entrenadores():
    """funcion para abrir el archivo entrenadores.csv y almacenarlos en una lista"""
   
    lista_entrenadores = []
    ruta = os.path.join("datasets", "entrenadores.csv")
    with open(ruta, "r", encoding="utf-8") as archivo:

        lista = archivo.readlines()
        
        for linea in lista:
            linea = linea.strip()
            lista_entrenadores.append(linea)

        #[0] = entrenadores  [1] = programones [2] = energia [3] = objetos

        for lista in range (len(lista_entrenadores)):
            lista_entrenadores[lista] = str(lista_entrenadores[lista]).split(",")
            lista_entrenadores[lista][1] = lista_entrenadores[lista][1].split(";")
            lista_entrenadores[lista][3] = lista_entrenadores[lista][3].split(";")
        #formato final por linea es [entrenador, [programones], energia, [objetos]]
    return lista_entrenadores


def menu_inicio():
    """funcion para mostrar el menu de inicio"""

    lista_entrenadores = abrir_entrenadores()

    print("\n" + "-" * 70)
    print(" " * 20 + "*** Menu de inicio ***" + " " * 20)
    print("-" * 70)
    print("\n")

    for nlinea in range (1,len(lista_entrenadores)):

        programones = ""
        for programon in range (len(lista_entrenadores[nlinea][1])):
            programones += lista_entrenadores[nlinea][1][programon] + ", "
        
        print(f"[{nlinea}] {lista_entrenadores[nlinea][0]}: " + programones.strip(", "))
    
    print("\n")
    print("[0] Salir")
    print("\n")
    eleccion = input("Ingrese el numero del entrenador que desea o 0 para Salir: ")

    while not eleccion.isdigit() or eleccion in range (0, len(lista_entrenadores)):
        print(f"Su respuesta debe ser un numero entero entre 0 y {len(lista_entrenadores)}\n")
        eleccion = input("Ingrese el numero del entrenador que desea o 0 para Salir: ")

    if eleccion.isdigit() and eleccion in range (0, len(lista_entrenadores)):
        
        if eleccion == 0:
            print("Nos vemos en una próxima instancia")
            print("Saliendo...\n")
            exit()
        
        else:
            print("entrenador seleccionado!")
            print("Avanzando al menu de entrenadores...\n")
        

def menu_entrenadores():

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

    while not eleccion.isdigit() or eleccion in range (0, 7):
        print(f"Su respuesta debe ser un numero entero entre 0 y 7\n")
        eleccion = input("Ingrese el numero del entrenador que desea o 0 para Salir: ")

    if eleccion.isdigit() and eleccion in range (0, 7):
        
        if eleccion == 0:
            print("Nos vemos en una próxima instancia")
            print("Saliendo...\n")
            exit()
        
        else:
            print("entrenador seleccionado!")
            print("Avanzando al menu de entrenadores...\n")
