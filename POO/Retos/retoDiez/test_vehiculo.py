from vehiculo import Vehiculo
from auto import Auto
from moto import Moto

vehiculos = [
    Auto("Honda", "Civic", 2020, 4),
    Moto("Susuki", "Gixxer" , 2025, "Deportiva")
    ]

for vehiculo in vehiculos:
    print(vehiculo.descripcion())