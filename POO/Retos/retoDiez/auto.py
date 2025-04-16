from vehiculo import Vehiculo

class Auto(Vehiculo):
    def __init__(self, marca, modelo, anio, num_puertas):
        super().__init__(marca, modelo, anio)
        self.num_puertas = num_puertas

    def descripcion(self):
        descrip =  super().descripcion()
        descrip.update({
            "NUMERO DE PUERTAS" : f"{self.num_puertas}"
        })
        return descrip
    