# interfaz
from PyQt5.QtCore import pyqtSignal, QObject

from frontend.ventana_espera import VentanaEspera
from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_juego import VentanaJuego
from frontend.ventana_final import VentanaFinal
from frontend.chat import Chat


class Ventana(QObject):

    # Señales
    senal_mostrar_ventana_inicio = pyqtSignal()
    senal_ocultar_ventana_inicio = pyqtSignal()
    senal_error_name_full = pyqtSignal()
    senal_error_name_server = pyqtSignal()
    senal_avanzar_espera = pyqtSignal(str)
    senal_avanzar_juego = pyqtSignal(str, str)
    senal_oponente_desconectado = pyqtSignal()
    senal_servidor_desconectado = pyqtSignal()
    senal_empate = pyqtSignal()
    senal_ganador = pyqtSignal()
    senal_perdedor = pyqtSignal()

    senal_chat_recibido = pyqtSignal(str)

    def __init__(self, parent) -> None:  # [parente = cliente]

        super().__init__()
        self.ventana_espera = VentanaEspera()
        self.ventana_inicio = VentanaInicio()
        self.ventana_juego = VentanaJuego()
        self.ventana_final = VentanaFinal()
        self.chat = Chat()

        self.descarga = bytearray()

        ### Conexiones ###

        # Señales de la ventana Inicio

        self.ventana_inicio.senal_validar_usuario.connect(parent.send_response)
        self.senal_error_name_full.connect(self.ventana_inicio.error_name_full)
        self.senal_error_name_server.connect(self.ventana_inicio.error_name_server)

        self.senal_avanzar_espera.connect(self.ventana_espera.abrir)
        self.senal_ocultar_ventana_inicio.connect(self.ventana_inicio.ocultar)

        # Señales de la ventana Espera

        self.senal_avanzar_juego.connect(self.ventana_espera.avanzar_juego)
        self.ventana_espera.senal_avanzar_juego.connect(self.ventana_juego.abrir)
        self.ventana_espera.senal_abrir_chat.connect(self.chat.abrir)

        # Señales de la ventana Juego

        self.ventana_juego.senal_enviar_carta.connect(parent.send_response)
        self.senal_empate.connect(self.ventana_juego.empate)
        self.senal_ganador.connect(self.ventana_juego.ganador)
        self.senal_perdedor.connect(self.ventana_juego.perdedor)

        # Señales de la ventana Final
        self.senal_oponente_desconectado.connect(
            self.ventana_final.desconexion_repentina
        )
        self.senal_servidor_desconectado.connect(
            self.ventana_final.desconexion_servidor
        )

        self.ventana_final.senal_volver_inicio.connect(self.ventana_inicio.abrir)

        # Señales del chat
        self.chat.senal_enviar_mensaje.connect(parent.send_response)
        self.senal_chat_recibido.connect(self.chat.recibir_mensaje)

    def mostrar_ventana_inicio(self):
        self.ventana_inicio.abrir()

    def mostrar_ventana_espera(self):
        self.ventana_espera.abrir()
        self.ventana_inicio.ocultar()

    # === > Lógica del cliente < ===

    def avanzar_espera(self, username):
        print("señal recibida")
        self.senal_avanzar_espera.emit(username)
        self.senal_ocultar_ventana_inicio.emit()

    def servidor_lleno(self):
        self.senal_error_name_full.emit()

    def nombre_repetido(self):
        self.senal_error_name_server.emit()

    def avanzar_juego(self, username, oponente):

        # primero iniciar timer ventana espera
        self.senal_avanzar_juego.emit(username, oponente)
        # abrir ventana juego
        pass

    def oponente_desconectado(self):
        self.senal_oponente_desconectado.emit()
        pass

    def servidor_desconectado(self):
        self.senal_servidor_desconectado.emit()
        pass

    def respuesta_chat(self, msg_oponente):
        self.senal_chat_recibido.emit(msg_oponente)

    def ganador(self):
        self.senal_ganador.emit()

    def perdedor(self):
        self.senal_perdedor.emit()

    def empate(self):
        self.senal_empate.emit()
