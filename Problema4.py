class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = largo  
        self.ancho = ancho 
    
    def calcular_area(self):
        return self.largo * self.ancho

class CUADRADO(RECTANGULO):
    def __init__(self, lado):
        super().__init__(lado, lado)

rectangulo = RECTANGULO(25, 5)

cuadrado = CUADRADO(10)

print(f"El área del rectángulo es: {rectangulo.calcular_area()}")

print(f"El área del cuadrado es: {cuadrado.calcular_area()}")
