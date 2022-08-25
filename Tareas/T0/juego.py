#in this file the game system is defined

from curses.ascii import isdigit
import menus
import parametros
import random
import math

class Juego:

    def __init__(self):

        self.largo_tablero = math.ceil(menus.menu_de_inicio()[0])
        self.ancho_tablero = math.ceil(menus.menu_de_inicio()[1])
        self.cantidad_bestias = math.ceil(int(self.largo_tablero * self.ancho_tablero * parametros.PROB_BESTIA))
        self.tablero = []
        self.ubicacion_bestias = []
        self.puntaje = 0
        self.casillas_descubiertas = 0

    def generar_tablero(self):
        
        for X in range(self.largo_tablero):
            
            nueva_fila = []

            for Y in range(self.ancho_tablero):
                
                nueva_columna = [' ']
                nueva_fila.append(nueva_columna)
            
            self.tablero.append(nueva_fila)

    def llenar_bestias(self):

        for bestia in range(self.cantidad_bestias - 1):
                
                X = random.randint(0, self.largo_tablero - 1)
                Y = random.randint(0, self.ancho_tablero - 1)
                
                if [X,Y] not in self.ubicacion_bestias:
                    
                    self.tablero[X][Y].append('N')
                    self.ubicacion_bestias.append([X, Y])

                else:
                    pass #pensar como hacerlo
                
    def actualizar_puntaje(self):

        self.puntaje = self.cantidad_bestias * self.casillas_descubiertas * parametros.POND_PUNT

    
    def descubrir_sector(self):

        X_casilla_por_descubrir = int(input("Ingrese la coordenada X de la casilla por descubrir: "))

        # arregalr is digit y perdir antes int en todo caso

        while not isdigit(X_casilla_por_descubrir) or X_casilla_por_descubrir > self.largo_tablero:
            
            print("La coordenada X debe ser un número entero menor que ", self.largo_tablero - 1)
            X_casilla_por_descubrir = int(input("Ingrese la coordenada X de la casilla por descubrir: "))

        Y_casilla_por_descubrir = int(input("Ingrese la coordenada X de la casilla por descubrir: "))

        while Y_casilla_por_descubrir > self.ancho_tablero:

            #ARREGLAR
            
            print("La coordenada Y debe ser un número entero menor que ", self.ancho_tablero - 1)
            Y_casilla_por_descubrir = int(input("Ingrese la coordenada Y de la casilla por descubrir: "))

        sector =[X_casilla_por_descubrir,Y_casilla_por_descubrir]

        ### while sector not in self.ubicacion_bestias: #si no hay bestias, se sigue jugando y muestro lo que rodea la casilla

            #cantidad_bestias_alrededor = 0

            #for X in range(self.largo_tablero):

                #caso borde

                #if not X_casilla_por_descubrir == 0 or not X_casilla_por_descubrir == self.largo_tablero:

                #else:
                    
            if 

                    
            