# en este archivo se define la clase Logica

from helpers_s import json_reader


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


class Jugador:
    def __init__(self, nombre, socket_cliente):
        self.nombre = nombre
        self.socket = socket_cliente
