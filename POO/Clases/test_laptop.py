from laptop import Laptop
from laptop_gaming import Laptop_Gaming
from laptop_business import Laptop_Empresarial

def imprimir_informe(laptop):
    informe = laptop.realizar_informe_uso()
    for clave, valor in informe.items():
        print(f"{clave} : {valor}")
    print("\n")

laptop_Pepito = Laptop("Lenovo", "i7", 32)
laptop_Maria = Laptop("Lenovo", "i7", 32, 600)

laptop_Juanito = Laptop_Gaming("MSI", "i7", 4, "RTX 8GB")

laptop_oficina = Laptop_Empresarial("DELL", "i5", 16, 250, 4)

# for numero in range(1, 3):
#     asus_laptop = Laptop.asus_laptop(numero)
#     print(asus_laptop.__dict__)
# #print(Laptop.comparar_costo(laptop_Pepito, laptop_Maria))

# print(laptop_Juanito.realizar_diagnostico_sistema())


# print(laptop_oficina.realizar_diagnostico_sistema())
print("PEPITO: ")
imprimir_informe(laptop_Pepito)
print("JUANITO: ")
imprimir_informe(laptop_Juanito)

