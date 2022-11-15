import json
from os.path import join


def json_reader(key):
    """Lee el archivo json y retorna el valor de la llave"""
    ruta = join("parametros.json")

    with open(ruta, "r", encoding="UTF-8") as archivo:
        data = json.load(archivo)
    valor = data[key]
    return valor
