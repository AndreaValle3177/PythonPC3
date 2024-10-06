class CIRCULO:
    def __init__(self, radio):
        self.radio = radio  
    
    def calcular_area(self):
        return 3.1416 * (self.radio ** 2)


class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = largo  
        self.ancho = ancho 
    
    def calcular_area(self):
        return self.largo * self.ancho


class CUADRADO(RECTANGULO):
    def __init__(self, lado):
        super().__init__(lado, lado)


def validar_numero(numero):
    try:
        valor = float(numero)
        if valor > 0:
            return valor
        else:
            print("Error: Debe ingresar un número positivo.")
            return None
    except ValueError:
        print("Error: Debe ingresar un número válido.")
        return None


def menu():
    while True:
        print("\nMenú:")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            radio = input("Ingrese el radio del círculo: ")
            radio_valido = validar_numero(radio)
            if radio_valido is not None:
                circulo = CIRCULO(radio_valido)
                print(f"El área del círculo es: {circulo.calcular_area():.2f}")

        elif opcion == "2":
            largo = input("Ingrese el largo del rectángulo: ")
            ancho = input("Ingrese el ancho del rectángulo: ")
            largo_valido = validar_numero(largo)
            ancho_valido = validar_numero(ancho)
            if largo_valido is not None and ancho_valido is not None:
                rectangulo = RECTANGULO(largo_valido, ancho_valido)
                print(f"El área del rectángulo es: {rectangulo.calcular_area():.2f}")

        elif opcion == "3":
            lado = input("Ingrese el lado del cuadrado: ")
            lado_valido = validar_numero(lado)
            if lado_valido is not None:
                cuadrado = CUADRADO(lado_valido)
                print(f"El área del cuadrado es: {cuadrado.calcular_area():.2f}")

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Error: Opción no válida. Por favor, seleccione una opción entre 1 y 4.")


if __name__ == "__main__":
    menu()
