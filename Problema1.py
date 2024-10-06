print("Obteniendo porcentaje de combustible")  # Corrigiendo la impresión
while True: 
    try:
        fraccion = input("Ingresa fracción (X/Y): ")
        x, y = fraccion.split('/')
        
        x = int(x)
        y = int(y)

        if y == 0:
            raise ZeroDivisionError("El denominador debe ser distinto al número 0")
        if x > y:
            raise ValueError("El numerador no puede ser mayor que el denominador.")
        
        porcentaje = (x / y) * 100
        
        if porcentaje <= 1:
            print("E")  
        elif porcentaje >= 99:
            print("F")  
        else:
            print(f"{round(porcentaje)}%")  
        break  

    except ValueError:
        print("Revisa que sean números enteros en el formato X/Y y de que X <= Y.")
    except ZeroDivisionError:
        print("El denominador no puede ser 0.")
