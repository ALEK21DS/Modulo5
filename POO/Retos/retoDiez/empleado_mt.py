from empleado import Empleado

class EmpleadoMedioTiempo(Empleado):
    def calcular_salario(self):
        bono = self.salario_base * 0.10
        salario_completo = self.salario_base + bono
        return salario_completo
