from empleado import Empleado
from empleado_tc import EmpleadoTiempoCompleto
from empleado_mt import EmpleadoMedioTiempo

empleados = [
    EmpleadoTiempoCompleto("Juan", 600),
    EmpleadoMedioTiempo("Carlos", 400)
]

for empleado in empleados:
    print(f"{empleado.nombre}")
    print(f" Salario: {empleado.calcular_salario()}")

