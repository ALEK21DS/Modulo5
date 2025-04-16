class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        
    def descripcion(self):
        descripcion = {
            "MARCA" : f"{self.marca}",
            "MODELO" : f"{self.modelo}",
            "ANIO" : f"{self.anio}"
        }
        return descripcion