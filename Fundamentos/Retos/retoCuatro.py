datos = []


cantidad = int(input("Ingrese la cantidad de datos: "))

for i in range(cantidad):
    dato = input(f"Ingrese el dato {i+1}: ")
    try:
        num = float(dato)
        datos.append(num)
    except ValueError:
        datos.append(dato)


print(f"Su lista es : {datos} ")