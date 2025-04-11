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

auto_Marco = Auto("Kia", "Soluto", "2018")

print(auto_Marco.mostrar_informacion())

actualizacion = float(input("Ingrese el kilometraje a actualizar: "))
print(auto_Marco.actualizar_kilometraje(actualizacion))

kilometros_viaje = float(input("Usted a realizado un viaje \n Ingrese los kilometros del viaje: "))
print(auto_Marco.realizar_viaje(kilometros_viaje))

print(auto_Marco.estado_auto())