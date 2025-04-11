class Laptop:
    def __init__(self, marca, procesador, memoria, costo = 500, impuesto = 10):
        self.marca = marca
        self.procesador = procesador
        self.memorio = memoria
        self.costo = costo
        self.impuesto = impuesto

    def valor_final(self):
        return self.costo + self.impuesto
    
    def valor_descuento(self, descuento):
        return(self.costo*descuento)/100

laptop_Pepito = Laptop("Lenovo", "i7", 32)

print(laptop_Pepito.__dict__)
print(f"Valor del producto: {laptop_Pepito.valor_final()}")
print(f"Valor de descuento: {laptop_Pepito.valor_descuento(10)}")