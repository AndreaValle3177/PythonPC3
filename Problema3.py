
class CIRCULO:
    def __init__(self, radio):
        self.radio = radio  
    
    def calcular_area(self):
        return 3.1416 * (self.radio ** 2)

circulo1 = CIRCULO(20)  
circulo2 = CIRCULO(15)  

print(f"El área del círculo con radio {circulo1.radio} es: {circulo1.calcular_area():.2f}")
print(f"El área del círculo con radio {circulo2.radio} es: {circulo2.calcular_area():.2f}")
