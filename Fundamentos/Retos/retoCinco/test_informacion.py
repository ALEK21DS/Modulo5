import informacion

datos = int(input("Ingrese el numero de pacientes que quiere registrar: "))

for i in range(datos):
    print("------------------------------------------------")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    anio_nacimiento = int(input("Ingrese su anio de nacimientio: ")) 
    print("------------------------------------------------")
    print(f"Datos del paciente {i+1} ha sido guardado")
    informacion.agregar_nombre(nombre, apellido)
    informacion.agregar_edad(anio_nacimiento)


informacion.imprimir_datos()
informacion.imprimir_m()