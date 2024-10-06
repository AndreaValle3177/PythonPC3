import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x  
        self.y = y  
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            return "Está en el origen"
        elif self.x == 0:
            return "Está sobre el eje Y"
        elif self.y == 0:
            return "Está sobre el eje X"
        elif self.x > 0 and self.y > 0:
            return "Cuadrante I"
        elif self.x < 0 and self.y > 0:
            return "Cuadrante II"
        elif self.x < 0 and self.y < 0:
            return "Cuadrante III"
        else:
            return "Cuadrante IV"
    
    def vector(self, otro):
        return (otro.x - self.x, otro.y - self.y)

    def distancia(self, otro):
        return math.sqrt((otro.x - self.x) ** 2 + (otro.y - self.y) ** 2)

class Rectangulo:
    def __init__(self, punto_inicial=None, punto_final=None):
        self.punto_inicial = punto_inicial if punto_inicial else Punto(0, 0)
        self.punto_final = punto_final if punto_final else Punto(0, 0)
    
    def base(self):
        return abs(self.punto_final.x - self.punto_inicial.x)
    
    def altura(self):
        return abs(self.punto_final.y - self.punto_inicial.y)
    
    def area(self):
        return self.base() * self.altura()

A = Punto(2, 3)
B = Punto(5, 5)
C = Punto(-3, -1)
D = Punto(0, 0)

print("Puntos:")
print("A:", A)
print("B:", B)
print("C:", C)
print("D:", D)

print("\nCuadrantes:")
print(f"A {A} -> {A.cuadrante()}")
print(f"C {C} -> {C.cuadrante()}")
print(f"D {D} -> {D.cuadrante()}")

vector_AB = A.vector(B)
vector_BA = B.vector(A)
print(f"\nVector AB: {vector_AB}")
print(f"Vector BA: {vector_BA}")

distancia_AB = A.distancia(B)
distancia_BA = B.distancia(A)
print(f"\nDistancia entre A y B: {distancia_AB}")
print(f"Distancia entre B y A: {distancia_BA}")

distancias = {
    "A": A.distancia(Punto(0, 0)),
    "B": B.distancia(Punto(0, 0)),
    "C": C.distancia(Punto(0, 0)),
}

punto_mas_lejos = max(distancias, key=distancias.get)
print(f"\nEl punto más lejano del origen es: {punto_mas_lejos} con distancia {distancias[punto_mas_lejos]}")

rectangulo = Rectangulo(A, B)

print("\nRectángulo:")
print(f"Base: {rectangulo.base()}")
print(f"Altura: {rectangulo.altura()}")
print(f"Área: {rectangulo.area()}")

