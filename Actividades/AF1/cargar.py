from collections import namedtuple

# --- EXPLICACION --- #
# los datos vienen en este orden en el .csv:
# nombre,categoria,tiempo_preparacion,precio,ingrediente_1,...,ingrediente_n

# cargar platos retorna una lista de namedtuples, donde cada namedtuple contiene información de un plato

def cargar_platos(ruta_archivo: str) -> list:
    
    lista_notuple = []
    lista_namedtuples = []

    with open(platos.csv, 'r') as platos:
        
        for linea in platos:

            linea = linea.strip()
            linea = linea.split(',')
            linea[4] = linea[4].split(';')

            lista_notuple.append(linea)

    mi_tupla = namedtuple("tupla",["nombre", "categoria", "tiempo_preparacion", "precio", "ingredientes"])

    #convertir lista de listas a lista de namedtuples

    for i in range(len(lista_notuple)):

        lista_namedtuples.append(mi_tupla(lista_notuple[0],lista_notuple[1],lista_notuple[2],lista_notuple[3],lista_notuple[4]))

    return lista_namedtuples


# --- EXPLICACION --- #
# los datos vienen en este orden el el .csv:
# nombre,cantidad

def cargar_ingredientes(ruta_archivo: str) -> dict:

    diccionario = {}

    with open(ingredientes.csv, 'r') as ingredientes:

        for linea in ingredientes:

            linea = linea.strip()
            linea = linea.split(',')

            diccionario[linea[0]] = linea[1]

            pass

    return diccionario
