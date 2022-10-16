from PyQt5.QtWidgets import QApplication

# import backend
from backend.logica_inicio import LogicaInicio
from backend.logica_juego import LogicaJuego
from backend.elementos_juego import *

# import frontend
from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_principal import VentanaPrincipal
from frontend.ventana_juego import VentanaJuego
from frontend.ventana_postronda import VentanaPostronda
from frontend.ventana_ranking import VentanaRanking

# codigo inspirado desde dccubitos en AS3


class DCCruz(QApplication):
    def __init__(self, argv) -> None:
        super().__init__(argv)

        # instanciar ventanas
        self.ventana_inicio = VentanaInicio()
        self.ventana_principal = VentanaPrincipal()
        self.ventana_juego = VentanaJuego()
        self.ventana_postronda = VentanaPostronda()
        self.ventana_ranking = VentanaRanking()

        # instanciar logicas
        self.logica_inicio = LogicaInicio()
        self.logica_juego = LogicaJuego()

        # conectar signals

        self.conectar_inicio()
        self.conectar_principal()
        self.conectar_juego()
        self.conectar_postronda()
        self.conectar_ranking()

    def conectar_inicio(self):

        # JUGAR
        self.ventana_inicio.senal_login.connect(self.logica_inicio.validar_usuario)
        self.logica_inicio.senal_respuesta_validacion.connect(
            self.ventana_inicio.recibir_validacion
        )

        # RANKING
        self.ventana_inicio.senal_mostrar_ranking.connect(
            self.ventana_ranking.mostrar_ventana
        )

        # SALIR
        self.ventana_inicio.senal_cerrar_juego.connect(self.exit)
        pass

    def conectar_principal(self):
        self.logica_inicio.senal_abrir_principal.connect(
            self.ventana_principal.mostrar_ventana
        )

        pass

    def conectar_juego(self):
        self.ventana_principal.senal_modo.connect(self.ventana_juego.mostrar_ventana)
        self.logica_inicio.senal_usuario.connect(self.logica_juego.get_usuario)
        self.ventana_principal.senal_modo.connect(self.logica_juego.get_modo)

        # INICIAR
        self.ventana_juego.senal_iniciar_juego.connect(self.logica_juego.iniciar_juego)

        # AVANZAR
        self.ventana_juego.senal_comprobar_avanzar.connect(
            self.logica_juego.comprobar_avanzar
        )
        self.logica_juego.senal_avanzar.connect(self.ventana_juego.avanzar)
        self.ventana_juego.senal_avanzar.connect(self.ventana_postronda.mostrar_ventana)

        # SALIR
        self.ventana_juego.senal_cerrar_juego.connect(self.exit)

        pass

    def conectar_postronda(self):

        self.ventana_postronda.senal_salir.connect(self.exit)
        self.ventana_postronda.senal_siguiente_ronda.connect(
            self.logica_juego.siguiente_ronda
        )
        self.logica_juego.senal_siguiete_ronda.connect(
            self.ventana_juego.mostrar_ventana
        )
        pass

    def conectar_ranking(self):

        # Volver
        self.ventana_ranking.senal_volver.connect(self.iniciar)
        self.logica_juego.senal_avanzar.connect(self.ventana_postronda.mostrar_ventana)
        pass

    def iniciar(self):
        self.ventana_inicio.show()
        pass
