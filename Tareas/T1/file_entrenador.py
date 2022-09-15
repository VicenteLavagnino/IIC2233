# En este archivo se define la clase Entrenador

from file_programon import Programon
from file_objeto import Objeto


class Entrenador:
    def __init__(
        self,
        nombre: str,
        programones: list[Programon],
        energia: int,
        objetos: list[Objeto],
    ):
        """Constructor de la clase"""

        self.nombre = nombre
        self.programones = programones
        self.energia = energia
        self.objetos = objetos

    def estado_entrenador(self):
        """Metodo para ver el estado del entrenador"""

        show_objetos = ""
        for objeto in self.objetos:
            show_objetos += objeto + ", "
        show_objetos = show_objetos.strip(", ")

        print("\n" + "-" * 70)
        print(" " * 20 + "*** Estado entrenador ***" + " " * 20)
        print("-" * 70)
        print("\n")
        print("Nombre: " + self.nombre)
        print("Energia: " + self.energia)
        print("Objetos: " + show_objetos)
        print("-" * 70)
        print(" " * 20 + "*** Programones ***" + " " * 20)
        print("-" * 70)
        # print(f"{Nombre}    |    {Tipo}   |   {Nivel}  | {Vida}")
        print("-" * 70)
        for programon in self.programones:
            print(
                f"{programon.nombre}    |    {programon.tipo}   |   {programon.nivel}  | {programon.vida}"
            )

        print("\n")
        print("[0] Salir")
        print("[1] Volver\n")
        eleccion = input("Ingrese la opcion que desea para continuar, debe ser 0 o 1: ")

        while eleccion not in ["0", "1"]:
            print("Su respuesta debe ser 0 o 1")
            eleccion = input(
                "Ingrese la opcion que desea para continuar, debe ser 0 o 1: "
            )

        if eleccion == "0":
            print("Nos vemos en una próxima instancia")
            print("Saliendo...\n")
            exit()

        elif eleccion == "1":
            print("Volviendo al menu de entrenadores...\n")
