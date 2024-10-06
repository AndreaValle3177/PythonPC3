from operaciones import sumar, restar, multiplicar, dividir

def main():
    print("Suma:", sumar(10, 5))                  
    print("Resta:", restar(10, 5))                  
    print("Multiplicación:", multiplicar(10, 5))    
    print("División:", dividir(10, 5))              

    # Ejemplos con errores
    print("Suma (error):", sumar(10, "a"))         
    print("División (error):", dividir(10, 0))      

if __name__ == "__main__":
    main()
