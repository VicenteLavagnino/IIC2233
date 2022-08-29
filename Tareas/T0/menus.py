#in this file the menus are defined

from curses.ascii import isdigit
from genericpath import isfile
import tablero
import juego
import os


def menu_de_inicio():

    print("Bienvenido a Star Advanced\n")
    
    print("Seleccione una opcion:\n")

    print("[1] Partida nueva")
    print("[2] Cargar una partida")
    print("[3] Ranking de puntajes")
    print("[0] Salir del juego")

    print("\n")
    print("Su respuesta debe ser 1, 2, 3 o 0")

    opcion = int(input("Ingrese una opcion: "))
    
    while opcion != 1 and opcion != 2 and opcion != 3 and opcion != 0:
        
        print("\n")
        print("Su respuesta debe ser 1, 2, 3 o 0")
        opcion = int(input("Ingrese una opción: "))


    if opcion == 1:
        print("Has elegido la opcion de partida nueva")

        nombre_usuario = input("Registre su nombre de usuario: ")
        
        nombre_archivo = nombre_usuario + ".txt"
        path_partida = os.path.join("partidas", nombre_archivo)

        #verifica si el nombre ya está en uso

        while os.path.isfile(path_partida):
            
            print("El nombre de usuario ya existe, intente con otro")
            nombre_usuario = input("Registre su nombre de usuario: ")
            nombre_archivo = nombre_usuario + ".txt"
            path_partida = os.path.join("partidas", nombre_archivo)


        largo_tablero = input("Ingrese el largo del tablero (número entero entre 3 y 15): ")

        while  not largo_tablero.isdigit() or (int(largo_tablero) < 3 or int(largo_tablero) > 15):
            print("El largo debe ser un número entre 3 y 15")
            largo_tablero = input("Ingrese el largo del tablero (número entero entre 3 y 15): ")

        ancho_tablero = input("Ingrese el ancho del tablero (número entero entre 3 y 15): ")

        while not ancho_tablero.isdigit() or int(ancho_tablero) < 3 or int(ancho_tablero) > 15:
            print("El ancho debe ser un número entre 3 y 15")
            ancho_tablero = input("Ingrese el ancho del tablero (número entero entre 3 y 15): ")

        largo_tablero = int(largo_tablero)
        ancho_tablero = int(ancho_tablero)

        escritura = open(path_partida, "w") #crea el archivo
        lineas = escritura.write(f"{nombre_archivo}, {largo_tablero}, {ancho_tablero}\n")
        escritura.close()

        partida = juego.Juego(nombre_usuario, largo_tablero, ancho_tablero)
        partida.generar_tablero()
        partida.llenar_bestias()
        partida.actualizar_puntaje()

        return partida.menu_de_juego()

        
    elif opcion == 2:
        
        nombre_usuario = input("nombre de usuario: ")

        nombre_archivo = nombre_usuario + ".txt"
        path_partida = os.path.join("partidas", nombre_archivo)

        if not os.path.isfile(path_partida):
            
            print("El nombre de usuario no existe \n")
            print("Volviendo al menú principal...")
            
            menu_de_inicio()
        
        else:

            juego.Juego.cargar_partida(nombre_usuario)
            partida = juego.Juego(nombre_usuario, largo_tablero, ancho_tablero)
            
            return partida.menu_de_juego()
    
    elif opcion == 3:
        
        print("Abriendo ranking de puntajes...")

        ruta = os.path.join("ranking_T0-IIC2233.txt")

        apertura = open(ruta, "r")
        lineas = apertura.readlines()

        for linea in lineas:
            print(linea)
        
        apertura.close()

        print("Volviendo al menú principal...")
        
        return menu_de_inicio()
        
    elif opcion == 0:
        
        print("Saliendo del juego")
        exit()


def actualizar_ranking(nombre_usuario, puntaje):

    #ranking tiene el formato "nombre_usuario, puntaje"

    ruta = os.path.join("ranking_T0-IIC2233.txt")

    archivo = open(ruta, "wt")
    lineas = archivo.readlines()

    for linea in range(0,9):

        linea.split(",")

        if linea[1] >= puntaje:

            pass

        elif linea[1] < puntaje:

            archivo.write(nombre_usuario + "," + puntaje + "\n")
            archivo.close()

def mostrar_ranking():

    ruta = os.path.join("ranking_T0-IIC223.txt")

    apertura = open(ruta, "r")
    lineas = apertura.readlines()

    for linea in lineas:
        print(linea)
        
    apertura.close()
