#in this file the menus are defined

import tablero

import juego

def menu_de_inicio():

    print("Bienvenido a Star Advanced/n")
    
    print("Seleccione una opcion:/n")

    print("[1] Partida nueva")
    print("[2] Cargar una partida")
    print("[3] Ranking de puntajes")
    print("[0] Salir del juego")

    print("/n")
    print("Su respuesta debe ser 1, 2, 3 o 0")

    opcion = int(input("Ingrese una opcion: "))
    
    while opcion != 1 or opcion != 2 or opcion != 3 or opcion != 0:
        print("/n")
        print("Su respuesta debe ser 1, 2, 3 o 0")
        opcion = int(input("Ingrese una opción: "))


    if opcion == 1:
        print("Has elegido la opcion de partida nueva")
        nombre_usuario = input("Registre su nombre de usuario: ")
        largo_tablero = int(input("Ingrese el largo del tablero: (debe ser un número entero entre 3 y 15)"))

        while largo_tablero < 3 or largo_tablero > 15:
            print("El largo debe ser un número entre 3 y 15")
            largo_tablero = int(input("Ingrese el largo del tablero: (debe ser un número entero entre 3 y 15)"))

        ancho_tablero = int(input("Ingrese el ancho del tablero: (debe ser un número entero entre 3 y 15)"))

        while ancho_tablero < 3 or ancho_tablero > 15:
            print("El ancho debe ser un número entre 3 y 15")
            ancho_tablero = int(input("Ingrese el ancho del tablero: (debe ser un número entero entre 3 y 15)"))

        return [largo_tablero, ancho_tablero]

        

    elif opcion == 2:
        
        nombre_usuario = input("nombre de usuario: ")

        if #nombre de usuario no existe:
            
            print("El nombre de usuario no existe /n")
            print("Volviendo al menú principal...")
            
            menu_de_inicio()
        
        #cargar partida con nombre de usuario --> menu juego
        #usar isfile de os.path
        
        pass
    
    elif opcion == 3:

       
        pass

    elif opcion == 3:
        #ranking de puntajes
        pass

    elif opcion == 0:
        print("Saliendo del juego")



def menu_de_juego():

    tablero.juego.print_tablero(tablero, False) #arreglar el utf8

    print("Seleccione una acción:/n")

    print("[1] Descubrir un nuevo sector")
    print("[2] Guardar la partida") #preguntar si desea Salir
    print("[3] Salir de la partida") #con o sin guardar VER SI VOLVER AL MENU O SALIR
    print("[4] Atrás")
    print("/n)")
    print("[0] Salir del juego")
    
    print("/n")
    print("Su respuesta debe ser 1, 2, 3 o 0")

    opcion_juego = int(input("Ingrese una opción: "))

    while opcion_juego != 1 or opcion_juego != 2 or opcion_juego != 3 or opcion_juego != 0:
        print("/n")
        print("Su respuesta debe ser 1, 2, 3 o 0")
        opcion_juego = int(input("Ingrese una opción: "))


    if opcion_juego == 1:
        #descubrir un nuevo sector
        pass

    elif opcion_juego == 2:
        
        def guardar_partida():
            
            print("Partida guardada")
            #crear nombre_usuario.txt almacenar posiciones descubiertas y num respetivos y posicion de cada bestia (detallar formato en readme)
            pass
        
        pass

    elif opcion_juego == 3:
        print("...Saliendo de la partida")
        print("/n")
        print("Desea guardar la partida?")
        print("[1] Salir con guardar[2] Salir sin guardar")
        print("[2] Salir sin guardar")

        tipo_salida = int(input("Ingrese una opción: "))

        while tipo_salida != 1 or tipo_salida != 2:
            print("Su respuesta debe ser 1 o 2")
            tipo_salida = int(input("Ingrese una opción: "))
            
        if tipo_salida == 1:
            #guardar la partida
            pass

        elif tipo_salida == 2:
            #salir sin guardar
            pass

        print("Volviendo al menú de inicio")
        menu_de_inicio()
        
        pass

    elif opcion_juego == 4:
        print("Volviendo al menú de inicio")
        menu_de_inicio()

    elif opcion_juego == 0:
        print("Saliento del juego")
        exit()

    menu_de_juego()




