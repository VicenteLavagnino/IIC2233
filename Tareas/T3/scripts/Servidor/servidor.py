# en este archivo se define la clase Servidor

import socket
import threading
import json
from logica import Logica


class Servidor:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket_servidor = None
        self.conectado = False
        print("Servidor creado con éxito!")
        self.sockets_totales = []
        self.logica = Logica(self)
        self.lock = threading.Lock()
        self.iniciar_servidor()

    def iniciar_servidor(self):
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # bind & listen
        self.socket_servidor.bind((self.host, self.port))
        self.socket_servidor.listen()
        self.conectado = True
        print(f"Servidor iniciado, host: {self.host}, puerto: {self.port}")
        self.accept_connections()

    def accept_connections(self):
        """acepta nuevas conexiones"""
        thread = threading.Thread(target=self.accept_connections_thread)
        thread.start()

    def accept_connections_thread(self):

        print("Aceptando nuevas conexiones...")

        while self.conectado:
            client_socket, _ = self.socket_servidor.accept()
            listening_client_thread = threading.Thread(
                target=self.listen_client_thread, args=(client_socket,), daemon=True
            )
            listening_client_thread.start()

    def listen_client_thread(self, client_socket):
        """escucha los mensajes del cliente"""
        print("Escuchando cliente...")

        while self.conectado:
            response_bytes_length = client_socket.recv(4)
            response_length = int.from_bytes(response_bytes_length, byteorder="big")
            response = bytearray()

            for i in range(response_length // 32 + 1):
                numero_bloque_bytes = client_socket.recv(4)
                numero_bloque = int.from_bytes(numero_bloque_bytes, byteorder="little")
                print("Codificando bloque numero", numero_bloque)

                mensaje_bloque_bytes = client_socket.recv(32)
                response += mensaje_bloque_bytes
                print("mensaje bloque:", mensaje_bloque_bytes)

            received = self.decodificar(response)
            print("Mensaje recibido:", received)

            self.logica.message_handler(received, client_socket)

    def send_response(self, response, client_socket):
        """envía una respuesta al cliente"""

        with self.lock:

            print("Enviando respuesta:", response)
            response = self.codificar(response)

            len_response = len(response)
            len_response_bytes = len_response.to_bytes(4, byteorder="big")
            mensaje = bytearray()

            mensaje += len_response_bytes

            for i in range(len_response // 32):
                numero_bloque = i.to_bytes(4, byteorder="little")
                mensaje += numero_bloque

                mensaje += bytearray(response[:32], encoding="utf-8")
                response = response[32:]

            if len(response) > 0:
                i = len_response // 32
                i = i.to_bytes(4, byteorder="little")
                mensaje += i

                for _ in range(32 - len(response)):
                    response += " "
                mensaje += bytearray(response, encoding="utf-8")

            print("Mensaje a enviar:", mensaje)
            return client_socket.sendall(mensaje)

    def codificar(self, mensaje):
        mensaje = json.dumps(mensaje)
        return mensaje

    def decodificar(self, mensaje):

        print("Decodificando mensaje:", mensaje)
        mensaje = json.loads(mensaje)
        print("Mensaje decodificado:", mensaje)
        return mensaje

    def handle_command(self, received, client_socket):
        print("Comando recibido:", received)
        # Este método debería ejecutar la acción y enviar una respuesta.
        return "Acción asociada a " + received
