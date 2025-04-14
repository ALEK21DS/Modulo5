from laptop import Laptop
import random
class Laptop_Empresarial(Laptop):
    def __init__(self, marca, procesador, memoria, almacenamiento, duracion_bateria, costo=500, impuesto=10):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.almacenamiento = almacenamiento
        self.duracio_bateria = duracion_bateria

    def __str__(self):
        return f" Marca {self.marca} \n Procesador {self.procesador} \n Memoria {self.memoria} \n Almacenamiento {self.almacenamiento} \n Duracion Bateria {self.duracio_bateria} \n Costo {self.costo} \n Impuesto {self.impuesto} \n"

    def realizar_diagnostico_sistema(self):
        resultado_diagnostico = super().realizar_diagnostico_sistema()
        resultado_almacenamiento = self.resultado_diagnostico_almacenamiento()
        resultado_conectividad = self.verificar_conectividad_red()
        resultado_diagnostico["Resultado almacenamiento"] = resultado_almacenamiento
        resultado_diagnostico["Resultado conectividad"] = resultado_conectividad
        return resultado_diagnostico
    
    def resultado_diagnostico_almacenamiento(self):
        almacenamiento_usado = random.randint(25, self.almacenamiento)
        resultado = " "
        if almacenamiento_usado <= (self.almacenamiento*0.25):
            resultado = f"Su almacenamiento esta casi vacio: {almacenamiento_usado}/{self.almacenamiento}"
        elif almacenamiento_usado > (self.almacenamiento*0.25) and almacenamiento_usado < (self.almacenamiento*0.75):
            resultado = f"Su almacenamiento esta por la mitad: {almacenamiento_usado}/{self.almacenamiento}"
        else:
            resultado = f"Su almacenamiento esta casi lleno: {almacenamiento_usado}/{self.almacenamiento}"
        
        return resultado
    
    def verificar_conectividad_red(self):
        conectividad = ["DISPONIBILIDAD DE WIFI", "ACCESO A SERVIDORES", "LATENCIA DE RED"]
        resultados = {}
        for i in conectividad:
            ran = random.choice([True, False])
            if ran == True:
                res = "SI"
            else:
                res = "NO"

            resultados [i] = f"{res}"
        return resultados
    pass