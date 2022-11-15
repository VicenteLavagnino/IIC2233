def desencriptar(msg: bytearray) -> bytearray:
    # Completar con el proceso de desencriptación

    A = []
    B = []
    C = []

    mensaje = bytearray()

    if msg[0] == 0:

        msg = msg[1:]

        largo = len(msg)

        if largo % 3 == 0:
            largo_A = largo / 3
            largo_B = largo / 3
            largo_C = largo / 3

        elif largo % 3 == 1:
            largo_B = (largo - 1) / 3
            largo_C = (largo - 1) / 3
            largo_A = (largo + 2) / 3

        elif largo % 3 == 2:
            largo_C = (largo - 2) / 3
            largo_A = (largo + 1) / 3
            largo_B = (largo + 1) / 3

        i = 0
        print("Largo A: ", largo_A)
        print("Largo B: ", largo_B)
        print("Largo C: ", largo_C)

        while i != largo_C - 1:
            C.append(msg[0])
            msg = msg[1:]
            i += 1

        while i != largo_A - 1:
            A.append(msg[0])
            msg = msg[1:]
            i += 1

        while i != largo_B - 1:
            B.append(msg[0])
            msg = msg[1:]
            i += 1

        print(A)
        print(B)
        print(C)

        mensaje.extend(bytes(C))
        mensaje.extend(bytes(A))
        mensaje.extend(bytes(B))

    elif msg[0] == 1:

        msg = msg[1:]

        largo = len(msg)

        if largo % 3 == 0:
            largo_A = largo_B = largo_C = largo / 3

        elif largo % 3 == 1:
            largo_B = largo_C = (largo - 1) / 3
            largo_A = (largo + 2) / 3

        elif largo % 3 == 2:
            largo_C = (largo - 2) / 3
            largo_A = largo_B = (largo + 1) / 3

        i = 0

        print(msg)

        for i in range(int(largo_A)):
            print("msg en A: ", msg)
            A.append(msg[0])
            msg = msg[1:]

        for i in range(int(largo_B)):
            print("msg en C: ", msg)
            C.append(msg[0])
            msg = msg[1:]

        for i in range(int(largo_C)):
            print("msg en B: ", msg)
            B.append(msg[0])
            msg = msg[1:]

        mensaje.extend(bytes(A))
        mensaje.extend(bytes(C))
        mensaje.extend(bytes(B))

    return mensaje


a = bytearray(b"\x05\x08\x03\x02\x04\x03\x05\x09\x05\x09\x01")

print(a[3])
