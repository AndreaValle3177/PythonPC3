def sumar(a, b):
    try:
        return a + b
    except TypeError:
        return "Error: Tipo de dato no válido."

def restar(a, b):
    try:
        return a - b
    except TypeError:
        return "Error: Tipo de dato no válido."

def multiplicar(a, b):
    try:
        return a * b
    except TypeError:
        return "Error: Tipo de dato no válido."

def dividir(a, b):
    try:
        if b == 0:
            return "Error: No es posible dividir entre cero."
        return a / b
    except TypeError:
        return "Error: Tipo de dato no válido."
