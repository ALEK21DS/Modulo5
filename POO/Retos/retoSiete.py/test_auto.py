from auto import Auto
import random

# Test Metodo 1
print("Autos del anio: ")
for i in range (1,25):
    auto_anio = Auto.auto_anio()
    print(f"{i}. {auto_anio.__dict__}")

# Test Metodo 2
auto_Marco = Auto("Kia", "Soluto", 2018)
auto_Maria = Auto("Chevrolet", "Aveo", 2018, 20000)
print(" ")
print("Comparacion de autos: \n")
print(Auto.comparar_auto(auto_Marco, auto_Maria))
print(f" Auto de Marco: {auto_Marco.kilometraje} \n Auto de Maria: {auto_Maria.kilometraje} \n")

# Test Metodo 3

print("Se han ingresado 25 autos usados de marca chevrolet: \n")
for i in range (1, 26):
    anio_us = random.randint(2001,2019)
    kilometraje_ran = random.randint(20000, 100000)
    auto_usado = Auto.auto_usados(anio_us, kilometraje_ran)
    print(f"{i}. {auto_usado.__dict__}")

# Test Metodo 4
print("\n Metodo estatico: \n")
print(Auto.comparar_anio(auto_Marco, auto_Maria))