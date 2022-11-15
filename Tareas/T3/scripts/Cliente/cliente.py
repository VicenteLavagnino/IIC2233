import socket
import json
from threading import Thread
from ventana import Ventana
from helpers import name_error_server_full


class Cliente:
    def __init__(self, host, port) -> None:

        self.host = host
        self.port = port
        self.ventana = Ventana(self)
        self.conectado = False
        self.username = None
        self.oponente = None
        self.iniciar_cliente()

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

        while self.conectado:
            print("escuchando")
            response_bytes_length = self.socket_cliente.recv(4)
            response_length = int.from_bytes(response_bytes_length, byteorder="big")
            response = bytearray()

            print("Recibiendo respuesta del servidor...")

            for i in range(response_length // 32 + 1):
                print("Recibiendo bloque", i)
                numero_bloque_bytes = self.socket_cliente.recv(4)
                numero_bloque = int.from_bytes(numero_bloque_bytes, byteorder="little")
                print("Codificando bloque numero", numero_bloque)

                mensaje_bloque_bytes = self.socket_cliente.recv(32)
                print("Mensaje recibido:", mensaje_bloque_bytes)
                response += mensaje_bloque_bytes

            received = self.decodificar(response)
            print("Recibido:", received)

            self.message_handler(received)

    def send_response(self, response):
        """envía una respuesta al servidor"""
        print("Enviando respuesta:", response)
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

        print("Mensaje recibido:", mensaje)

        mensaje = mensaje.split(";")
        tipo = mensaje[0]

        if tipo == "LOGIN":
            self.manejar_login(mensaje)

        elif tipo == "INICIAR_PARTIDA":
            jugadores = mensaje[1].split(",")
            print(f"INICIAR_PARTIDA, {jugadores}")
            self.manejar_iniciar_partida(jugadores)

    def manejar_login(self, mensaje):

        print("Mensaje recibido:", mensaje)

        if mensaje[1] == "True":

            print(f"usuario {mensaje[2]}", mensaje[3])
            self.username = str(mensaje[3])
            print("emitir señal")
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
