from empleado import Empleado

class EmpleadoTiempoCompleto(Empleado):
    def calcular_salario(self):
        bono = self.salario_base*0.20
        salario_completo = self.salario_base + bono
        return salario_completo