#in this file the game system is defined

import menus
import parametros
import random
import math
import tablero
import os

class Juego:

    def __init__(self, nombre_usuario, largo_tablero, ancho_tablero):

        self.nombre_usuario = nombre_usuario
        self.nombre_archivo = self.nombre_usuario + ".txt"
        self.path_archivo = os.path.join("partidas", self.nombre_archivo)
        self.largo_tablero = math.ceil(largo_tablero)
        self.ancho_tablero = math.ceil(ancho_tablero)
        self.cantidad_bestias = math.ceil(int(self.largo_tablero * self.ancho_tablero * parametros.PROB_BESTIA))
        self.tablero = []
        self.ubicacion_bestias = []
        self.puntaje = 0
        self.casillas_descubiertas = []

    def cargar_partida(self, nombre_usuario):

        self.nombre_usuario = nombre_usuario 
        self.nombre_archivo = self.nombre_usuario + ".txt"
        self.path_archivo = os.path.join("partidas" + self.nombre_archivo)

        partida = open(self.path_archivo, "r")
        lineas = partida.readlines()

        self.largo_tablero = int(lineas[0][1])
        self.ancho_tablero = int(lineas[0][2])
        self.cantidad_bestias = int(lineas[1])
        self.tablero = int[lineas[2]]
        self.ubicacion_bestias = int[lineas[3]]
        self.puntaje = int(lineas[4])
        self.casillas_descubiertas = int(lineas[5])

        partida.close()

    def guardar_partida(self):

        partida = open(self.path_archivo, "w")

        lineas = partida.write(f"{self.nombre_usuario}, {self.largo_tablero}, {self.ancho_tablero}\n")
        lineas = partida.write(f"{self.cantidad_bestias}\n")
        lineas = partida.write(f"{self.tablero}\n")
        lineas = partida.write(f"{self.ubicacion_bestias}\n")
        lineas = partida.write(f"{self.puntaje}\n")
        lineas = partida.write(f"{self.casillas_descubiertas}\n")
        
        #   lineas[0] = "{self.nombre_usuario}, {self.largo_tablero}, {self.ancho_tablero}"
        #   lineas[1] = self.cantidad_bestias
        #   lineas[2] = self.tablero
        #   lineas[3] = self.ubicacion_bestias
        #   lineas[4] = self.puntaje
        #   lineas[5] = self.casillas_descubiertas

        partida.close()

    def generar_tablero(self):
        
        for X in range(self.largo_tablero):
            
            nueva_fila = []

            for Y in range(self.ancho_tablero):
                
                nueva_columna = ' '
                nueva_fila.append(nueva_columna)
            
            self.tablero.append(nueva_fila)

    def llenar_bestias(self):

        for bestia in range(self.cantidad_bestias - 1):
                
                X = random.randint(0, self.largo_tablero - 1)
                Y = random.randint(0, self.ancho_tablero - 1)

                while [X,Y] in self.ubicacion_bestias:

                    X = random.randint(0, self.largo_tablero - 1)
                    Y = random.randint(0, self.ancho_tablero - 1)
                    
                self.tablero[X][Y].append('N')
                self.ubicacion_bestias.append([X, Y])
                
    def actualizar_puntaje(self):

        self.puntaje = self.cantidad_bestias * len(self.casillas_descubiertas) * parametros.POND_PUNT

    
    def descubrir_sector(self):

        X_casilla_por_descubrir = input("Ingrese la coordenada X de la casilla por descubrir: ")

        # arregalr is digit y perdir antes int en todo caso

        while not X_casilla_por_descubrir.isdigit() or int(X_casilla_por_descubrir) > self.largo_tablero or int(X_casilla_por_descubrir) < 0:
            
            print("La coordenada X debe ser un número entero menor que ", self.largo_tablero - 1)
            X_casilla_por_descubrir = input("Ingrese la coordenada X de la casilla por descubrir: ")

        Y_casilla_por_descubrir = input("Ingrese la coordenada X de la casilla por descubrir: ")

        while not (Y_casilla_por_descubrir).isdigit() or int(Y_casilla_por_descubrir) > self.ancho_tablero or int(Y_casilla_por_descubrir) < 0:
            
            print("La coordenada Y debe ser un número entero menor que ", self.ancho_tablero - 1)
            Y_casilla_por_descubrir = input("Ingrese la coordenada Y de la casilla por descubrir: ")

        X_casilla_por_descubrir = int(X_casilla_por_descubrir)
        Y_casilla_por_descubrir = int(Y_casilla_por_descubrir)

        sector = [X_casilla_por_descubrir,Y_casilla_por_descubrir]

        if sector in self.ubicacion_bestias:

            print("En el sector se encuentra una bestia")
            print("Perdiste")
            print()

            print("nombre de usuario: ", self.nombre_usuario)
            print("Puntaje final: ", self.puntaje)

            self.actualizar_puntaje()
            self.guardar_partida()
            menus.actualizar_ranking(self.nombre_archivo, self.puntaje)

            #pierde
            pass

        elif sector in self.casillas_descubiertas:
            
            print("La casilla ha sido descubierta anteriormente")
            print()
            pass

        else:

            casillas_con_bestias = 0

            if X_casilla_por_descubrir != 0 or X_casilla_por_descubrir != self.largo_tablero:
                
                if Y_casilla_por_descubrir != 0 or Y_casilla_por_descubrir != self.ancho_tablero:

                    if self.tablero[X_casilla_por_descubrir - 1][Y_casilla_por_descubrir] == 'N':
                        casillas_con_bestias += 1

                    if self.tablero[X_casilla_por_descubrir + 1][Y_casilla_por_descubrir] == 'N':
                        casillas_con_bestias += 1
                    
                    if self.tablero[X_casilla_por_descubrir][Y_casilla_por_descubrir - 1] == 'N':
                        casillas_con_bestias += 1
                    
                    if self.tablero[X_casilla_por_descubrir][Y_casilla_por_descubrir + 1] == 'N':
                        casillas_con_bestias += 1

                    if self.tablero[X_casilla_por_descubrir - 1][Y_casilla_por_descubrir - 1] == 'N':
                        casillas_con_bestias += 1

                    if self.tablero[X_casilla_por_descubrir - 1][Y_casilla_por_descubrir + 1] == 'N':
                        casillas_con_bestias += 1

                    if self.tablero[X_casilla_por_descubrir + 1][Y_casilla_por_descubrir - 1] == 'N':
                        casillas_con_bestias += 1

                    if self.tablero[X_casilla_por_descubrir + 1][Y_casilla_por_descubrir + 1] == 'N':
                        casillas_con_bestias += 1

                elif Y_casilla_por_descubrir == 0:
                    
                    if self.tablero[X_casilla_por_descubrir - 1][Y_casilla_por_descubrir] == 'N':
                        casillas_con_bestias += 1

                    if self.tablero[X_casilla_por_descubrir + 1][Y_casilla_por_descubrir] == 'N':
                        casillas_con_bestias += 1
                     
                    if self.tablero[X_casilla_por_descubrir][Y_casilla_por_descubrir + 1] == 'N':
                        casillas_con_bestias += 1

                    if self.tablero[X_casilla_por_descubrir - 1][Y_casilla_por_descubrir + 1] == 'N':
                        casillas_con_bestias += 1

                    if self.tablero[X_casilla_por_descubrir + 1][Y_casilla_por_descubrir + 1] == 'N':
                        casillas_con_bestias += 1
          
                elif Y_casilla_por_descubrir == self.ancho_tablero:
                    
                    if self.tablero[X_casilla_por_descubrir - 1][Y_casilla_por_descubrir] == 'N':
                        casillas_con_bestias += 1

                    if self.tablero[X_casilla_por_descubrir + 1][Y_casilla_por_descubrir] == 'N':
                        casillas_con_bestias += 1
                    
                    if self.tablero[X_casilla_por_descubrir][Y_casilla_por_descubrir - 1] == 'N':
                        casillas_con_bestias += 1
                    
                    if self.tablero[X_casilla_por_descubrir - 1][Y_casilla_por_descubrir - 1] == 'N':
                        casillas_con_bestias += 1

                    if self.tablero[X_casilla_por_descubrir + 1][Y_casilla_por_descubrir - 1] == 'N':
                        casillas_con_bestias += 1

            elif X_casilla_por_descubrir == 0:

                if Y_casilla_por_descubrir != 0 or Y_casilla_por_descubrir != self.ancho_tablero:

                    if self.tablero[X_casilla_por_descubrir + 1][Y_casilla_por_descubrir] == 'N':
                        casillas_con_bestias += 1
                    
                    if self.tablero[X_casilla_por_descubrir][Y_casilla_por_descubrir - 1] == 'N':
                        casillas_con_bestias += 1
                    
                    if self.tablero[X_casilla_por_descubrir][Y_casilla_por_descubrir + 1] == 'N':
                        casillas_con_bestias += 1

                    if self.tablero[X_casilla_por_descubrir + 1][Y_casilla_por_descubrir - 1] == 'N':
                        casillas_con_bestias += 1

                    if self.tablero[X_casilla_por_descubrir + 1][Y_casilla_por_descubrir + 1] == 'N':
                        casillas_con_bestias += 1
     
                elif Y_casilla_por_descubrir == 0:

                    if self.tablero[X_casilla_por_descubrir + 1][Y_casilla_por_descubrir] == 'N':
                        casillas_con_bestias += 1
                    
                    if self.tablero[X_casilla_por_descubrir][Y_casilla_por_descubrir + 1] == 'N':
                        casillas_con_bestias += 1

                    if self.tablero[X_casilla_por_descubrir + 1][Y_casilla_por_descubrir + 1] == 'N':
                        casillas_con_bestias += 1
                
                elif Y_casilla_por_descubrir == self.ancho_tablero:

                    if self.tablero[X_casilla_por_descubrir + 1][Y_casilla_por_descubrir] == 'N':
                        casillas_con_bestias += 1
                    
                    if self.tablero[X_casilla_por_descubrir][Y_casilla_por_descubrir - 1] == 'N':
                        casillas_con_bestias += 1

                    if self.tablero[X_casilla_por_descubrir + 1][Y_casilla_por_descubrir - 1] == 'N':
                        casillas_con_bestias += 1

            elif X_casilla_por_descubrir == self.largo_tablero:

                if Y_casilla_por_descubrir != 0 or Y_casilla_por_descubrir != self.ancho_tablero:

                    if self.tablero[X_casilla_por_descubrir - 1][Y_casilla_por_descubrir] == 'N':
                        casillas_con_bestias += 1
                    
                    if self.tablero[X_casilla_por_descubrir][Y_casilla_por_descubrir - 1] == 'N':
                        casillas_con_bestias += 1
                    
                    if self.tablero[X_casilla_por_descubrir][Y_casilla_por_descubrir + 1] == 'N':
                        casillas_con_bestias += 1

                    if self.tablero[X_casilla_por_descubrir - 1][Y_casilla_por_descubrir - 1] == 'N':
                        casillas_con_bestias += 1

                    if self.tablero[X_casilla_por_descubrir - 1][Y_casilla_por_descubrir + 1] == 'N':
                        casillas_con_bestias += 1

                elif Y_casilla_por_descubrir == 0:
                    
                    if self.tablero[X_casilla_por_descubrir - 1][Y_casilla_por_descubrir] == 'N':
                        casillas_con_bestias += 1
                    
                    if self.tablero[X_casilla_por_descubrir][Y_casilla_por_descubrir + 1] == 'N':
                        casillas_con_bestias += 1

                    if self.tablero[X_casilla_por_descubrir - 1][Y_casilla_por_descubrir + 1] == 'N':
                        casillas_con_bestias += 1
                
                elif Y_casilla_por_descubrir == self.ancho_tablero:
                    
                    if self.tablero[X_casilla_por_descubrir - 1][Y_casilla_por_descubrir] == 'N':
                        casillas_con_bestias += 1
                    
                    if self.tablero[X_casilla_por_descubrir][Y_casilla_por_descubrir - 1] == 'N':
                        casillas_con_bestias += 1
                    
                    if self.tablero[X_casilla_por_descubrir - 1][Y_casilla_por_descubrir - 1] == 'N':
                        casillas_con_bestias += 1


            self.tablero[X_casilla_por_descubrir][Y_casilla_por_descubrir] = casillas_con_bestias

            self.casillas_descubiertas.append([X_casilla_por_descubrir, Y_casilla_por_descubrir])

            return self.menu_de_juego()


    def menu_de_juego(self):

        tablero.print_tablero_con_utf8(self.tablero) #arreglar el utf8

        print("Seleccione una acción:\n")

        print("[1] Descubrir un nuevo sector")
        print("[2] Guardar la partida") #preguntar si desea Salir
        print("[3] Salir de la partida") #con o sin guardar VER SI VOLVER AL MENU O SALIR
        print("[4] Atrás")
        print("\n)")
        print("[0] Salir del juego")
        
        print("\n")
        print("Su respuesta debe ser 1, 2, 3 o 0")

        opcion_juego = int(input("Ingrese una opción: "))

        while opcion_juego != 1 and opcion_juego != 2 and opcion_juego != 3 and opcion_juego != 0:
            print("\n")
            print("Su respuesta debe ser 1, 2, 3 o 0")
            opcion_juego = int(input("Ingrese una opción: "))

        if opcion_juego == 1:
            self.descubrir_sector()
            self.actualizar_puntaje()
            menus.actualizar_ranking(self.nombre_usuario, self.puntaje)

        elif opcion_juego == 2:
            
            self.guardar_partida()
            print("Partida guardada")

            print("Presione [0] para Salir")
            print("Presione [1] para volver al menú de juego")

            opcion = int(input("Ingrese una opción: "))

            while opcion != 0 and opcion != 1:
                print("Su respuesta debe ser [0] o [1]")
                opcion = int(input("Ingrese una opción: "))

            if opcion == 0:
                print("Saliendo del juego")
                exit()
            
            elif opcion == 1:
                return self.menu_de_juego()

        elif opcion_juego == 3:
            print("...Saliendo de la partida")
            print("\n")
            print("Desea guardar la partida?")
            print("[1] Salir con guardar")
            print("[2] Salir sin guardar")

            tipo_salida = int(input("Ingrese una opción: "))

            while tipo_salida != 1 and tipo_salida != 2:
                print("Su respuesta debe ser 1 o 2")
                tipo_salida = int(input("Ingrese una opción: "))
                
            if tipo_salida == 1:
                
                self.guardar_partida()
                print("Partida guardada")
                pass

            elif tipo_salida == 2:
                
                print("Saliendo SIN GUARDAR de la partida...")
                pass

            print("Volviendo al menú de inicio")
            
            menus.menu_de_inicio()
            
            pass

        elif opcion_juego == 4:
            print("Volviendo al menú de inicio")
            
            menus.menu_de_inicio()

        elif opcion_juego == 0:
            print("Saliento del juego")
            exit()

        self.menu_de_juego()