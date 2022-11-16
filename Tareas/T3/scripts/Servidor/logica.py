# en este archivo se define la clase Logica

from helpers_s import json_reader
from time import sleep


class Logica:
    def __init__(self, Servidor):
        self.servidor = Servidor

        # datos
        self.jugadores = []
        self.total_jugadores = json_reader("TOTAL_JUGADORES")

    def message_handler(self, message, socket_cliente):

        # print("Mensaje recibido:", mensaje)

        message = message.split(";")
        tipo = message[0]
        mensaje = message[1]

        if tipo == "LOGIN":
            self.validar_usuario(mensaje, socket_cliente)

        elif tipo == "JUGADA":
            self.manejar_jugada(mensaje, socket_cliente)

        elif tipo == "CHAT":
            self.manejar_chat(mensaje, socket_cliente)

        elif tipo == "JUGARCARTA":
            self.manjejar_jugada(mensaje, socket_cliente)

    def validar_usuario(self, usuario, socket_cliente):

        if len(self.jugadores) >= self.total_jugadores:
            output = "LOGIN;False;lleno"
            self.servidor.send_response(output, socket_cliente)

        elif usuario.lower() in [j.nombre for j in self.jugadores]:
            output = "LOGIN;False;repetido"
            self.servidor.send_response(output, socket_cliente)

        else:
            self.jugadores.append(Jugador(usuario, socket_cliente))

            output = f"LOGIN;True;1;{usuario}"
            self.servidor.send_response(output, socket_cliente)

            if len(self.jugadores) == self.total_jugadores:
                # INICIAR PARTIDA
                output = (
                    f"INICIAR_PARTIDA;{','.join([j.nombre for j in self.jugadores])}"
                )
                # enviar a ambos jugadores
                for j in self.jugadores:
                    self.servidor.send_response(output, j.socket)

    def manejar_chat(self, mensaje_para_oponente, socket_cliente):

        mensaje = f"CHAT;{mensaje_para_oponente}"

        # enviar a ambos jugadores
        for j in self.jugadores:
            if j.socket != socket_cliente:
                self.servidor.send_response(mensaje, j.socket)

    def manejar_jugada(self, mensaje, socket_cliente):

        carta = mensaje.split(",")

        for j in self.jugadores:
            if j.socket == socket_cliente:
                j.cartas_jugada = carta
                sleep(5)

                for j in self.jugadores:
                    resultado = self.enfrentar_cartas()
                    self.servidor.send_response(resultado, j.socket)

    def enfrentar_cartas(self):

        tipo1 = self.jugadores[0].cartas_jugada[1]
        tipo2 = self.jugadores[1].cartas_jugada[1]

        if self.jugadores[0].carta_jugada == self.jugadores[1].carta_jugada:

            return "JUEGO;EMPATE"

        elif tipo1 == "Fuego" and tipo2 == "Agua":
            return f"JUEGO;{self.jugadores[1].nombre}"

        elif tipo1 == "Fuego" and tipo2 == "Nieve":
            return f"JUEGO;{self.jugadores[0].nombre}"

        elif tipo1 == "Agua" and tipo2 == "Fuego":
            return f"JUEGO;{self.jugadores[0].nombre}"

        elif tipo1 == "Agua" and tipo2 == "Nieve":
            return f"JUEGO;{self.jugadores[1].nombre}"

        elif tipo1 == "Nieve" and tipo2 == "Fuego":
            return f"JUEGO;{self.jugadores[1].nombre}"

        elif tipo1 == "Nieve" and tipo2 == "Agua":
            return f"JUEGO;{self.jugadores[0].nombre}"

        elif tipo1 == "Nieve" and tipo2 == "Nieve":

            if self.jugadores[0].carta_jugada[2] > self.jugadores[1].carta_jugada[2]:
                return f"JUEGO;{self.jugadores[0].nombre}"
            else:
                return f"JUEGO;{self.jugadores[1].nombre}"

        elif tipo1 == "Agua" and tipo2 == "Agua":

            if self.jugadores[0].carta_jugada[2] > self.jugadores[1].carta_jugada[2]:
                return f"JUEGO;{self.jugadores[0].nombre}"
            else:
                return f"JUEGO;{self.jugadores[1].nombre}"

        elif tipo1 == "Fuego" and tipo2 == "Fuego":

            if self.jugadores[0].carta_jugada[2] > self.jugadores[1].carta_jugada[2]:
                return f"JUEGO;{self.jugadores[0].nombre}"
            else:
                return f"JUEGO;{self.jugadores[1].nombre}"


class Jugador:
    def __init__(self, nombre, socket_cliente):
        self.nombre = nombre
        self.socket = socket_cliente
        self.carta_jugada = []
