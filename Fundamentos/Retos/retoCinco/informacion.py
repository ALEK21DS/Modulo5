nombre_paciente = []
edad = []
def agregar_nombre(nombre, apellido):
    nombre_paciente.append(f"{nombre} {apellido}")

def agregar_edad(anio_nacimiento):
    edad_actual = 2025-anio_nacimiento
    edad.append(edad_actual)

def imprimir_datos():
    num = len(nombre_paciente)
    for i in range(num):
        print(f"{i+1}. {nombre_paciente[i]} {edad[i]}")

def imprimir_m():
    persona_menor = " "
    persona_mayor = " "
    edad_min = min(edad)
    edad_max = max(edad)
    num2 = len(edad)
    for i in range(num2):
        if edad_min < edad[i] :
            num_edad = edad.index(edad_min)
            persona_menor = nombre_paciente[num_edad]
        else:
            num2_edad = edad.index(edad_max)
            persona_mayor = nombre_paciente[num2_edad]

    
    print(f"{persona_menor} con la edad de {edad_min} anios es menor a los demas pacientes")
    print(f"{persona_mayor} con la edad de {edad_max} anios es mayor a los demas pacientes")
