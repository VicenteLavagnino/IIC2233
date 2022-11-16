import socket
import json
from threading import Thread
from ventana import Ventana
from helpers import name_error_server_full
from cripto import encriptar, desencriptar


class Cliente:
    def __init__(self, host, port) -> None:

        self.host = host
        self.port = port
        self.ventana = Ventana(self)
        self.conectado = False
        self.username = None
        self.oponente = None
        self.iniciar_cliente()

    def log(self, mensaje: str):
        print("\n|" + mensaje.center(80, " ") + "|\n")

    def iniciar_cliente(self):
        ##agregar try except
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_cliente.connect((self.host, self.port))
        self.ventana.mostrar_ventana_inicio()
        self.conectado = True
        self.escuchar_servidor()
        pass

    def escuchar_servidor(self):
        thread = Thread(target=self.escuchar_servidor_thread)
        thread.start()

    def escuchar_servidor_thread(self):

        try:

            while self.conectado:
                self.log("escuchando")
                response_bytes_length = self.socket_cliente.recv(4)
                response_length = int.from_bytes(response_bytes_length, byteorder="big")
                response = bytearray()

                self.log("Recibiendo respuesta del servidor...")

                for i in range(response_length // 32 + 1):
                    self.log(f"Recibiendo bloque {i}")
                    numero_bloque_bytes = self.socket_cliente.recv(4)
                    numero_bloque = int.from_bytes(
                        numero_bloque_bytes, byteorder="little"
                    )
                    self.log(f"Codificando bloque numero {numero_bloque}")

                    mensaje_bloque_bytes = self.socket_cliente.recv(32)
                    self.log(f"Mensaje recibido: {mensaje_bloque_bytes}")
                    response += mensaje_bloque_bytes

                received = self.decodificar(response)

                self.log(f"Recibido: {received}")

                self.message_handler(received)

        except:
            self.ventana.servidor_desconectado()

    def send_response(self, response):
        """envía una respuesta al servidor"""
        self.log(f"Enviando respuesta: {response}")
        response = self.codificar(response)

        len_response = len(response)
        len_response_bytes = len_response.to_bytes(4, byteorder="big")
        mensaje = bytearray()

        mensaje += len_response_bytes

        for i in range(len_response // 32):
            numero_bloque = i.to_bytes(4, byteorder="little")
            mensaje += numero_bloque

            mensaje += response[:32]
            response = response[32:]

        if len(response) > 0:
            i = len_response // 32
            i = i.to_bytes(4, byteorder="little")
            mensaje += i

            for _ in range(32 - len(response)):
                # response += b"\x00"
                response += " "
            mensaje += bytearray(response, encoding="utf-8")

        return self.socket_cliente.sendall(mensaje)

    def codificar(self, mensaje):
        mensaje = json.dumps(mensaje)
        return mensaje

    def decodificar(self, mensaje):

        mensaje = json.loads(mensaje)
        return mensaje

    # === > Lógica del cliente < ===

    def message_handler(self, mensaje):

        self.log(f"Mensaje recibido: {mensaje}")

        mensaje = mensaje.split(";")
        tipo = mensaje[0]

        if tipo == "LOGIN":
            self.manejar_login(mensaje)

        elif tipo == "INICIAR_PARTIDA":
            jugadores = mensaje[1].split(",")
            self.log(f"INICIAR_PARTIDA {jugadores}")
            self.manejar_iniciar_partida(jugadores)

        elif tipo == "CLIENTE_DESCONECTADO":
            self.ventana.oponente_desconectado()

        elif tipo == "SERVIDOR_DESCONECTADO":
            self.ventana.servidor_desconectado()

        elif tipo == "CHAT":
            self.ventana.respuesta_chat(mensaje[1])

    def manejar_login(self, mensaje):

        self.log(f"Mensaje recibido: {mensaje}")

        if mensaje[1] == "True":

            self.log(f"usuario {mensaje[2]}, {mensaje[3]}")
            self.username = str(mensaje[3])
            self.log("emitir señal")
            self.ventana.avanzar_espera(self.username)
            pass

        elif mensaje[1] == "False":

            if mensaje[2] == "lleno":
                self.ventana.servidor_lleno()

            elif mensaje[2] == "repetido":
                self.ventana.nombre_repetido()

    def manejar_iniciar_partida(self, jugadores):

        for jugador in jugadores:
            if jugador != self.username:
                self.oponente = jugador

        self.ventana.avanzar_juego(self.username, self.oponente)
