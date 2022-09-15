class Objeto:
    def __init__(self, nombre: str, tipo: str):
        self.nombre = nombre
        self.tipo = tipo  # Baya, Pocion, Caramelo
        self.costo = None
        self.probabilidad_efecto = None

    def aplicar_objeto(self):
        pass

    pass
