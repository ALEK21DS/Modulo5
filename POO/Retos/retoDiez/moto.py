from vehiculo import Vehiculo

class Moto(Vehiculo):
    def __init__(self, marca, modelo, anio, tipo):
        super().__init__(marca, modelo, anio)
        self.tipo = tipo
    
    def descripcion(self):
        descrip = super().descripcion()
        descrip.update({
            "TIPO" : f"{self.tipo}"
        })
        return descrip
    