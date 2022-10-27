class TrickOrTreater:  # TrickOrTreater = tot
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.protagonista = False
        self.siguiente = None  # persona despues en la fila


class ColaDulces:
    """
    Clase que representa una lista ligada
    """

    def __init__(self):
        """
        Inicializa una lista ligada vacia, con una referencia nula a su cabeza y cola.
        """
        self.primero = None
        self.ultimo = None

    def tot_llega(self, nombre: str):
        """
        Agrega un nodo al final de la cola
        """
        nuevo = TrickOrTreater(nombre)

        if self.primero is None:
            self.primero = nuevo
            self.ultimo = self.primero

        else:
            self.ultimo.siguiente = nuevo
            self.ultimo = self.ultimo.siguiente

    def obtener_tot(self, posicion: int):
        """
        Recibe una posición como argumento y retorna
        el tot en esa posición de la cola
        """
        tot_actual = self.primero

        for _ in range(posicion):
            if tot_actual is not None:
                tot_actual = tot_actual.siguiente
            else:
                return None

        return tot_actual

    def obtener_posicion_protagonista(self):
        """
        Retorna la posición del tot protagonista en la cola.
        Si no se encuentra en la fila, retorna -1
        """
        # COMPLETAR

        if self.primero is None:
            return -1
        else:

            tot_actual = self.primero
            posicion = 0

            if tot_actual.protagonista:
                return posicion

            else:
                while tot_actual.siguiente.protagonista is False:

                    tot_actual = tot_actual.siguiente
                    posicion += 1

                    if tot_actual.protagonista:
                        return posicion

                    if tot_actual.siguiente is None:
                        return -1

    def tot_se_cola(self, nombre: str, posicion: int):
        """
        Crea una instancia de TrickOrTreater con el nombre recibido y
        lo inserta en la cola en la posición recibida.
        """
        # COMPLETAR
        tot_actual = self.primero

        tot_nuevo = TrickOrTreater(nombre)

        if posicion == 0:
            tot_nuevo.siguiente = self.primero
            self.primero = tot_nuevo

        else:
            while tot_nuevo != tot_actual:
                tot_actual = tot_actual.siguiente

            if tot_nuevo == tot_actual:
                tot_nuevo.siguiente = tot_actual.siguiente
                tot_actual.siguiente = tot_nuevo

    def tot_se_va(self, posicion: int):
        """
        Elimina a la persona de la posición recibida de la cola.
        """
        if posicion == 0:
            tot_nuevo = self.primero.siguiente
            self.primero.siguiente = None
            self.primero = tot_nuevo

            if tot_nuevo.siguiente is None:
                self.ultimo = tot_nuevo

            return

        tot_actual = self.obtener(posicion - 1)
        tot_fuera = tot_actual.siguiente
        tot_actual.siguiente = tot_fuera.siguiente
        tot_fuera.siguiente = None
        if tot_actual.siguiente is None:
            self.ultimo = tot_actual

    def atender_tot(self):
        """
        Elimina a la primera persona de la cola y la retorna.
        """
        # COMPLETAR

        tot_actual = self.primero
        eliminado = self.primero
        self.primero = tot_actual.siguiente

        while tot_actual.siguiente.siguiente is not None:
            tot_actual.siguiente = tot_actual.siguiente.siguiente
            tot_actual = tot_actual.siguiente

        if tot_actual.siguiente.siguiente is None:
            self.ultimo = tot_actual

        return eliminado

    def obtener_largo(self):
        """
        Retorna el largo de la cola como int.
        """
        # COMPLETAR
        tot_actual = self.primero
        contador = 0

        while tot_actual is not None:
            contador += 1
            tot_actual = tot_actual.siguiente

        return contador

    def __str__(self) -> str:
        """
        Retorna una representación de la fila con los nombres de
        cada uno de sus participantes.
        """
        string = "DULCES :) "
        tot_actual = self.primero
        while tot_actual:
            string += "<- " + tot_actual.nombre
            tot_actual = tot_actual.siguiente

        return string
