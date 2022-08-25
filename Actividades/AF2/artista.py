from parametros import (AFINIDAD_HIT, AFINIDAD_INICIAL, AFINIDAD_PUBLICO_POP,
                        AFINIDAD_STAFF_POP, AFINIDAD_PUBLICO_ROCK,
                        AFINIDAD_STAFF_ROCK, AFINIDAD_PUBLICO_TRAP_CHILENO ,
                        AFINIDAD_STAFF_TRAP_CHILENO , AFINIDAD_PUBLICO_REG,
                        AFINIDAD_STAFF_REG, AFINIDAD_ACCION_POP,
                        AFINIDAD_ACCION_ROCK, AFINIDAD_ACCION_TRAP_CHILENO ,
                        AFINIDAD_ACCION_REG, AFINIDAD_MIN, AFINIDAD_MAX)


class Artista:
    def __init__(self, nombre, genero, dia_presentacion, hit_del_momento):
        self.nombre = nombre
        self.hit_del_momento = hit_del_momento
        self.genero = genero
        self.dia_presentacion = dia_presentacion
        self._afinidad_con_publico = AFINIDAD_INICIAL
        self._afinidad_con_staff = AFINIDAD_INICIAL

    @property
    def afinidad_con_publico(self):
        return self._afinidad_con_publico

    @afinidad_con_publico.setter
    def afinidad_con_publico(self, valor: float):

        if valor >= 100:
            self._afinidad_con_publico = 100

        elif valor <= 0:
            self._afinidad_con_publico = 0

        else:
            self._afinidad_con_publico = valor


    @property
    def afinidad_con_staff(self):
        return self._afinidad_con_staff

    @afinidad_con_staff.setter
    def afinidad_con_staff(self, valor: float):

        if valor >= 100:
            self._afinidad_con_staff = 100

        elif valor <= 0:
            self._afinidad_con_staff = 0

        else:
            self._afinidad_con_staff = valor

    def animo(self):
        
        animo = (self._afinidad_con_publico * 0.5) * (self._afinidad_con_staff * 0.5)
        
        return animo

    def recibir_suministros(self, suministro):
        
        self.afinidad_con_staff += suministro.valor_de_satisfaccion

        if suministro.valor_de_satisfaccion < 0:

            f"{self.nombre} recibió {suministro.nombre} en malas condiciones."

        elif suministro.valor_de_satisfaccion > 0:

            f"{self.nombre} recibió un {suministro.nombre} a tiempo!"


    def cantar_hit(self):
        
        self.afinidad_con_publico += AFINIDAD_HIT
        

    def __str__(self):
        
        print(f"nombre del artista: {self.nombre}")
        print(f"genero: {self.genero}")
        print(f"ánimo: {self.animo()}")
        


class ArtistaPop(Artista):
    
    def __init__(self, nombre, genero, dia_presentacion, hit_del_momento, *args, **kwargs):

        Artista.__init__(self, nombre, genero, dia_presentacion, hit_del_momento)
        
        self.accion = "Solo de guitarra"
        
        self._afinidad_con_publico = AFINIDAD_PUBLICO_ROCK 
        
        self._afinidad_con_staff = AFINIDAD_STAFF_ROCK
        

    def accion_especial(self):
        # COMPLETAR
        pass

    def animo(self):
        # COMPLETAR
        pass


class ArtistaRock(Artista):
    def __init__(self, *args, **kwargs):
        # COMPLETAR
        pass

    def accion_especial(self):
        # COMPLETAR
        pass

    def animo(self):
        # COMPLETAR
        pass


class ArtistaTrapChileno(Artista):
    def __init__(self, *args, **kwargs):
        # COMPLETAR
        pass

    def accion_especial(self):
        # COMPLETAR
        pass

    def animo(self):
        # COMPLETAR
        pass


class ArtistaReggaeton(Artista):
    def __init__(self, *args, **kwargs):
        # COMPLETAR
        pass

    def accion_especial(self):
        # COMPLETAR
        pass

    def animo(self):
        # COMPLETAR
        pass
