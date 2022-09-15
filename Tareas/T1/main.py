# en este archivo se corre el programa
from data import entrenadores, programones, objetos, liga
from menus_principales import menu_inicio
from file_liga import LigaProgramon

if __name__ == "__main__":

    menu_inicio(entrenadores, programones, objetos, liga)
