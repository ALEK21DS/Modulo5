from laptop import Laptop


laptop_Pepito = Laptop("Lenovo", "i7", 32)
laptop_Maria = Laptop("Lenovo", "i7", 32, 600)


for numero in range(1, 1001):
    asus_laptop = Laptop.asus_laptop(numero)
    print(asus_laptop.__dict__)
#print(Laptop.comparar_costo(laptop_Pepito, laptop_Maria))