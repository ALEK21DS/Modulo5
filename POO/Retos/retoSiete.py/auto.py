class Auto:
    def __init__(self, marca, modelo, anio, kilometraje = 0):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = kilometraje
    
    def mostrar_informacion(self):
        return (f"Auto: \n {self.marca} \n {self.modelo} \n {self.anio}")
    
    def actualizar_kilometraje(self, kilometraje):
        if self.kilometraje < kilometraje:
            self.kilometraje = kilometraje
            return (f"El kilometreje ha sido actualizado a: {kilometraje} \n")
        else:
            return ("No se puede reducir el kilometraje \n")
        
    def realizar_viaje(self, kilometros):
        if kilometros > 0:
            self.kilometraje = self.kilometraje + kilometros
            return (f"Kilometraje final: {self.kilometraje} \n")
        else:
            return ("La cantidad de kilometros debe ser positiva \n")
        
    def estado_auto(self):
        if self.kilometraje < 20000:
            return (f"Estado del vehiculo: \n Kilometraje: {self.kilometraje} \n Estoy como nuevo!!!")
        elif self.kilometraje >= 20000 and self.kilometraje <= 100000:
            return (f"Estado del vehiculo: \n Kilometraje: {self.kilometraje} \n Ya estoy usado")
        elif self.kilometraje > 100000:
            return (f"Estado del vehiculo: \n Kilometraje: {self.kilometraje} \n Ya dejame descansar porfavor!!!")
        
    @classmethod
    def auto_anio(cls):
        marca = "Toyota"
        modelo = "RAV4"
        anio = 2025
        return cls(marca, modelo, anio)
    
    @staticmethod
    def comparar_auto(auto1, auto2):
        if auto1.kilometraje == auto2.kilometraje:
            return "Los autos tienen el mismo kilometraje"
        return "Los autos tienen diferente kilometraje"

    @classmethod
    def auto_usados(cls, anio, kilometraje):
        marca = "Chevrolet"
        modelo = "Aveo"
        return cls(marca, modelo, anio, kilometraje)
    
    @staticmethod
    def comparar_anio(auto1, auto2):
        if auto1.anio == auto2.anio:
            return "Los autos son del mismo anio"
        return "Los autos son de distinto anio"