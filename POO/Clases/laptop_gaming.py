from laptop import Laptop

class Laptop_Gaming(Laptop):
    def __init__(self, marca, procesador, memoria, tarj_graf, costo=500, impuesto=10):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.tarj_graf = tarj_graf

    def realizar_diagnostico_sistema(self):
        resultado_diagnostico = super().realizar_diagnostico_sistema()
        resultado_juegos = self.realizar_diagnostico_juegos()
        resultado_diagnostico["Resultado juegos"] = resultado_juegos
        return resultado_diagnostico
    
    def realizar_diagnostico_juegos(self):
        juegos = ["FORTNITE", "COD", "GAT"]
        resultados = {}
        for juego in juegos:
            fps_basic = 30
            if "RTX" in self.tarj_graf:
                fps = fps_basic*3
            elif "GTX" in self.tarj_graf:
                fps = fps_basic*2
            else:
                fps = fps_basic

            resultados [juego] = f"{fps} FPS"

        return resultados
    pass