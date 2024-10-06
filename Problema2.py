def obtener_calificaciones():
    while True:
        try:
            calificaciones_lista = input("Ingresa las calificaciones, recuerda que deben estar separadas por comas: ")
            
            calificaciones_lista = calificaciones_lista.split(',')
            
            calificaciones = [int(calificacion.strip()) for calificacion in calificaciones_lista]
            
            print("Calificaciones ingresadas por el usuario:", calificaciones)
            break 
        
        except ValueError:
            # Mostrar un mensaje de error si hay un problema en la conversión
            print("Recuerde que deben ser valores enteros separados por la coma.")

obtener_calificaciones()
