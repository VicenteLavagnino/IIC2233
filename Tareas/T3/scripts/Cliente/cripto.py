def encriptar(msg: bytearray) -> bytearray:
    # Completar con el proceso de encriptación

    msg = bytes(msg)

    A = []
    B = []
    C = []

    encriptado = bytearray()

    for i in range(len(msg)):

        if i % 3 == 0:
            A.append(msg[i])

        if abs(i - 1) % 3 == 0:
            B.append(msg[i])

        if abs(i - 2) % 3 == 0:
            C.append(msg[i])

    valor_1A = A[0]

    if len(B) % 2 == 1:
        valor_MB = B[int((len(B) - 1) / 2)]

    elif len(B) % 2 == 0:
        valor_MB = B[int(len(B) / 2)] + B[(int(len(B) / 2)) - 1]

    valor_FC = C[-1]

    suma = valor_1A + valor_MB + valor_FC

    if suma % 2 == 0:
        encriptado.extend(b"\x00")
        encriptado.extend(bytes(C))
        encriptado.extend(bytes(A))
        encriptado.extend(bytes(B))
        # print("Encriptado con el primer algoritmo: ", encriptado)

    elif suma % 2 == 1:
        encriptado.extend(b"\x01")
        encriptado.extend(bytes(A))
        encriptado.extend(bytes(C))
        encriptado.extend(bytes(B))
        # print("Encriptado con el segundo algoritmo: ", encriptado)

    return encriptado


def desencriptar(msg: bytearray) -> bytearray:
    # Completar con el proceso de desencriptación

    A = []
    B = []
    C = []

    mensaje = []

    # definir largos

    cantidad_celdas = len(msg) - 1

    if cantidad_celdas % 3 == 0:
        largo_A = int(cantidad_celdas / 3)
        largo_B = int(cantidad_celdas / 3)
        largo_C = int(cantidad_celdas / 3)

    elif cantidad_celdas % 3 == 1:
        largo_A = int((cantidad_celdas + 2) / 3)
        largo_B = int((cantidad_celdas - 1) / 3)
        largo_C = int((cantidad_celdas - 1) / 3)

    elif cantidad_celdas % 3 == 2:
        largo_A = int((cantidad_celdas + 1) / 3)
        largo_B = int((cantidad_celdas + 1) / 3)
        largo_C = int((cantidad_celdas - 2) / 3)

    if msg[0] == 0:

        msg = msg[1:]

        for i in range(largo_C):
            C.append(msg[0])
            msg = msg[1:]

        for i in range(largo_A):
            A.append(msg[0])
            msg = msg[1:]

        for i in range(largo_B):
            B.append(msg[0])
            msg = msg[1:]

    elif msg[0] == 1:

        msg = msg[1:]

        for i in range(largo_A):
            A.append(msg[0])
            msg = msg[1:]

        for i in range(largo_C):
            C.append(msg[0])
            msg = msg[1:]

        for i in range(largo_B):
            B.append(msg[0])
            msg = msg[1:]

    for i in range(cantidad_celdas):

        if i % 3 == 0:
            mensaje.append(A[0])
            A = A[1:]

        if abs(i - 1) % 3 == 0:
            mensaje.append(B[0])
            B = B[1:]

        if abs(i - 2) % 3 == 0:
            mensaje.append(C[0])
            C = C[1:]

    mensaje = bytes(mensaje)

    return mensaje


if __name__ == "__main__":
    # Testear encriptar
    msg_original = bytearray(b"\x05\x08\x03\x02\x04\x03\x05\x09\x05\x09\x01")
    msg_esperado = bytearray(b"\x01\x05\x02\x05\x09\x03\x03\x05\x08\x04\x09\x01")

    msg_encriptado = encriptar(msg_original)
    if msg_encriptado != msg_esperado:
        print("encriptando...")
        print(f"actual: {msg_encriptado}")
        print(f"esperado: {msg_esperado}")
        print("[ERROR] Mensaje escriptado erroneamente")
    else:
        print("[SUCCESSFUL] Mensaje escriptado correctamente")

    # Testear desencriptar
    msg_desencriptado = desencriptar(msg_esperado)
    if msg_desencriptado != msg_original:
        print("desencriptando...")
        print(f"actual: {msg_desencriptado}")
        print(f"esperado: {msg_original}")
        print("[ERROR] Mensaje descencriptado erroneamente")
    else:
        print("[SUCCESSFUL] Mensaje descencriptado correctamente")
